from uuid import UUID
from fastapi import Depends, HTTPException, Request, status
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token
from sqlalchemy.orm import Session
from .core import Role, settings
from .database import get_db
from .models import User


def verify_google_token(token: str) -> dict:
    if not settings.google_client_id:
        raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, "Google OAuth is not configured")
    try:
        claims = id_token.verify_oauth2_token(token, google_requests.Request(), settings.google_client_id)
    except ValueError as exc:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid Google identity token") from exc
    if not claims.get("sub") or not claims.get("email") or not claims.get("email_verified"):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Google account is not verified")
    return claims


def current_user(request: Request, db: Session = Depends(get_db)) -> User:
    raw_user_id = request.session.get("user_id")
    if not raw_user_id:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Authentication required")
    try:
        user_id = UUID(raw_user_id)
    except ValueError as exc:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid session") from exc
    user = db.get(User, user_id)
    if not user or user.disabled_at:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Session is no longer valid")
    return user


def require_role(*roles: Role):
    def dependency(user: User = Depends(current_user)) -> User:
        if user.role not in roles:
            raise HTTPException(status.HTTP_403_FORBIDDEN, "Insufficient role")
        return user
    return dependency

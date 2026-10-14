from sqlalchemy.types import UserDefinedType


class PgVector(UserDefinedType):
    """Small pgvector adapter that avoids a NumPy runtime dependency."""
    cache_ok = True

    def __init__(self, dimensions: int):
        self.dimensions = dimensions

    def get_col_spec(self, **_: object) -> str:
        return f"vector({self.dimensions})"

    def bind_processor(self, dialect):
        def process(value):
            if value is None:
                return None
            if len(value) != self.dimensions:
                raise ValueError(f"Expected vector with {self.dimensions} dimensions")
            return "[" + ",".join(str(float(item)) for item in value) + "]"
        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            if value is None or isinstance(value, list):
                return value
            return [float(item) for item in value.strip("[]").split(",")]
        return process

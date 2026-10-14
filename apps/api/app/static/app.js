const toast = document.getElementById('toast');
const notify = (message) => { toast.textContent = message; toast.classList.add('show'); setTimeout(() => toast.classList.remove('show'), 3600); };
async function checkHealth() {
  const label = document.getElementById('api-status'); const value = document.getElementById('api-value');
  try { const res = await fetch('/api/v1/health'); const data = await res.json(); if (!res.ok) throw new Error(); label.textContent = 'Trực tuyến'; value.textContent = data.status === 'ok' ? 'Sẵn sàng' : data.status; }
  catch { label.textContent = 'Không kết nối'; value.textContent = '—'; }
}
document.getElementById('health').addEventListener('click', async () => { await checkHealth(); notify('Đã kiểm tra trạng thái API.'); });
document.getElementById('signin').addEventListener('click', () => notify('Google OAuth cần GOOGLE_CLIENT_ID để kích hoạt.'));
document.getElementById('start').addEventListener('click', () => notify('Chọn sự kiện sau khi đăng nhập Google.'));
checkHealth();

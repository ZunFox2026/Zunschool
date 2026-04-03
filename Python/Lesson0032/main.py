import time
import functools

# --- VÍ DỤ 1: Đo thời gian thực thi ---
def timing_decorator(func):
    @functools.wraps(func)  # Giữ nguyên tên, docstring của hàm gốc
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Hàm '{func.__name__}' thực thi trong {end - start:.4f} giây")
        return result
    return wrapper

@timing_decorator
def tinh_tong(n):
    """Tính tổng từ 1 đến n"""
    return sum(range(1, n + 1))

# --- VÍ DỤ 2: Ghi log hoạt động ---
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Đang gọi hàm: {func.__name__} với args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Hàm {func.__name__} trả về: {result}")
        return result
    return wrapper

@log_calls
def chia(a, b):
    if b == 0:
        raise ValueError("Không thể chia cho 0")
    return a / b

# --- VÍ DỤ 3: Xác thực truy cập ---
def require_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Giả lập kiểm tra đăng nhập
        if not wrapper.is_authenticated:
            print("Lỗi: Bạn cần đăng nhập để thực hiện hành động này.")
            return None
        return func(*args, **kwargs)
    wrapper.is_authenticated = False  # Mặc định chưa đăng nhập
    return wrapper

@require_auth
def xoa_tep_tin(ten_tep):
    print(f"Đã xóa tệp: {ten_tep}")

# --- Chạy các ví dụ ---
if __name__ == "__main__":
    print("=== Ví dụ 1: Đo thời gian ===")
    ket_qua = tinh_tong(100000)
    print(f"Kết quả: {ket_qua}\n")

    print("=== Ví dụ 2: Ghi log ===")
    try:
        chia(10, 2)
    except Exception as e:
        print(f"Lỗi: {e}\n")

    print("=== Ví dụ 3: Xác thực ===")
    xoa_tep_tin("document.txt")  # Sẽ báo lỗi vì chưa đăng nhập

    # Đăng nhập thành công
    xoa_tep_tin.is_authenticated = True
    xoa_tep_tin("document.txt")  # Thành công
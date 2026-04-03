import time
import functools

# --- VÍ DỤ 1: Decorator ghi log ---
def log_decorator(func):
    """
    Decorator ghi lại khi một hàm được gọi và khi hoàn tất.
    """
    def wrapper(*args, **kwargs):
        print(f"[LOG] Đang gọi hàm: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Hàm {func.__name__} đã hoàn tất.")
        return result
    return wrapper

@log_decorator
def tinh_tong(a, b):
    """Tính tổng hai số"""
    return a + b

# --- VÍ DỤ 2: Đo thời gian thực thi ---
def time_decorator(func):
    """
    Decorator đo thời gian thực thi của hàm.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] Hàm '{func.__name__}' thực thi trong {end - start:.4f} giây")
        return result
    return wrapper

@time_decorator
def tinh_giai_thua(n):
    """Tính giai thừa theo đệ quy"""
    if n <= 1:
        return 1
    return n * tinh_giai_thua(n - 1)

# --- VÍ DỤ 3: Decorator có tham số (Xác thực quyền) ---
def require_role(role_required):
    """
    Tạo decorator yêu cầu vai trò cụ thể.
    """
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != role_required:
                print(f"[AUTH] Từ chối truy cập! Cần quyền: {role_required}, bạn có: {user_role}")
                return None
            print(f"[AUTH] Truy cập được cấp cho quyền: {user_role}")
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def xoa_nguoi_dung(user_role):
    """Hàm xóa người dùng (chỉ admin mới được dùng)"""
    print("[ACTION] Đã xóa người dùng thành công!")

# --- Chạy các ví dụ ---
if __name__ == "__main__":
    print("=== Ví dụ 1: Log decorator ===")
    ket_qua_tong = tinh_tong(5, 7)
    print(f"Kết quả: {ket_qua_tong}\n")

    print("=== Ví dụ 2: Time decorator ===")
    ket_qua_gt = tinh_giai_thua(5)
    print(f"Giai thừa(5) = {ket_qua_gt}\n")

    print("=== Ví dụ 3: Decorator có tham số ===")
    xoa_nguoi_dung("admin")      # Được phép
    xoa_nguoi_dung("user")       # Bị từ chối
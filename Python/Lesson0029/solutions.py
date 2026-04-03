import functools

# --- Bài tập 1: Tạo decorator retry ---

def retry(max_attempts=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Lỗi: {e}, thử lại lần {attempts}/{max_attempts}...")
                    if attempts >= max_attempts:
                        print("Vượt quá số lần thử. Đẩy lỗi lên.")
                        raise e
            return None  # Không cần, vì raise ở trên
        return wrapper
    return decorator

# --- Bài tập 2: Tạo decorator only_admin ---

def only_admin(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        # Giả sử tham số đầu tiên là user
        if user.get('role') != 'admin':
            print(f"[Từ chối] Người dùng '{user.get('name')}' không có quyền admin.")
            return None
        return func(user, *args, **kwargs)
    return wrapper

# --- Bài tập 3: Tạo decorator cache_result ---

def cache_result(func):
    cache = {}  # Dictionary lưu kết quả
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Tạo key từ args và kwargs
        key = (args, frozenset(kwargs.items()))
        
        if key in cache:
            print(f"[Cache] Trả về kết quả đã lưu cho {func.__name__}")
            return cache[key]
        
        # Nếu chưa có, tính toán và lưu vào cache
        result = func(*args, **kwargs)
        cache[key] = result
        print(f"[Cache] Lưu kết quả cho {func.__name__}")
        return result
    
    return wrapper

# --- Kiểm thử lời giải ---
if __name__ == "__main__":
    print("=== Kiểm thử @retry ===")
    
    @retry(max_attempts=3)
    def ham_loi_ngau_nhien():
        import random
        if random.random() < 0.7:
            raise ValueError("Lỗi giả lập!")
        return "Thành công!"
    
    try:
        print(ham_loi_ngau_nhien())
    except:
        print("Thử lại thất bại hoàn toàn.\n")
    
    print("\n=== Kiểm thử @only_admin ===")
    
    @only_admin
    def sua_du_lieu(user, data_id):
        print(f"[OK] Sửa dữ liệu ID={data_id}")
        return True
    
    user1 = {'name': 'Minh', 'role': 'admin'}
    user2 = {'name': 'Hoa', 'role': 'user'}
    
    sua_du_lieu(user1, 100)
    sua_du_lieu(user2, 200)
    
    print("\n=== Kiểm thử @cache_result ===")
    
    @cache_result
    def tinh_binh_phuong(x):
        print(f"Tính bình phương của {x}...")
        return x ** 2
    
    print(tinh_binh_phuong(4))  # Tính lần đầu
    print(tinh_binh_phuong(4))  # Dùng cache
    print(tinh_binh_phuong(5))  # Tính mới
    print(tinh_binh_phuong(4))  # Dùng cache

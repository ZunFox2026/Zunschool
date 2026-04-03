import inspect
from functools import wraps

def ham_bai_tap(x: int, y: str = "test", z: list = None):
    if z is None:
        z = []
    return x > 0 and len(y) in z

class LopBaiTap:
    def __init__(self, gia_tri: int):
        self.gia_tri = gia_tri

    def phuong_thuc_1(self, a: float) -> float:
        return a * self.gia_tri

    def phuong_thuc_2(self, b: str = "ok") -> bool:
        return b == "ok"

# Bài tập 1: In thông tin chi tiết về một hàm
def in_thong_tin_ham(func):
    """In ra thông tin chi tiết về một hàm"""
    print(f"Tên hàm: {func.__name__}")
    print(f"Định nghĩa: {func.__doc__ or 'Không có'}")
    
    sig = inspect.signature(func)
    print("Tham số:")
    for name, param in sig.parameters.items():
        kieu = param.annotation if param.annotation != inspect._empty else "Không xác định"
        mac_dinh = param.default if param.default != inspect._empty else "Không có"
        print(f"  - {name}: kiểu {kieu}, mặc định = {mac_dinh}")

# Bài tập 2: Kiểm tra tính hợp lệ của tham số khi gọi hàm
def kiem_tra_loi_goi(func, *args, **kwargs):
    """Kiểm tra xem việc gọi hàm có hợp lệ không"""
    sig = inspect.signature(func)
    try:
        # Bind tham số vào chữ ký hàm
        sig.bind(*args, **kwargs)
        return True, "Hợp lệ"
    except TypeError as e:
        return False, str(e)

# Bài tập 3: Viết decorator @theo_doi
def theo_doi(func):
    """Decorator ghi log tên hàm, tham số và kết quả"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy tên tham số
        sig = inspect.signature(func)
        param_names = list(sig.parameters.keys())
        
        # Ghép tên và giá trị tham số
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        all_args = args_repr + kwargs_repr
        
        print(f"[GỌI] {func.__name__}({', '.join(all_args)})")
        
        result = func(*args, **kwargs)
        
        print(f"[TRẢ VỀ] {func.__name__} -> {repr(result)}")
        return result
    return wrapper

# Bài tập 4: Tìm và in thông tin về một phương thức trong lớp
def tim_phuong_thuc_cua_lop(cls, ten_phuong_thuc):
    """Tìm phương thức trong lớp và in thông tin chi tiết"""
    try:
        # Lấy phương thức từ lớp
        phuong_thuc = getattr(cls, ten_phuong_thuc)
        
        # Kiểm tra có phải là hàm không
        if inspect.isfunction(phuong_thuc) or inspect.ismethod(phuong_thuc):
            print(f"Tìm thấy phương thức '{ten_phuong_thuc}' trong lớp {cls.__name__}")
            in_thong_tin_ham(phuong_thuc)
        else:
            print(f"'{ten_phuong_thuc}' tồn tại nhưng không phải là phương thức.")
    except AttributeError:
        print(f"Lớp {cls.__name__} không có phương thức '{ten_phuong_thuc}'")

# --- Demo lời giải ---
if __name__ == "__main__":
    print("=== Bài tập 1 ===")
    in_thong_tin_ham(ham_bai_tap)
    
    print("\n=== Bài tập 2 ===")
    print(kiem_tra_loi_goi(ham_bai_tap, 5, "abc", z=[3, 4]))
    print(kiem_tra_loi_goi(ham_bai_tap, "sai", "abc"))  # Sai kiểu
    
    print("\n=== Bài tập 3 ===")
    @theo_doi
    def ham_thu(x, y=10):
        return x + y
    
    ham_thu(5)
    ham_thu(3, y=7)
    
    print("\n=== Bài tập 4 ===")
    tim_phuong_thuc_cua_lop(LopBaiTap, "phuong_thuc_1")
    tim_phuong_thuc_cua_lop(LopBaiTap, "khong_ton_tai")
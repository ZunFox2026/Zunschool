import inspect
import functools
import datetime

# --- Ví dụ 1: Tự động ghi log tham số đầu vào của hàm ---
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy signature của hàm
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        # Ghi log
        print(f"[{datetime.datetime.now()}] Gọi hàm: {func.__name__}")
        for name, value in bound_args.arguments.items():
            print(f"  {name} = {value} (kiểu: {type(value).__name__})")

        return func(*args, **kwargs)
    return wrapper

@log_calls
def greet(name: str, age: int = 18, active: bool = True):
    print(f"Xin chào {name}, bạn {age} tuổi.")
    if active:
        print("Bạn đang hoạt động.")

# Gọi hàm để xem log
greet("An", 25, False)


# --- Ví dụ 2: Trích xuất thông tin hàm để tạo tài liệu API đơn giản ---
def describe_function(func):
    """
    In mô tả chi tiết về một hàm: tên, docstring, tham số, kiểu, giá trị mặc định.
    """
    print(f"Hàm: {func.__name__}")
    print(f"Docstring: {func.__doc__ or 'Không có'}")

    sig = inspect.signature(func)
    print("Tham số:")
    for name, param in sig.parameters.items():
        annotation = param.annotation if param.annotation != inspect.Parameter.empty else "không xác định"
        default = param.default if param.default != inspect.Parameter.empty else "không có"
        print(f"  {name}: kiểu={annotation}, mặc định={default}")

    print("---")

def calculate_area(length: float, width: float = 1.0) -> float:
    """Tính diện tích hình chữ nhật."""
    return length * width

def connect(host: str, port: int = 8080, ssl: bool = True):
    """Kết nối đến server."""
    pass

# In mô tả
print("Mô tả các hàm:")
describe_function(calculate_area)
describe_function(connect)


# --- Ví dụ 3: Kiểm tra loại tham số tại thời điểm chạy ---
def type_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for name, value in bound_args.arguments.items():
            param = sig.parameters[name]
            # Kiểm tra type hint
            expected_type = param.annotation
            if expected_type != inspect.Parameter.empty:
                if not isinstance(value, expected_type):
                    print(f"Cảnh báo: Tham số '{name}' của hàm '{func.__name__}'"
                          f" nên là kiểu {expected_type}, nhưng nhận {type(value)}.")

        return func(*args, **kwargs)
    return wrapper

@type_check
def process_user(name: str, age: int):
    print(f"Xử lý người dùng: {name}, {age} tuổi.")

# Gọi với kiểu không đúng
def main_examples():
    print("\n--- Ví dụ 3: Kiểm tra kiểu ---")
    process_user("Bình", 30)  # OK
    process_user("Lan", "25")  # Cảnh báo

main_examples()
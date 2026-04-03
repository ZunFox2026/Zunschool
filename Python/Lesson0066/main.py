import inspect

class Calculator:
    """Một lớp máy tính đơn giản."""
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def _private_method(self):
        # Phương thức nội bộ
        pass

    def get_history(self):
        return self.history


# Ví dụ 1: Liệt kê tất cả phương thức công khai của lớp
print("=== Ví dụ 1: Liệt kê phương thức công khai ===")
def list_public_methods(cls):
    # Lấy tất cả thành viên của lớp
    members = inspect.getmembers(cls, predicate=inspect.isfunction)
    public_methods = []
    for name, func in members:
        if not name.startswith("_"):
            public_methods.append(name)
    return public_methods

methods = list_public_methods(Calculator)
print("Các phương thức công khai:", methods)


# Ví dụ 2: Trích xuất thông tin tham số hàm
def describe_function(func):
    """In ra mô tả chi tiết về tham số của hàm."""
    sig = inspect.signature(func)
    print(f"Hàm: {func.__name__}")
    print("Tham số:")
    for param in sig.parameters.values():
        default = param.default
        if default == inspect.Parameter.empty:
            default = "không có"
        print(f"  - {param.name}: kiểu {param.annotation}, mặc định = {default}")

print("\n=== Ví dụ 2: Mô tả hàm ===")
describe_function(Calculator.add)


# Ví dụ 3: Ghi log tự động tên hàm và tham số
import functools

def debug_call(func):
    """Decorator ghi log khi gọi hàm, dùng inspect để lấy thông tin."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy thông tin ngăn xếp
        frame = inspect.currentframe()
        try:
            caller_info = inspect.getframeinfo(frame.f_back)
            print(f"[DEBUG] Gọi hàm '{func.__name__}' trong file '{caller_info.filename}', dòng {caller_info.lineno}")
            # In các tham số
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            print(f"  Tham số: {dict(bound_args.arguments)}")
        finally:
            del frame  # Tránh rò rỉ bộ nhớ

        return func(*args, **kwargs)
    return wrapper

@debug_call
def greet(name: str, age: int = 18, city: str = "Hà Nội"):
    print(f"Xin chào {name}, {age} tuổi, đến từ {city}.")

print("\n=== Ví dụ 3: Ghi log tự động ===")
greet("An", 25, "TP.HCM")

greet("Bình")
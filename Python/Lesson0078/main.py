import inspect

class Person:
    """Lớp mô tả một người."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        """Giới thiệu bản thân."""
        print(f"Xin chào, tôi là {self.name}, {self.age} tuổi.")

    def have_birthday(self):
        """Tăng tuổi thêm 1."""
        self.age += 1
        print(f"Chúc mừng sinh nhật! Bạn đã {self.age} tuổi.")


def analyze_function_params(func):
    """In chi tiết các tham số của một hàm."""
    sig = inspect.signature(func)
    print(f"Phân tích hàm: {func.__name__}")
    for name, param in sig.parameters.items():
        type_hint = param.annotation if param.annotation != inspect.Parameter.empty else "Không có"
        default = param.default if param.default != inspect.Parameter.empty else "Không có"
        print(f" - {name}: kiểu={type_hint}, mặc định={default}")


def log_call(func):
    """Decorator: ghi log khi hàm được gọi."""
    def wrapper(*args, **kwargs):
        # Lấy thông tin stack
        frame = inspect.currentframe().f_back
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno

        # Lấy tên tham số
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        args_str = ", ".join(f"{k}={v}" for k, v in bound_args.arguments.items())

        print(f"[LOG] Gọi {func.__name__}({args_str}) tại {filename}:{lineno}")
        return func(*args, **kwargs)
    return wrapper

# Ví dụ 1: In thông tin lớp
print("=== Ví dụ 1: Thông tin lớp Person ===")
members = inspect.getmembers(Person, predicate=inspect.isfunction)
for name, method in members:
    doc = inspect.getdoc(method) or "Không có mô tả"
    print(f"Phương thức: {name} -> {doc}")

# Ví dụ 2: Phân tích tham số hàm
print("\n=== Ví dụ 2: Phân tích tham số ===")
analyze_function_params(Person.__init__)

# Ví dụ 3: Dùng decorator log_call
print("\n=== Ví dụ 3: Ghi log tự động ===")
@log_call
def calculate(a: float, b: float, op: str = "add"):
    if op == "add":
        return a + b
    elif op == "mul":
        return a * b

result = calculate(5, 3, op="mul")
print(f"Kết quả: {result}")
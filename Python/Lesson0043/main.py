import inspect

def hello(name: str, age: int = 20):
    """Chào một người"""
    print(f"Xin chào {name}, {age} tuổi.")

def greet_many(*names, greeting: str = "Chào"):
    """In ra lời chào cho nhiều người"""
    for name in names:
        print(f"{greeting} {name}!")

class Calculator:
    """Máy tính đơn giản"""

    def add(self, a: float, b: float) -> float:
        """Cộng hai số"""
        return a + b

    def multiply(self, x: float, y: float) -> float:
        """Nhân hai số"""
        return x * y

# Ví dụ 1: Trích xuất thông tin hàm để validate tham số
print("=== Ví dụ 1: Kiểm tra chữ ký hàm ===")
sig = inspect.signature(hello)
for name, param in sig.parameters.items():
    default = param.default if param.default != inspect.Parameter.empty else "Không có"
    annotation = param.annotation if param.annotation != inspect.Parameter.empty else "Không xác định"
    print(f"Tham số: {name}, Kiểu: {annotation}, Mặc định: {default}")

# Ví dụ 2: In mã nguồn của các hàm trong module
def print_function_sources(module):
    """In mã nguồn của tất cả các hàm trong một module"""
    print("\n=== Ví dụ 2: Mã nguồn các hàm ===")
    functions = inspect.getmembers(module, inspect.isfunction)
    for name, func in functions:
        try:
            source = inspect.getsource(func)
            print(f"\n--- Hàm: {name} ---\n{source}")
        except Exception as e:
            print(f"Không thể lấy mã nguồn của {name}: {e}")

# Gọi hàm in mã nguồn
print_function_sources(__name__)

# Ví dụ 3: Tự động ghi log phương thức lớp
import functools
import time

def log_calls(func):
    """Decorator ghi log chi tiết khi hàm được gọi"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy thông tin hàm
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[LOG] Hàm '{func.__name__}' được gọi với: {dict(bound_args.arguments)}")
        
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        
        print(f"[LOG] Kết quả: {result} (Thời gian: {duration:.4f}s)")
        return result
    return wrapper

class MathOperations:
    @log_calls
    def power(self, base: float, exp: int = 2):
        """Tính lũy thừa"""
        return base ** exp

    @log_calls
    def divide(self, a: float, b: float):
        """Chia hai số"""
        if b == 0:
            raise ValueError("Không thể chia cho 0")
        return a / b

print("\n=== Ví dụ 3: Ghi log phương thức ===")
math = MathOperations()
math.power(5, 3)
math.divide(10, 2)

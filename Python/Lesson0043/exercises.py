import inspect

def hello(name: str, age: int = 20):
    """Chào một người"""
    print(f"Xin chào {name}, {age} tuổi.")

def greet_many(*names, greeting: str = "Chào"):
    pass

class Calculator:
    """Máy tính đơn giản"""

    def add(self, a: float, b: float) -> float:
        """Cộng hai số"""
        return a + b

    def multiply(self, x: float, y: float) -> float:
        """Nhân hai số"""
        return x * y

# Bài tập 1: Liệt kê các hàm trong một module và số tham số
# Viết hàm list_functions(module) in ra tên hàm và số lượng tham số

def list_functions(module):
    # TODO: Viết mã ở đây
    pass

# Bài tập 2: Viết decorator @log_calls ghi log khi gọi hàm
# Gợi ý: Dùng inspect.signature và bind để lấy danh sách tham số

def log_calls(func):
    # TODO: Viết mã ở đây
    pass

# Bài tập 3: Lấy danh sách phương thức của lớp kèm docstring
# Viết hàm get_class_methods(cls) trả về list các dict {name, doc}

def get_class_methods(cls):
    # TODO: Viết mã ở đây
    pass

# Bài tập 4: Kiểm tra kiểu dữ liệu theo annotation
# Viết hàm validate_annotations(func, *args, **kwargs)
# Trả về True nếu tất cả tham số khớp với annotation, False nếu không
# Gợi ý: Dùng inspect.signature và bind

def validate_annotations(func, *args, **kwargs):
    # TODO: Viết mã ở đây
    pass

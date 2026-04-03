import inspect

def example_function(a: int, b: str = "hello", *args, **kwargs) -> bool:
    """
    Hàm ví dụ để minh họa việc lấy thông tin bằng inspect.
    
    Args:
        a (int): Số nguyên bắt buộc.
        b (str): Chuỗi tùy chọn, mặc định là "hello".
        *args: Các giá trị bổ sung.
        **kwargs: Các cặp key-value bổ sung.

    Returns:
        bool: Luôn trả về True.
    """
    return True

class ExampleClass:
    class_var = "Tôi là biến lớp"

    def __init__(self, value):
        self.value = value

    def method_a(self):
        pass

    def method_b(self, x: float) -> float:
        return x * 2

# Ví dụ 1: In thông tin chi tiết về hàm
def print_function_info(func):
    print(f"Tên hàm: {func.__name__}")
    print(f"Docstring: {inspect.getdoc(func)}")
    
    # Lấy signature
    sig = inspect.signature(func)
    print(f"Signature: {sig}")
    
    for name, param in sig.parameters.items():
        print(f"  Tham số: {name}")
        print(f"    Kiểu: {param.annotation if param.annotation != inspect.Parameter.empty else 'Không xác định'}")
        print(f"    Mặc định: {param.default if param.default != inspect.Parameter.empty else 'Không có'}")
        print(f"    Kiểu tham số: {param.kind}")

print("=== VÍ DỤ 1: Thông tin hàm ===")
print_function_info(example_function)

# Ví dụ 2: Tự động phát hiện và chạy các hàm test
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

def normal_function():
    pass

def run_tests():
    # Lấy tất cả thành viên trong module hiện tại
    members = inspect.getmembers(globals()['__builtins__'], inspect.isfunction)
    members = inspect.getmembers(globals(), inspect.isfunction)
    
    test_functions = [name for name, func in members if name.startswith('test_')]
    
    print("\n=== VÍ DỤ 2: Chạy các test ===")
    for name in test_functions:
        func = globals()[name]
        try:
            func()
            print(f"✅ {name} passed")
        except Exception as e:
            print(f"❌ {name} failed: {e}")

run_tests()

# Ví dụ 3: Ghi log ai đã gọi hàm
def who_called_me():
    stack = inspect.stack()
    # stack[0] là hàm hiện tại, stack[1] là nơi gọi
    caller_frame = stack[1]
    caller_name = caller_frame.function
    caller_line = caller_frame.lineno
    filename = caller_frame.filename
    print(f"Hàm này được gọi từ {caller_name} trong file {filename} tại dòng {caller_line}")

def some_function():
    who_called_me()

def another_function():
    some_function()

print("\n=== VÍ DỤ 3: Xác định nơi gọi ===")
another_function()
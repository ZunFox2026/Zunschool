import inspect

class Calculator:
    """Một lớp mô phỏng máy tính đơn giản"""
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def multiply(self, x: float, y: float) -> float:
        result = x * y
        self.history.append(f"{x} * {y} = {result}")
        return result

    def _private_method(self):
        pass

    def __internal(self):
        pass


def example_1_auto_type_check():
    """Ví dụ 1: Tạo decorator kiểm tra kiểu tham số tự động"""
    from functools import wraps

    def type_check(func):
        sig = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Kết hợp args và kwargs thành binding đầy đủ
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # Kiểm tra từng tham số
            for name, value in bound_args.arguments.items():
                param = sig.parameters[name]
                if param.annotation != inspect.Parameter.empty:
                    expected_type = param.annotation
                    # Hỗ trợ Union type như Optional[int] = Union[int, None]
                    if hasattr(expected_type, '__origin__') and expected_type.__origin__ == Union:
                        types = expected_type.__args__
                    else:
                        types = (expected_type,)

                    # Kiểm tra kiểu
                    if not any(isinstance(value, t) for t in types if t is not type(None)):
                        if value is None and type(None) in types:
                            continue
                        raise TypeError(f"Tham số '{name}' cần kiểu {expected_type}, nhận được {type(value)}")
            return func(*args, **kwargs)

        return wrapper

    @type_check
    def greet(name: str, age: int, scores: list = None):
        print(f"Xin chào {name}, bạn {age} tuổi.")

    print("Ví dụ 1: Kiểm tra kiểu tự động")
    greet("An", 25)  # OK
    try:
        greet("An", "25")  # Lỗi
    except TypeError as e:
        print(f"Lỗi: {e}")


def example_2_list_public_methods():
    """Ví dụ 2: In ra tất cả phương thức public của một lớp"""
    print("\nVí dụ 2: Liệt kê phương thức public")
    calc = Calculator()
    methods = inspect.getmembers(calc, predicate=inspect.ismethod)
    for name, method in methods:
        if not name.startswith('_'):
            print(f"- {name}")


def example_3_debug_call_log():
    """Ví dụ 3: Ghi log tên hàm và tham số khi gọi"""
    def log_call(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Lấy thông tin frame hiện tại
            frame = inspect.currentframe()
            try:
                caller_frame = frame.f_back
                filename = caller_frame.f_code.co_filename
                lineno = caller_frame.f_lineno
            finally:
                del frame

            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)

            print(f"[LOG] Gọi {func.__name__}({signature}) tại {filename}:{lineno}")
            return func(*args, **kwargs)

        return wrapper

    @log_call
    def divide(a, b):
        return a / b

    print("\nVí dụ 3: Ghi log gọi hàm")
    result = divide(10, 2)
    print(f"Kết quả: {result}")


if __name__ == "__main__":
    example_1_auto_type_check()
    example_2_list_public_methods()
    example_3_debug_call_log()

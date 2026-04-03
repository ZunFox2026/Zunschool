import inspect
import functools

def list_public_methods(cls):
    """Bài 1: Liệt kê các phương thức công khai của lớp."""
    # Lấy tất cả thành viên là hàm
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    public_names = []
    for name, method in methods:
        if not name.startswith('_'):
            public_names.append(name)
    return public_names


def get_function_defaults(func):
    """Bài 2: Trả về từ điển tên tham số và giá trị mặc định."""
    sig = inspect.signature(func)
    defaults = {}
    for name, param in sig.parameters.items():
        if param.default != inspect.Parameter.empty:
            defaults[name] = param.default
    return defaults


def debug_caller():
    """Bài 3: In ra tên hàm gọi nó và tên file thực thi."""
    # inspect.stack() trả về danh sách các frame, phần tử [1] là hàm gọi hiện tại
    stack = inspect.stack()
    caller_frame = stack[1]  # Frame của hàm gọi debug_caller
    print(f"Hàm gọi: {caller_frame.function}")
    print(f"File: {caller_frame.filename}")


def print_class_source(cls):
    """Bài 4: In ra mã nguồn của lớp nếu có thể."""
    try:
        source = inspect.getsource(cls)
        print(source)
    except OSError as e:
        print(f"Không thể lấy mã nguồn: {e}")


def log_call(func):
    """Bài 5: Decorator in tên hàm và tham số khi gọi."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy chữ ký hàm để gán tham số
        sig = inspect.signature(func)
        try:
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            args_str = ", ".join(f"{k}={v}" for k, v in bound_args.arguments.items())
        except TypeError as e:
            args_str = "(lỗi khi bind tham số)"

        print(f"[LOG] Gọi hàm '{func.__name__}' với tham số: {args_str}")
        return func(*args, **kwargs)
    return wrapper
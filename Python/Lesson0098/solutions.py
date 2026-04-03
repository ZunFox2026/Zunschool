import inspect

def print_class_info(cls):
    """Bài 1: In ra tất cả phương thức và thuộc tính của một lớp."""
    print(f"Thông tin về lớp: {cls.__name__}")
    print("- Các phương thức:")
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        print(f"  + {name}")
    print("- Các thuộc tính (không phải hàm):")
    for name, attr in inspect.getmembers(cls):
        if not (inspect.isfunction(attr) or name.startswith("__")):
            print(f"  + {name}")


def debug_calls(func):
    """Bài 2: Decorator in ra tên hàm, tham số và giá trị trả về."""
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[CALL] Hàm: {func.__name__}")
        print(f"       Tham số: {dict(bound_args.arguments)}")
        
        result = func(*args, **kwargs)
        
        print(f"       Trả về: {result}")
        return result
    return wrapper


def get_caller_info():
    """Bài 3: In ra tên hàm gọi nó và tên file."""
    frame = inspect.currentframe().f_back  # Frame của hàm gọi
    filename = frame.f_code.co_filename
    func_name = frame.f_code.co_name
    print(f"Hàm '{func_name}' trong file '{filename}' đã gọi get_caller_info().")


def require_kwargs_only(func):
    """Bài 4: Decorator yêu cầu tất cả tham số phải là keyword arguments."""
    def wrapper(*args, **kwargs):
        if args:
            raise TypeError(f"Hàm {func.__name__} chỉ nhận keyword arguments.")
        return func(*args, **kwargs)
    return wrapper


def list_functions_in_module(module):
    """Bài 5: Liệt kê tất cả hàm trong module cùng số lượng tham số."""
    print(f"Các hàm trong module {module.__name__}:")
    for name, func in inspect.getmembers(module, inspect.isfunction):
        sig = inspect.signature(func)
        params_count = len(sig.parameters)
        print(f"- {name}: {params_count} tham số")
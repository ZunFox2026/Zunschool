import inspect
import time
from functools import wraps

# Bài tập 1: Viết hàm in ra thông tin hàm gọi nó
def print_caller_info():
    # inspect.stack()[1] là frame của hàm gọi hàm hiện tại
    caller_frame = inspect.stack()[1]
    print(f"Hàm \"{caller_frame.function}\" gọi tại dòng {caller_frame.lineno} của file {caller_frame.filename}")

# Bài tập 2: Liệt kê các phương thức công khai của lớp
def list_public_methods(cls):
    # Dùng getmembers để lấy tất cả thành viên, lọc ra hàm và không bắt đầu bằng _
    methods = []
    for name, obj in inspect.getmembers(cls, predicate=inspect.isfunction):
        if not name.startswith("_"):
            methods.append(name)
    return methods

# Bài tập 3: Decorator ghi log thời gian thực thi
def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        
        # Lấy tên hàm gọi từ stack nếu cần, nhưng ở đây dùng __name__ cũng được
        print(f"[LOG] Hàm '{func.__name__}' thực thi mất {end - start:.4f} giây")
        return result
    return wrapper

# Bài tập 4: Kiểm tra kiểu tham số dựa trên annotation
def validate_annotations(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        for param_name, value in bound_args.arguments.items():
            param = sig.parameters[param_name]
            if param.annotation != inspect.Parameter.empty:
                expected_type = param.annotation
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Tham số '{param_name}' cần là {expected_type}, "
                        f"nhưng nhận {type(value)}"
                    )
        return func(*args, **kwargs)
    return wrapper

# Bài tập 5: Lấy mã nguồn nếu có thể
def get_function_source_if_possible(func):
    try:
        source = inspect.getsource(func)
        return source
    except OSError:
        return "Không thể lấy mã nguồn (hàm built-in hoặc không có mã nguồn)"
    except Exception as e:
        return f"Lỗi không xác định: {e}"
import inspect
import time
from functools import wraps

# Bài tập 1: Viết hàm in ra thông tin hàm gọi nó
def print_caller_info():
    # Gợi ý: dùng inspect.stack()
    pass

# Bài tập 2: Liệt kê các phương thức công khai của lớp
def list_public_methods(cls):
    # Gợi ý: dùng inspect.getmembers() và kiểm tra isfunction
    pass

# Bài tập 3: Decorator ghi log thời gian thực thi
def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Gợi ý: dùng time.time() và inspect.stack()
        pass
    return wrapper

# Bài tập 4: Kiểm tra kiểu tham số dựa trên annotation
def validate_annotations(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Gợi ý: dùng inspect.signature() và isinstance()
        pass
    return wrapper

# Bài tập 5: Lấy mã nguồn nếu có thể
def get_function_source_if_possible(func):
    # Gợi ý: dùng inspect.getsource(), xử lý ngoại lệ
    pass
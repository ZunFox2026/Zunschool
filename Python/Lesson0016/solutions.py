import functools
import time

############## Bài tập 1 ##############
# Viết decorator @log_calls để in ra tên hàm và các tham số khi gọi

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Gọi hàm {func.__name__} với args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

############## Bài tập 2 ##############
# Viết decorator @retry để thử lại hàm nếu gặp lỗi, tối đa 3 lần

def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(3):  # Thử tối đa 3 lần
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Lỗi khi gọi {func.__name__}: {e}. Thử lại lần {i+1}")
                if i == 2:  # Lần cuối cùng
                    raise
    return wrapper

############## Bài tập 3 ##############
# Viết decorator @memoize để lưu kết quả hàm, tránh tính toán lại

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Tạo key từ args và kwargs (chỉ dùng khi tham số là immutable)
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

############## Bài tập 4 ##############
# Viết decorator @timing có thể dùng cho hàm có tham số

def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Hàm '{func.__name__}' thực thi trong {end - start:.4f} giây")
        return result
    return wrapper

############## Bài tập 5 ##############
# Viết decorator @ensure_positive kiểm tra tất cả tham số là số dương

def ensure_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Kiểm tra các tham số trong args
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                print(f"Lỗi: Tham số {arg} không phải số dương")
                return None
        # Kiểm tra các tham số trong kwargs
        for k, v in kwargs.items():
            if isinstance(v, (int, float)) and v <= 0:
                print(f"Lỗi: Tham số {k}={v} không phải số dương")
                return None
        return func(*args, **kwargs)
    return wrapper
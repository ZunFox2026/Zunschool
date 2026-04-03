from typing import Any, Callable, get_type_hints
import inspect
import functools

# Bài tập 1: Viết decorator @log_calls
# Ghi log tên hàm và tất cả tham số (args và kwargs)
# TODO: Viết decorator tại đây

def log_calls(func):
    # TODO: Hoàn thiện decorator
    pass


# Bài tập 2: In mã nguồn các hàm trong một module
# Viết hàm in mã nguồn của mọi hàm trong module được truyền vào
# TODO: Hoàn thiện hàm

def print_function_sources(module):
    # TODO: Duyệt qua các hàm và in mã nguồn
    pass


# Bài tập 3: Phân tích tham số hàm
# In chi tiết: tên, kiểu (nếu có), giá trị mặc định
# TODO: Hoàn thiện hàm

def analyze_function_params(func):
    # TODO: Sử dụng inspect.signature và get_type_hints
    pass


# Bài tập 4: In ra tên hàm đã gọi hàm hiện tại
# TODO: Viết hàm who_called_me()

def who_called_me():
    # TODO: Dùng inspect.stack() để lấy frame gọi
    pass


def caller_function():
    who_called_me()


# Bài tập 5: Decorator kiểm tra kiểu tham số
# Kiểm tra type hints và cảnh báo nếu kiểu không khớp
# TODO: Viết decorator @validate_types

def validate_types(func):
    # TODO: Dùng get_type_hints và isinstance để kiểm tra
    pass

@validate_types
def add_numbers(a: int, b: int) -> int:
    return a + b
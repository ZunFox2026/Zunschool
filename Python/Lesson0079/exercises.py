import inspect
import functools

# Bài tập 1: Viết decorator @log_calls ghi log tên hàm và các tham số khi được gọi.
# Gợi ý: Dùng inspect.signature và bind
# def log_calls(func):
#     ...

# Bài tập 2: Viết hàm describe_function(func) in ra mô tả chi tiết về một hàm
# In tên, docstring, các tham số với kiểu và giá trị mặc định
# def describe_function(func):
#     ...

# Bài tập 3: Viết decorator @type_check kiểm tra kiểu dữ liệu của tham số truyền vào
# Dựa trên type hint. Nếu kiểu không khớp, in cảnh báo (không chặn)
# def type_check(func):
#     ...

# Bài tập 4: Viết hàm find_functions_in_module(module, min_params=2)
# Tìm tất cả hàm trong module có ít nhất min_params tham số
# Trả về danh sách tên hàm
# def find_functions_in_module(module, min_params=2):
#     ...

# Bài tập 5: Viết hàm print_call_stack()
# In ra danh sách các hàm đang được gọi (tên hàm và file) từ điểm hiện tại
# Dùng inspect.stack()
# def print_call_stack():
#     ...

import inspect

# Bài tập 1: Viết hàm in ra tất cả các phương thức public của một lớp
# Input: một lớp
# Output: in ra danh sách tên phương thức (không bao gồm phương thức riêng tư bắt đầu bằng _)
def print_public_methods(cls):
    # TODO: Hoàn thành hàm
    pass

# Bài tập 2: Viết hàm kiểm tra một hàm có tham số bắt buộc nào không
# Input: một hàm
# Output: True nếu có ít nhất một tham số bắt buộc (không có giá trị mặc định), ngược lại False
def has_required_params(func):
    # TODO: Hoàn thành hàm
    pass

# Bài tập 3: Viết decorator ghi log thời gian gọi hàm và ai gọi hàm đó
# Yêu cầu in ra: tên hàm, thời gian gọi, tên hàm gọi nó (caller)
def log_call(func):
    # TODO: Hoàn thành decorator
    pass

# Bài tập 4: Viết hàm lấy danh sách các lớp con trực tiếp của một lớp cha trong một mô-đun
# Input: lớp cha và mô-đun (module)
# Output: danh sách các lớp con
def get_direct_subclasses(parent_class, module):
    # TODO: Hoàn thành hàm
    pass

# Bài tập 5: Viết hàm kiểm tra xem một hàm có dùng biến toàn cục (global) không
# Input: hàm
# Output: True nếu có dùng biến global, ngược lại False
def uses_global_variables(func):
    # TODO: Hoàn thành hàm
    pass
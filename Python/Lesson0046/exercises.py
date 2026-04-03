# Bài tập 1: Viết hàm ghi log tự động
# Viết hàm `log_call(func)` nhận một hàm và in ra:
# - Tên hàm
# - Các tham số được truyền vào (tên và giá trị)
# - Giá trị trả về
# Gợi ý: dùng inspect.signature và *args, **kwargs

def exercise_1():
    pass

# Bài tập 2: Kiểm tra tính toàn vẹn của lớp
# Viết hàm `validate_class(cls)` kiểm tra rằng:
# - Lớp có __init__
# - Tất cả phương thức public (không bắt đầu bằng _) có docstring
# - Trả về danh sách các lỗi (nếu có)

def exercise_2():
    pass

# Bài tập 3: Trích xuất thông tin từ module
# Viết hàm `analyze_module(module)` nhận một module (như math, os, ...)
# và in ra:
# - Danh sách các hàm
# - Danh sách các lớp
# - Danh sách các hằng số (giá trị không phải hàm/lớp)
# Gợi ý: dùng inspect.isfunction, inspect.isclass

def exercise_3():
    pass

# Bài tập 4: Tạo factory tự động
# Viết hàm `create_instance_by_name(class_name, *args, **kwargs)`
# Tìm lớp trong module hiện tại có tên `class_name` và tạo instance
# Nếu không tìm thấy, trả về None
# Gợi ý: dùng globals() và inspect.isclass

def exercise_4():
    pass

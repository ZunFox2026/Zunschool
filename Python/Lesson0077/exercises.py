###################
# Bài tập thực hành - Bài 77
# File: exercises.py
# Chứa các bài tập chưa có lời giải
###################

# Bài 1: Viết một descriptor EmailDescriptor kiểm tra định dạng email đơn giản
# (có @ và ., không bắt đầu hoặc kết thúc bằng @)

class EmailDescriptor:
    # TODO: Viết phương thức __get__, __set__, __delete__
    pass

class Person:
    email = EmailDescriptor()
    def __init__(self, email):
        self.email = email


# Bài 2: Viết descriptor LimitedAccessDescriptor chỉ cho phép truy cập tối đa N lần

class LimitedAccessDescriptor:
    # TODO: Triển khai
    pass

class SecretData:
    secret = LimitedAccessDescriptor(max_access=3)
    def __init__(self, value):
        self.secret = value


# Bài 3: Viết descriptor ReadOnlyDescriptor để tạo thuộc tính chỉ đọc

class ReadOnlyDescriptor:
    # TODO: Triển khai
    pass

class Configuration:
    api_key = ReadOnlyDescriptor("abc123")
    def __init__(self):
        pass


# Bài 4: Viết descriptor TimeTrackerDescriptor ghi lại thời gian truy cập cuối cùng

class TimeTrackerDescriptor:
    # TODO: Sử dụng time.time() để lưu thời gian truy cập
    pass

class TrackedValue:
    value = TimeTrackerDescriptor()
    def __init__(self, val):
        self.value = val


# Bài 5: Viết descriptor TypeEnforcedDescriptor buộc kiểu dữ liệu

class TypeEnforcedDescriptor:
    # TODO: Chỉ cho phép gán giá trị đúng kiểu đã khai báo
    pass

class DataRecord:
    name = TypeEnforcedDescriptor(str)
    age = TypeEnforcedDescriptor(int)
    def __init__(self, name, age):
        self.name = name
        self.age = age

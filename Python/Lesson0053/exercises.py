import inspect

# Bài 1: In thông tin các phương thức của lớp
def print_class_info(cls):
    """In tên và tham số của tất cả phương thức trong lớp"""
    # TODO: Viết mã ở đây
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self, greeting="Xin chào"):
        return f"{greeting}, tôi là {self.name}"

    def have_birthday(self):
        self.age += 1

# Bài 2: Decorator ghi log vào file
def log_calls(func):
    """Decorator ghi tên hàm, tham số, kết quả vào file debug.log"""
    # TODO: Viết mã ở đây
    pass

# Bài 3: Tìm các hàm không có docstring
def find_functions_without_docstring(module):
    """Trả về danh sách tên các hàm trong module không có docstring"""
    # TODO: Viết mã ở đây
    pass

# Bài 4: In ra tên hàm đã gọi hàm hiện tại
def who_called_me():
    """In ra tên hàm đã gọi hàm này"""
    # TODO: Viết mã ở đây
    pass

def caller():
    who_called_me()

# Gọi các hàm để kiểm tra (không sửa phần này)
if __name__ == "__main__":
    print_class_info(Person)
    
    @log_calls
    def test_func(x, y=10):
        return x * y
    
    test_func(5, y=3)
    
    print("Hàm không có docstring:", find_functions_without_docstring(__name__))
    
    caller()
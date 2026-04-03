import inspect

def exercise1():
    """
    Bài tập 1: Viết hàm nhận vào một đối tượng và in ra tất cả các phương thức 
    công khai (không bắt đầu bằng '_') cùng với docstring của chúng.
    """
    # Gợi ý: Dùng inspect.getmembers và lọc theo tên
    pass

class MathUtils:
    """Công cụ toán học đơn giản"""
    
    def square(self, x):
        """Trả về bình phương của x"""
        return x ** 2
    
    def _private_helper(self):
        """Hàm helper không công khai"""
        return "private"
    
    def cube(self, x):
        """Trả về lập phương của x"""
        return x ** 3


def exercise2(obj):
    """
    Bài tập 2: Viết hàm kiểm tra một phương thức của đối tượng có tham số cụ thể không.
    Ví dụ: Kiểm tra phương thức 'square' có tham số 'x' không.
    """
    # Gợi ý: Dùng inspect.signature và kiểm tra trong .parameters
    pass


def exercise3(frame_depth=1):
    """
    Bài tập 3: Viết hàm in ra chuỗi gọi hàm (call stack) từ hiện tại trở lên.
    In ra tên hàm, file, và số dòng.
    """
    # Gợi ý: Dùng inspect.stack()
    pass

def outer():
    middle()

def middle():
    inner()

def inner():
    exercise3(frame_depth=3)

# Gọi để kiểm tra
# inner()
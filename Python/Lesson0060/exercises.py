import inspect

def hello(name, age=20):
    """Chào một người."""
    return f"Xin chào {name}, {age} tuổi."

def greet_all(*names):
    """Chào tất cả mọi người."""
    return " và ".join([f"Xin chào {n}" for n in names])

class User:
    def __init__(self, username, email=""):
        self.username = username
        self.email = email

    def info(self):
        return f"User: {self.username}, Email: {self.email}"

    def change_email(self, new_email):
        self.email = new_email

# Bài tập 1: Liệt kê các hàm trong một module cùng docstring
def list_functions(module):
    """In ra danh sách các hàm trong module cùng với docstring.
    
    Gợi ý: Dùng inspect.getmembers() và inspect.isfunction()
    """
    pass

# Bài tập 2: Viết decorator @log_call ghi log khi gọi hàm
def log_call(func):
    """Decorator ghi log tên hàm và tham số khi gọi.
    
    Gợi ý: Dùng inspect.signature để lấy tham số và giá trị thực tế.
    """
    pass

# Bài tập 3: Phân tích một lớp, in ra các phương thức và thuộc tính
def analyze_class(cls):
    """In ra tất cả phương thức và thuộc tính của một lớp.
    
    Gợi ý: Dùng inspect.getmembers(), lọc theo isfunction hoặc isroutine.
    """
    pass

# Bài tập 4: Tìm các hàm có tham số mặc định
def find_functions_with_defaults(module):
    """Trả về danh sách tên các hàm trong module có tham số có giá trị mặc định.
    
    Gợi ý: Dùng inspect.signature và kiểm tra param.default != inspect.Parameter.empty
    """
    pass

# Bài tập 5: In thông tin về hàm gọi nó
def print_caller_info():
    """In ra tên hàm gọi nó, tên file và số dòng.
    
    Gợi ý: Dùng inspect.stack()[1]
    """
    pass
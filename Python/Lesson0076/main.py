import inspect

def hello(name: str, age: int = 20):
    """Chào một người với tên và tuổi."""
    print(f"Xin chào {name}, bạn {age} tuổi.")

def greet_multiple(*names: str, greeting: str = "Chào"):
    """Chào nhiều người với lời chào tùy chọn."""
    for name in names:
        print(f"{greeting} {name}!")

class Calculator:
    """Máy tính đơn giản với một số phép toán cơ bản."""

    def __init__(self, precision: int = 2):
        self.precision = precision

    def add(self, a: float, b: float) -> float:
        """Cộng hai số."""
        return round(a + b, self.precision)

    def multiply(self, x: float, y: float) -> float:
        """Nhân hai số."""
        return round(x * y, self.precision)

    def _private_helper(self):
        pass  # Hàm riêng tư

# Ví dụ 1: Trình ghi log tự động tham số hàm
def log_args(func):
    """Decorator ghi log các tham số khi gọi hàm."""
    def wrapper(*args, **kwargs):
        # Lấy thông tin hàm
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[LOG] Gọi hàm '{func.__name__}' với tham số:")
        for name, value in bound_args.arguments.items():
            print(f"  {name} = {value}")
        
        result = func(*args, **kwargs)
        print(f"[LOG] Kết quả: {result}\n")
        return result
    return wrapper

@log_args
def calculate_area(length, width=1):
    return length * width

# Ví dụ 2: In mã nguồn và phương thức của lớp
def show_class_info(cls):
    """In thông tin về một lớp: docstring, mã nguồn, danh sách phương thức."""
    print(f"=== Thông tin về lớp {cls.__name__} ===")
    
    # Docstring
    doc = inspect.getdoc(cls)
    if doc:
        print(f"Docstring: {doc}")
    else:
        print("Không có docstring.")
    
    # Mã nguồn (nếu có)
    try:
        source = inspect.getsource(cls)
        print("\nMã nguồn:")
        print(source)
    except OSError:
        print("\nKhông thể lấy mã nguồn (có thể là built-in hoặc C extension).")
    
    # Liệt kê các phương thức công khai
    print("\nPhương thức công khai:")
    methods = [name for name, obj in inspect.getmembers(cls, predicate=inspect.isfunction)
               if not name.startswith("_")]
    for method in methods:
        print(f"  - {method}")

# Ví dụ 3: Framework tự động đăng ký hàm xử lý
def register_handler(name):
    """Decorator để đăng ký hàm xử lý."""
    def decorator(func):
        if not hasattr(register_handler, 'handlers'):
            register_handler.handlers = {}
        register_handler.handlers[name] = func
        return func
    return decorator

@register_handler('greet')
def handle_greet(name: str):
    return f"Xin chào {name}!"

@register_handler('add')
def handle_add(a: int, b: int):
    return a + b

# Hàm xử lý lệnh
def process_command(command: str, *args):
    handlers = getattr(register_handler, 'handlers', {})
    if command not in handlers:
        return "Lệnh không tồn tại."
    
    func = handlers[command]
    sig = inspect.signature(func)
    try:
        # Kiểm tra số lượng tham số
        bound = sig.bind(*args)
        bound.apply_defaults()
        return func(*bound.args)
    except TypeError as e:
        return f"Lỗi tham số: {e}"

# Chạy ví dụ minh họa
def main():
    print("=== Ví dụ 1: Ghi log tham số ===")
    calculate_area(5, 3)
    calculate_area(4)
    
    print("=== Ví dụ 2: Thông tin lớp Calculator ===")
    show_class_info(Calculator)
    
    print("=== Ví dụ 3: Framework xử lý lệnh ===")
    print(process_command('greet', 'An'))
    print(process_command('add', 5, 7))
    print(process_command('unknown'))

if __name__ == "__main__":
    main()
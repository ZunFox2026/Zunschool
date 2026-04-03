import inspect

def hello(name, age=20, city="Hà Nội"):
    """Chào một người với tên, tuổi và thành phố."""
    return f"Xin chào {name}, bạn {age} tuổi, đến từ {city}."

def greet_multiple(*names):
    """Chào nhiều người một lúc."""
    return ", ".join([f"Xin chào {name}" for name in names])

class Calculator:
    """Máy tính đơn giản hỗ trợ các phép tính cơ bản."""

    def __init__(self, precision=2):
        self.precision = precision

    def add(self, a, b):
        return round(a + b, self.precision)

    def multiply(self, a, b):
        return round(a * b, self.precision)

# —————————— Ví dụ 1: Tự động tạo tài liệu cho các hàm trong module ——————————
def generate_function_docs(module):
    """In ra tài liệu cho tất cả các hàm trong module."""
    print("=== Tài liệu các hàm trong module ===\n")
    functions = inspect.getmembers(module, inspect.isfunction)
    
    for name, func in functions:
        sig = inspect.signature(func)
        doc = inspect.getdoc(func) or "Không có mô tả."
        print(f"Hàm: {name}{sig}")
        print(f"  Mô tả: {doc}\n")

# Gọi ví dụ 1
generate_function_docs(__name__)

# —————————— Ví dụ 2: Ghi log tự động tên hàm và tham số ——————————
def log_function_call():
    """In ra thông tin về hàm gọi nó."""
    frame = inspect.currentframe().f_back  # Lấy frame gọi hàm hiện tại
    func_name = frame.f_code.co_name
    filename = frame.f_code.co_filename
    line_no = frame.f_lineno
    
    args = inspect.getargvalues(frame)
    print(f"[LOG] Hàm '{func_name}' được gọi từ {filename}:{line_no}")
    if args.args:
        for arg in args.args:
            value = args.locals[arg]
            print(f"      Tham số {arg} = {value}")

# Thử nghiệm log
def test_logging():
    x = 10
    y = 20
    log_function_call()

test_logging()

# —————————— Ví dụ 3: In mã nguồn của một lớp ——————————
try:
    source = inspect.getsource(Calculator)
    print("\n=== Mã nguồn của lớp Calculator ===\n")
    print(source)
except OSError:
    print("Không thể lấy mã nguồn (có thể do chạy trong REPL hoặc file được compile).")

# In toàn bộ thành viên của lớp
print("\n=== Các thành viên của lớp Calculator ===\n")
members = inspect.getmembers(Calculator, predicate=inspect.isfunction)
for name, method in members:
    sig = inspect.signature(method)
    print(f"Phương thức: {name}{sig}")
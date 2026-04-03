import inspect

def hello(name: str, age: int = 20) -> str:
    """Hàm chào hỏi một người."""
    return f"Xin chào {name}, bạn {age} tuổi."

class Calculator:
    """Một máy tính đơn giản."""
    
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

# Ví dụ 1: Kiểm tra thông tin hàm bằng inspect
print("=== Ví dụ 1: Thông tin hàm hello ===")
sig = inspect.signature(hello)
print(f"Chữ ký hàm: {sig}")
for name, param in sig.parameters.items():
    print(f"Tham số: {name}, kiểu: {param.annotation}, mặc định: {param.default}")

# Ví dụ 2: Lấy mã nguồn của hàm và lớp
print("\n=== Ví dụ 2: Lấy mã nguồn ===")
try:
    source = inspect.getsource(hello)
    print("Mã nguồn hàm hello:")
    print(source)
except OSError:
    print("Không thể lấy mã nguồn (có thể do chạy trong môi trường REPL)")

# Ví dụ 3: Kiểm tra các thành viên của lớp
print("\n=== Ví dụ 3: Kiểm tra thành viên lớp Calculator ===")
methods = inspect.getmembers(Calculator, predicate=inspect.isfunction)
print("Các phương thức trong Calculator:")
for name, method in methods:
    print(f"- {name}: {method.__doc__}")

# Ví dụ 4: Ghi log tự động tên hàm đang gọi
def debug_call():
    frame = inspect.currentframe().f_back  # Frame trước đó (người gọi)
    func_name = frame.f_code.co_name
    filename = frame.f_code.co_filename
    line_no = frame.f_lineno
    print(f"[DEBUG] Hàm '{func_name}' được gọi từ file '{filename}', dòng {line_no}")

def my_task():
    debug_call()
    return "Thực hiện xong task"

print("\n=== Ví dụ 4: Ghi log vị trí gọi hàm ===")
my_task()

# Ví dụ 5: Tự động đăng ký các hàm trong module
def register_functions(prefix=""):
    frame = inspect.currentframe().f_back
    module_vars = frame.f_locals
    functions = {}
    for name, obj in module_vars.items():
        if inspect.isfunction(obj) and name.startswith(prefix):
            functions[name] = obj
    return functions

def action_save():
    return "Đã lưu"

def action_delete():
    return "Đã xóa"

print("\n=== Ví dụ 5: Tự động đăng ký hàm theo tiền tố ===")
actions = register_functions("action_")
for name, func in actions.items():
    print(f"{name} -> {func()}")
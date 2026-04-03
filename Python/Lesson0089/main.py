import inspect
import functools

# ------------------------
# VÍ DỤ 1: Decorator ghi log tham số hàm
# ------------------------

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy signature của hàm để phân tích tham số
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()  # Áp dụng giá trị mặc định

        print(f"[LOG] Gọi hàm '{func.__name__}' với tham số:")
        for name, value in bound_args.arguments.items():
            print(f"  {name} = {value}")

        return func(*args, **kwargs)
    return wrapper

@log_calls
def greet(name, age=25, city='Hà Nội'):
    print(f"Xin chào {name}, {age} tuổi, đến từ {city}!")

# Gọi hàm để xem log
print("=== Ví dụ 1: Ghi log tham số ===")
greet("An", age=30, city="TP.HCM")


# ------------------------
# VÍ DỤ 2: In mã nguồn của các hàm trong module
# ------------------------

def print_function_sources(module):
    """In mã nguồn của tất cả các hàm trong một module."""
    print(f"\n=== Mã nguồn các hàm trong module {module.__name__} ===")
    for name, obj in inspect.getmembers(module, predicate=inspect.isfunction):
        if name.startswith('_'):  # Bỏ qua hàm private
            continue
        try:
            source = inspect.getsource(obj)
            print(f"\n--- Hàm: {name} ---")
            print(source.strip())
        except Exception as e:
            print(f"Không thể lấy mã nguồn của {name}: {e}")

# Gọi ví dụ 2
print_function_sources(__name__)


# ------------------------
# VÍ DỤ 3: Debug call stack khi có lỗi
# ------------------------

def debug_call_stack():
    """In ra thông tin về các hàm đang gọi nhau."""
    print("\n=== Call stack hiện tại ===")
    stack = inspect.stack()
    for frame_info in stack[1:]:  # Bỏ qua chính hàm này
        filename = frame_info.filename.split('/')[-1].split('\\')[-1]
        print(f"  File '{filename}', line {frame_info.lineno}, in {frame_info.function}")


def level1():
    level2()

def level2():
    debug_call_stack()

print("\n=== Ví dụ 3: Debug Call Stack ===")
level1()
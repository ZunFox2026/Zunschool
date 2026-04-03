import inspect

def hello(name: str, age: int = 20):
    """Chào một người"""
    print(f"Xin chào {name}, {age} tuổi.")

def greet_many(*names, greeting: str = "Chào"):
    pass

class Calculator:
    """Máy tính đơn giản"""

    def add(self, a: float, b: float) -> float:
        """Cộng hai số"""
        return a + b

    def multiply(self, x: float, y: float) -> float:
        """Nhân hai số"""
        return x * y

# Bài tập 1: Liệt kê các hàm trong một module và số tham số

def list_functions(module):
    """
    In ra danh sách các hàm trong module cùng số lượng tham số
    """
    print(f"Các hàm trong module {module.__name__}:")
    functions = inspect.getmembers(module, inspect.isfunction)
    for name, func in functions:
        sig = inspect.signature(func)
        num_params = len(sig.parameters)
        print(f"- {name}: {num_params} tham số")

# Bài tập 2: Viết decorator @log_calls ghi log khi gọi hàm

def log_calls(func):
    """
    Decorator ghi log mỗi khi hàm được gọi, hiển thị tên hàm và tham số
    """
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy chữ ký hàm
        sig = inspect.signature(func)
        try:
            # Ghép tham số vào
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()  # Áp dụng giá trị mặc định
            args_dict = dict(bound_args.arguments)
        except Exception as e:
            args_dict = {"error": str(e)}
        
        print(f"[LOG] Gọi hàm '{func.__name__}' với tham số: {args_dict}")
        result = func(*args, **kwargs)
        print(f"[LOG] Hàm '{func.__name__}' trả về: {result}")
        return result
    return wrapper

# Bài tập 3: Lấy danh sách phương thức của lớp kèm docstring

def get_class_methods(cls):
    """
    Trả về danh sách các phương thức của lớp kèm theo docstring
    """
    methods = []
    for name, func in inspect.getmembers(cls, inspect.isfunction):
        doc = inspect.getdoc(func) or "Không có mô tả"
        methods.append({
            "name": name,
            "doc": doc
        })
    return methods

# Bài tập 4: Kiểm tra kiểu dữ liệu theo annotation

def validate_annotations(func, *args, **kwargs):
    """
    Kiểm tra xem các đối số truyền vào có khớp với kiểu trong annotation không.
    Trả về True nếu tất cả đều khớp, ngược lại False.
    Lưu ý: Không kiểm tra sâu (như kiểu trong list), chỉ kiểm tra kiểu cơ bản.
    """
    sig = inspect.signature(func)
    try:
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
    except Exception:
        return False  # Nếu không bind được thì sai

    for param_name, value in bound_args.arguments.items():
        param = sig.parameters[param_name]
        annotation = param.annotation

        # Bỏ qua nếu không có annotation
        if annotation == inspect.Parameter.empty:
            continue

        # Kiểm tra kiểu (chỉ cho kiểu cơ bản)
        if (hasattr(annotation, '__origin__') and annotation.__origin__ is not None):
            # Hỗ trợ kiểu Optional, List, v.v. — bỏ qua ở đây để đơn giản
            continue
        
        if not isinstance(value, annotation):
            return False

    return True

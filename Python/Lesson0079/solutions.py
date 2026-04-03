import inspect
import functools

# Bài tập 1: Viết decorator @log_calls ghi log tên hàm và các tham số khi được gọi.
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy signature để ánh xạ tham số
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()  # Áp dụng giá trị mặc định

        # In log
        print(f"Gọi hàm: {func.__name__}(", end="")
        arg_strs = []
        for name, value in bound_args.arguments.items():
            arg_strs.append(f"{name}={value}")
        print("; ".join(arg_strs) + ")")

        return func(*args, **kwargs)
    return wrapper


# Bài tập 2: Viết hàm describe_function(func) in ra mô tả chi tiết về một hàm
def describe_function(func):
    """
    In mô tả chi tiết về một hàm: tên, docstring, tham số, kiểu, giá trị mặc định.
    """
    print(f"Tên hàm: {func.__name__}")
    print(f"Docstring: {func.__doc__ or 'Không có'}")

    sig = inspect.signature(func)
    params = sig.parameters

    if params:
        print("Các tham số:")
        for name, param in params.items():
            # Kiểu dữ liệu
            annot = param.annotation
            if annot == inspect.Parameter.empty:
                annot_str = "không xác định"
            else:
                annot_str = str(annot)

            # Giá trị mặc định
            default = param.default
            if default == inspect.Parameter.empty:
                default_str = "không có"
            else:
                default_str = repr(default)

            print(f"  - {name}: kiểu={annot_str}, mặc định={default_str}")
    else:
        print("Không có tham số.")

    print("-")


# Bài tập 3: Viết decorator @type_check kiểm tra kiểu dữ liệu của tham số
def type_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        # Kiểm tra từng tham số
        for name, value in bound_args.arguments.items():
            param = sig.parameters[name]
            expected_type = param.annotation

            # Nếu có type hint và không phải empty
            if expected_type != inspect.Parameter.empty:
                # Hỗ trợ Union (typing.Union), nhưng đơn giản: kiểm tra isinstance
                # Nếu là kiểu đơn giản
                if hasattr(expected_type, '__origin__') and expected_type.__origin__ is not None:
                    # Ví dụ: Union[int, str], List[str]...
                    # Không xử lý phức tạp, bỏ qua hoặc cảnh báo chung
                    pass
                else:
                    if not isinstance(value, expected_type):
                        print(f"[CẢNH BÁO] Hàm '{func.__name__}': tham số '{name}'"
                              f" có kiểu {type(value).__name__}, cần {expected_type.__name__}")

        return func(*args, **kwargs)
    return wrapper


# Bài tập 4: Tìm các hàm trong module có ít nhất min_params tham số
def find_functions_in_module(module, min_params=2):
    """
    Tìm tất cả các hàm trong module có ít nhất min_params tham số.
    Trả về danh sách tên hàm.
    """
    functions = []
    # Lấy tất cả thành viên của module
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        try:
            sig = inspect.signature(obj)
            if len(sig.parameters) >= min_params:
                functions.append(name)
        except (ValueError, TypeError):
            # Một số hàm built-in không thể lấy signature
            continue
    return functions


# Bài tập 5: In ra call stack hiện tại
def print_call_stack():
    """
    In ra danh sách các frame trong call stack, từ hiện tại đến gốc.
    Mỗi frame gồm: tên hàm, tên file, số dòng.
    """
    stack = inspect.stack()
    print("Call stack (từ dưới lên gốC):")
    for frame in stack[1:]:  # Bỏ frame hiện tại của print_call_stack
        filename = frame.filename
        lineno = frame.lineno
        function_name = frame.function
        print(f"  File \"{filename}\", line {lineno}, in {function_name}")

# --- Ví dụ kiểm thử lời giải ---
if __name__ == "__main__":
    # Test bài 1
    @log_calls
    def test_func(a, b=10):
        return a + b
    print("\nTest bài 1:")
    test_func(5)

    # Test bài 2
    print("\nTest bài 2:")
    def sample(x: int, y: str = "hello"):
        """Mô tả mẫu"""
        pass
    describe_function(sample)

    # Test bài 3
    print("\nTest bài 3:")
    @type_check
    def func_check(name: str, age: int):
        pass
    func_check("Nguyen", 25)      # OK
    func_check("Nguyen", "25")   # Cảnh báo

    # Test bài 4
    print("\nTest bài 4:")
    import math
    funcs = find_functions_in_module(math, min_params=2)
    print(f"Hàm trong math có >=2 tham số: {funcs[:5]}...")

    # Test bài 5
    print("\nTest bài 5:")
    def level_3():
        print_call_stack()
    def level_2():
        level_3()
    def level_1():
        level_2()
    level_1()
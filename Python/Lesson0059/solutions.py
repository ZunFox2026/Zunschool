import inspect

def print_caller_info():
    # Lấy stack, phần tử [1] là hàm gọi hàm hiện tại
    frame = inspect.stack()[1]
    caller_name = frame.function
    line_number = frame.lineno
    filename = frame.filename
    print(f"Hàm '{caller_name}' đã gọi hàm này tại dòng {line_number} trong file {filename}")

def log_calls(func):
    def wrapper(*args, **kwargs):
        # Lấy thông tin tham số
        sig = inspect.signature(func)
        try:
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            arguments = dict(bound.arguments)
        except TypeError as e:
            arguments = {"args": args, "kwargs": kwargs}
            
        print(f"[DEBUG] Gọi {func.__name__} với: {arguments}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] {func.__name__} trả về: {result}")
        return result
    return wrapper

def explore_module(module):
    # Lấy tất cả thành viên của module
    members = inspect.getmembers(module, predicate=lambda x: (inspect.isfunction(x) or inspect.isclass(x)))
    
    for name, obj in members:
        if inspect.isfunction(obj):
            print(f"Hàm: {name}")
            try:
                sig = inspect.signature(obj)
                print(f"  Tham số: {sig}")
            except:
                print("  Không thể lấy chữ ký.")
        elif inspect.isclass(obj):
            print(f"Lớp: {name}")
            methods = inspect.getmembers(obj, predicate=inspect.isfunction)
            for m_name, m_func in methods:
                try:
                    sig = inspect.signature(m_func)
                    print(f"  Phương thức {m_name}: {sig}")
                except:
                    print(f"  Phương thức {m_name}: không thể lấy chữ ký.")


def find_functions_with_kwargs(module):
    functions = []
    members = inspect.getmembers(module, predicate=inspect.isfunction)
    
    for name, func in members:
        sig = inspect.signature(func)
        for param in sig.parameters.values():
            if param.kind == inspect.Parameter.VAR_KEYWORD:  # **kwargs
                functions.append(name)
                break
    return functions

def validate_types(func):
    # Giả định: kiểu được ghi trong annotation đơn giản, ví dụ: def func(a: int, b: str)
    annotations = func.__annotations__
    
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        
        for name, value in bound.arguments.items():
            if name in annotations:
                expected_type = annotations[name]
                if not isinstance(value, expected_type):
                    raise TypeError(f"Tham số '{name}' phải là kiểu {expected_type.__name__}, nhận được {type(value).__name__}")
        
        return func(*args, **kwargs)
    return wrapper
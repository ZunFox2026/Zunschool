import inspect
import sys
from datetime import datetime

# Bài tập 1: In ra tất cả các phương thức public của một lớp
def print_public_methods(cls):
    # Lấy tất cả thành viên là hàm và không bắt đầu bằng _
    methods = [name for name, func in inspect.getmembers(cls, predicate=inspect.isfunction)
               if not name.startswith("_")]
    print(f"Các phương thức public của lớp {cls.__name__}:")
    for method in methods:
        print(f"- {method}")

# Bài tập 2: Kiểm tra hàm có tham số bắt buộc nào không
def has_required_params(func):
    sig = inspect.signature(func)
    for param in sig.parameters.values():
        # Nếu tham số không có giá trị mặc định và không phải là *args hoặc **kwargs
        if param.default == param.empty and param.kind not in (param.VAR_POSITIONAL, param.VAR_KEYWORD):
            return True
    return False

# Bài tập 3: Decorator ghi log thời gian gọi và ai gọi
def log_call(func):
    def wrapper(*args, **kwargs):
        # Lấy thời gian hiện tại
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Lấy thông tin người gọi từ stack
        frame = inspect.currentframe().f_back
        caller_name = frame.f_code.co_name
        
        print(f"[LOG] {current_time} - Hàm '{func.__name__}' được gọi bởi '{caller_name}'")
        
        return func(*args, **kwargs)
    return wrapper

# Bài tập 4: Lấy danh sách lớp con trực tiếp
def get_direct_subclasses(parent_class, module):
    subclasses = []
    # Duyệt qua tất cả các thành viên trong module
    for name, obj in inspect.getmembers(module):
        # Kiểm tra xem có phải là lớp, là con của parent_class và không phải chính parent_class
        if (inspect.isclass(obj) and 
            issubclass(obj, parent_class) and 
            obj != parent_class):
            subclasses.append(obj)
    return subclasses

# Bài tập 5: Kiểm tra hàm có dùng biến toàn cục không
def uses_global_variables(func):
    # Lấy code object của hàm
    code = func.__code__
    # Lấy danh sách tên biến toàn cục mà hàm tham chiếu
    global_names = code.co_names
    
    # Lấy danh sách global thực sự được khai báo trong hàm (nếu có)
    # Tuy nhiên, đơn giản hơn: nếu có lệnh global trong hàm, thì dùng global
    # Hoặc nếu truy cập biến không ở local và nonlocal thì là global
    # Cách đơn giản: kiểm tra xem có tên biến nào trong co_names mà không có trong tham số hoặc local?
    # Tuy nhiên, cách chính xác hơn là kiểm tra qua dis hoặc phân tích
    
    # Cách thực tế: nếu có lệnh global trong code
    # Nhưng inspect không cung cấp trực tiếp, nên dùng heuristic: nếu có co_names và hàm có global
    # Ta kiểm tra xem hàm có khai báo global không
    # Thực ra: nếu co_names tồn tại và tên biến đó không phải là built-in
    
    # Cách đơn giản: kiểm tra co_names và loại bỏ built-in
    import builtins
    builtin_names = set(dir(builtins))
    for name in global_names:
        if name not in builtin_names:
            # Nếu tên này không phải là thuộc tính của hàm (như __name__), và không có trong local thì có thể là global
            # Nhưng khó xác định 100% mà không parse code
            # Tuy nhiên, nếu hàm có lệnh global, thì co_names sẽ chứa tên đó và nó không ở local
            # Chúng ta giả định rằng nếu tên không phải built-in và không phải tham số, thì có thể là global
            # Nhưng không chính xác lắm
            
            # Cách tốt hơn: dùng inspect.getclosurevars() (Python 3.3+)
            try:
                closure_vars = inspect.getclosurevars(func)
                if name in closure_vars.globals or name in closure_vars.unbound:
                    return True
            except Exception:
                pass
    return False

# --- Kiểm thử các lời giải ---
if __name__ == "__main__":
    # Kiểm thử bài 1
    class TestClass:
        def public_method(self):
            pass
        def _private_method(self):
            pass

    print_public_methods(TestClass)
    
    # Kiểm thử bài 2
    def func1(a, b=2): return a + b
    def func2(a, b): return a + b
    def func3(): return "ok"
    print(f"func1 có tham số bắt buộc? {has_required_params(func1)}")
    print(f"func2 có tham số bắt buộc? {has_required_params(func2)}")
    print(f"func3 có tham số bắt buộc? {has_required_params(func3)}")
    
    # Kiểm thử bài 3
    @log_call
    def test_log():
        print("Đang thực hiện test_log...")
    
    def caller():
        test_log()
    
    caller()
    
    # Kiểm thử bài 4
    class Animal: pass
    class Dog(Animal): pass
    class Cat(Animal): pass
    class Bird: pass
    
    subclasses = get_direct_subclasses(Animal, sys.modules[__name__])
    print(f"Lớp con của Animal: {[cls.__name__ for cls in subclasses]}")
    
    # Kiểm thử bài 5
    x = 10
    def uses_x():
        return x  # truy cập biến global x
    
    def no_global():
        return len("hello")  # chỉ dùng built-in
    
    print(f"uses_x dùng biến global? {uses_global_variables(uses_x)}")
    print(f"no_global dùng biến global? {uses_global_variables(no_global)}")
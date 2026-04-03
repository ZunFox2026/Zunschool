import inspect

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Xin chào, tôi là {self.name}"

    def have_birthday(self):
        self.age += 1
        return f"{self.name} vừa tròn {self.age} tuổi!"

# --- Ví dụ 1: Serializer đối tượng tự động ---
def object_to_dict(obj):
    """
    Chuyển một đối tượng thành dictionary bằng cách sử dụng phản xạ.
    Bỏ qua các phương thức và thuộc tính nội bộ (bắt đầu bằng _).
    """
    result = {}
    for attr_name in dir(obj):
        # Bỏ qua các thuộc tính nội bộ và phương thức
        if attr_name.startswith('_'):
            continue
        attr_value = getattr(obj, attr_name)
        if not callable(attr_value):  # Không phải hàm
            result[attr_name] = attr_value
    return result

# Sử dụng
person = Person("Alice", 30)
print("Ví dụ 1 - Serializer:")
print(object_to_dict(person))

# --- Ví dụ 2: Gọi phương thức theo tên (plugin pattern) ---
def call_method_by_name(obj, method_name, *args, **kwargs):
    """
    Gọi một phương thức của đối tượng nếu tồn tại.
    Trả về kết quả hoặc thông báo lỗi nếu không tồn tại hoặc không phải phương thức.
    """
    if hasattr(obj, method_name):
        method = getattr(obj, method_name)
        if callable(method):
            return method(*args, **kwargs)
        else:
            return f"Lỗi: '{method_name}' không phải là phương thức."
    else:
        return f"Lỗi: Đối tượng không có phương thức '{method_name}'."

print("\nVí dụ 2 - Gọi phương thức theo tên:")
print(call_method_by_name(person, "greet"))
print(call_method_by_name(person, "have_birthday"))
print(call_method_by_name(person, "nonexistent"))

# --- Ví dụ 3: Ghi log tham số hàm bằng inspect ---
def log_call(func):
    """
    Decorator để ghi log các tham số khi gọi hàm.
    Sử dụng inspect để phân tích tham số.
    """
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"Hàm '{func.__name__}' được gọi với:")
        for name, value in bound_args.arguments.items():
            print(f"  {name} = {value}")
        
        return func(*args, **kwargs)
    return wrapper

@log_call
def create_user(name, email, age=18, active=True):
    return {"name": name, "email": email, "age": age, "active": active}

print("\nVí dụ 3 - Ghi log tham số:")
user = create_user("Bob", "bob@example.com", age=25)
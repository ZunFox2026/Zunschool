###################
# Bài 77: Sử dụng Descriptor để Tạo Thuộc Tính Thông Minh
# File: main.py
# Các ví dụ minh họa chi tiết
###################

class PositiveNumber:
    """Descriptor kiểm tra số dương"""
    def __init__(self, name):
        self.name = name  # Tên thuộc tính (dùng để gỡ lỗi)

    def __get__(self, instance, owner):
        # Trả về giá trị từ instance
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        # Kiểm tra giá trị trước khi gán
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} phải là số")
        if value < 0:
            raise ValueError(f"{self.name} phải là số dương")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        # Xóa giá trị
        if self.name in instance.__dict__:
            del instance.__dict__[self.name]


class Product:
    # Sử dụng descriptor cho thuộc tính price và quantity
    price = PositiveNumber('price')
    quantity = PositiveNumber('quantity')

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


# --- Ví dụ 2: Descriptor với caching ---
import time

class CachedProperty:
    """Descriptor tính toán và cache giá trị"""
    def __init__(self, func):
        self.func = func
        self.cache_name = f"_cache_{func.__name__}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # Kiểm tra cache
        if not hasattr(instance, self.cache_name):
            print(f"Tính toán lần đầu cho {self.func.__name__}...")
            setattr(instance, self.cache_name, self.func(instance))
        return getattr(instance, self.cache_name)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @CachedProperty
    def area(self):
        time.sleep(1)  # Giả lập tính toán nặng
        return 3.14159 * self.radius ** 2

    @CachedProperty
    def perimeter(self):
        time.sleep(1)
        return 2 * 3.14159 * self.radius


# --- Ví dụ 3: Ghi log truy cập ---
class LoggedAttribute:
    """Ghi log mỗi khi truy cập hoặc gán"""
    def __init__(self, initial_value=None):
        self.value = initial_value
        self.access_count = 0

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.access_count += 1
        print(f"[LOG] Đọc thuộc tính, lần thứ {self.access_count}")
        return self.value

    def __set__(self, instance, value):
        print(f"[LOG] Gán giá trị mới: {value}")
        self.value = value


class User:
    name = LoggedAttribute()

    def __init__(self, name):
        self.name = name  # Gọi __set__


# --- Chạy ví dụ ---
if __name__ == "__main__":
    print("=== Ví dụ 1: Kiểm tra số dương ===")
    try:
        p = Product("Laptop", 1000, 5)
        print(f"Tổng giá trị: {p.total_value()}")
        p.price = 1200
        print(f"Giá mới: {p.price}")
        # p.quantity = -3  # Sẽ gây lỗi
    except (ValueError, TypeError) as e:
        print(f"Lỗi: {e}")

    print("\n=== Ví dụ 2: Caching tính toán ===")
    c = Circle(5)
    print(f"Diện tích: {c.area:.2f}")  # Tính lần đầu
    print(f"Diện tích: {c.area:.2f}")  # Lấy từ cache
    print(f"Chu vi: {c.perimeter:.2f}")  # Tính lần đầu
    print(f"Chu vi: {c.perimeter:.2f}")  # Lấy từ cache

    print("\n=== Ví dụ 3: Ghi log truy cập ===")
    u = User("Alice")
    print(u.name)
    print(u.name)
    u.name = "Bob"
    print(u.name)

import inspect

class Car:
    """Lớp mô tả một chiếc xe hơi."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        """Khởi động động cơ."""
        print(f"{self.brand} {self.model} đang khởi động...")

    def honk(self):
        """Bấm còi."""
        print("Beep beep!")

    def get_info(self):
        """Trả về thông tin xe."""
        return f"{self.year} {self.brand} {self.model}"

def example_1():
    """Ví dụ 1: Liệt kê các phương thức và thuộc tính của lớp Car."""
    print("=== Ví dụ 1: Liệt kê thành viên của lớp Car ===")
    members = inspect.getmembers(Car, predicate=inspect.isfunction)
    for name, func in members:
        doc = inspect.getdoc(func) or "Không có mô tả"
        print(f"- {name}: {doc}")


def example_2():
    """Ví dụ 2: Lấy thông tin tham số của hàm."""
    print("\n=== Ví dụ 2: Phân tích tham số hàm get_info ===")
    sig = inspect.signature(Car.get_info)
    print(f"Chữ ký của get_info: {sig}")
    for name, param in sig.parameters.items():
        print(f"  Tham số: {name}, loại: {param.kind}")


def example_3():
    """Ví dụ 3: Decorator ghi log tự động."""
    print("\n=== Ví dụ 3: Ghi log tự động bằng inspect ===")

    def log_call(func):
        def wrapper(*args, **kwargs):
            # Lấy thông tin hàm
            func_name = func.__name__
            # Lấy tham số
            bound_args = inspect.signature(func).bind(*args, **kwargs)
            bound_args.apply_defaults()
            print(f"[LOG] Gọi hàm '{func_name}' với tham số: {dict(bound_args.arguments)}")
            result = func(*args, **kwargs)
            print(f"[LOG] Hàm '{func_name}' trả về: {result}")
            return result
        return wrapper

    @log_call
    def add(a, b=10):
        """Cộng hai số."""
        return a + b

    # Gọi hàm
    add(5)
    add(3, 7)

if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
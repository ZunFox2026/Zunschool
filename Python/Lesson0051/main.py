import inspect

class Person:
    """Lớp mô tả một người."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Xin chào, tôi là {self.name}"

    def have_birthday(self):
        self.age += 1
        return f"{self.name} vừa tròn {self.age} tuổi!"


def hello(name: str, greeting: str = "Xin chào") -> None:
    """Hàm chào hỏi một người với lời chào tùy chọn."""
    print(f"{greeting} {name}!")


def example_1():
    """Ví dụ 1: Liệt kê tất cả thành viên của lớp Person."""
    print("=== Ví dụ 1: Liệt kê thành viên của lớp Person ===")
    members = inspect.getmembers(Person)
    for name, obj in members:
        # Chỉ in các phương thức (loại bỏ các thuộc tính đặc biệt như __init__ nếu muốn)
        if inspect.isfunction(obj):
            print(f"Phương thức: {name}")


def example_2():
    """Ví dụ 2: Lấy mã nguồn của hàm hello."""
    print("\n=== Ví dụ 2: Lấy mã nguồn của hàm hello ===")
    try:
        source = inspect.getsource(hello)
        print(source)
    except OSError:
        print("Không thể lấy mã nguồn (hàm có thể được định nghĩa trong REPL).")


def example_3():
    """Ví dụ 3: Kiểm tra chữ ký (tham số) của hàm hello."""
    print("\n=== Ví dụ 3: Kiểm tra chữ ký của hàm hello ===")
    sig = inspect.signature(hello)
    print(f"Chữ ký hàm hello: {sig}")

    # In chi tiết từng tham số
    for param_name, param in sig.parameters.items():
        print(f"- Tham số: {param_name}, Loại: {param.kind}, Mặc định: {param.default}")


def example_4():
    """Ví dụ 4: In thông tin về hàm đang gọi (sử dụng stack)."""
    def inner_function():
        frame = inspect.currentframe()
        caller_name = frame.f_back.f_code.co_name
        print(f"Hàm \"inner_function\" được gọi từ hàm: {caller_name}")

    print("\n=== Ví dụ 4: Sử dụng inspect để xem call stack ===")
    inner_function()


if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
    example_4()
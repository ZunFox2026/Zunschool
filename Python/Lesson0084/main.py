import inspect

class Calculator:
    """Lớp máy tính đơn giản với một số phương thức cơ bản."""
    
    def __init__(self):
        self.history = []

    def add(self, a, b):
        """Cộng hai số."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """Trừ hai số."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def get_history(self):
        """Lấy lịch sử các phép tính."""
        return self.history

# Ví dụ 1: Kiểm tra các thành viên của lớp Calculator
def example_1():
    print("=== Ví dụ 1: Kiểm tra thành viên của lớp Calculator ===")
    members = inspect.getmembers(Calculator, predicate=inspect.isfunction)
    for name, func in members:
        print(f"Phương thức: {name}, Đang là hàm: {inspect.isfunction(func)}")

# Ví dụ 2: Lấy chữ ký (signature) của một hàm
def example_2():
    print("\n=== Ví dụ 2: Lấy chữ ký của phương thức add ===")
    calc = Calculator()
    sig = inspect.signature(calc.add)
    print(f"Chữ ký của add: {sig}")
    
    # Phân tích từng tham số
    for param_name, param in sig.parameters.items():
        print(f"Tham số: {param_name}, Mặc định: {param.default}, Kiểu: {param.annotation}")

# Ví dụ 3: In mã nguồn của một hàm
def example_3():
    print("\n=== Ví dụ 3: In mã nguồn của phương thức get_history ===")
    calc = Calculator()
    try:
        source = inspect.getsource(calc.get_history)
        print("Mã nguồn:")
        print(source)
    except OSError:
        print("Không thể lấy mã nguồn (có thể do hàm built-in hoặc không có file nguồn).")

# Gọi các ví dụ
def main():
    example_1()
    example_2()
    example_3()

if __name__ == "__main__":
    main()
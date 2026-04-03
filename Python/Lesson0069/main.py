from contextlib import contextmanager
import time
import os
from tempfile import NamedTemporaryFile

# Ví dụ 1: Đo thời gian thực thi

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        print("Bắt đầu đo thời gian...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.time() - self.start_time
        print(f"Thời gian thực thi: {elapsed:.4f} giây")
        return False  # Không xử lý lỗi, để lỗi ném ra ngoài

# Sử dụng Timer
with Timer():
    time.sleep(1)  # Giả lập công việc
    print("Đang xử lý...")


# Ví dụ 2: Quản lý kết nối cơ sở dữ liệu giả lập
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        print(f"Kết nối đến cơ sở dữ liệu '{self.db_name}'...")
        self.connected = True
        return self

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Chưa kết nối đến CSDL")
        print(f"Thực thi truy vấn: {sql}")

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Đóng kết nối đến '{self.db_name}'")
        self.connected = False
        # Nếu có lỗi, in ra thông báo
        if exc_type:
            print(f"Lỗi xảy ra: {exc_value}")
        return False  # Để lỗi ném ra ngoài nếu có

# Sử dụng DatabaseConnection
with DatabaseConnection("myapp_db") as db:
    db.query("SELECT * FROM users")
    # Giả lập lỗi
    # raise ValueError("Lỗi giả lập")


# Ví dụ 3: Tạm thời thay đổi thư mục làm việc
@contextmanager
def change_dir(destination):
    current_dir = os.getcwd()  # Lưu thư mục hiện tại
    print(f"Chuyển đến: {destination}")
    try:
        os.chdir(destination)
        yield  # Nhường quyền cho khối with
    finally:
        os.chdir(current_dir)
        print(f"Quay lại thư mục: {current_dir}")

# Sử dụng change_dir
with change_dir("/"):
    print("Thư mục hiện tại:", os.getcwd())

print("Trở lại:", os.getcwd())
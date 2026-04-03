import time
import os
from contextlib import contextmanager

# Ví dụ 1: Đo thời gian thực thi
class Timer:
    def __enter__(self):
        self.start_time = time.time()
        print("Bắt đầu đo thời gian...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        print(f"Kết thúc đo thời gian. Thời gian thực thi: {self.end_time - self.start_time:.4f} giây")
        # Không xử lý exception, để exception lan ra ngoài nếu có
        return False

# Sử dụng Timer
print("=== Ví dụ 1: Đo thời gian thực thi ===")
with Timer():
    time.sleep(1)
    print("Đang thực hiện công việc...")


# Ví dụ 2: Quản lý kết nối cơ sở dữ liệu giả lập
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        print(f"Kết nối đến cơ sở dữ liệu {self.db_name}...")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connected:
            print(f"Đóng kết nối đến {self.db_name}.")
            self.connected = False
        # Nếu có lỗi, in ra thông báo
        if exc_type is not None:
            print(f"Lỗi xảy ra: {exc_value}")
        return False  # Không chặn exception

# Sử dụng DatabaseConnection
print("\n=== Ví dụ 2: Quản lý kết nối CSDL ===")
with DatabaseConnection("mydb.sqlite") as db:
    print(f"Đã kết nối: {db.connected}")
    # Giả lập một thao tác
    print("Thực hiện truy vấn...")
    # Nếu muốn thử lỗi, bỏ comment dòng sau:
    # raise ValueError("Lỗi truy vấn")


# Ví dụ 3: Tạm thời thay đổi thư mục làm việc
@contextmanager
def change_dir(destination):
    # Lưu thư mục hiện tại
    current_dir = os.getcwd()
    print(f"Thư mục ban đầu: {current_dir}")
    try:
        # Chuyển đến thư mục mới
        os.chdir(destination)
        print(f"Đã chuyển đến: {destination}")
        yield  # Trả quyền điều khiển cho khối with
    finally:
        # Luôn quay lại thư mục ban đầu
        os.chdir(current_dir)
        print(f"Đã quay lại thư mục: {current_dir}")

# Sử dụng change_dir
print("\n=== Ví dụ 3: Thay đổi thư mục làm việc ===")
with change_dir(".."):
    print(f"Thư mục hiện tại trong khối with: {os.getcwd()}")
print(f"Thư mục sau khi thoát khối with: {os.getcwd()}")
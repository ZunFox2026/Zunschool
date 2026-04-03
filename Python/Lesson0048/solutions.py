from contextlib import contextmanager
import os
import time

# Bài tập 1: Viết Context Manager để tạm thời thay đổi thư mục làm việc

class TemporaryDirectory:
    def __init__(self, path):
        self.path = path
        self.original_path = None

    def __enter__(self):
        self.original_path = os.getcwd()  # Lưu thư mục hiện tại
        os.chdir(self.path)  # Chuyển đến thư mục mới
        print(f"Đã chuyển đến: {self.path}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.original_path)  # Quay lại thư mục ban đầu
        print(f"Đã quay lại: {self.original_path}")

# Bài tập 2: Viết Context Manager để đếm số lần gọi hàm

class CallCounter:
    def __init__(self):
        self.count = 0

    def __enter__(self):
        self.count = 0  # Reset bộ đếm
        # Ghi đè hàm print để đếm
        self.original_print = __builtins__.print

        def counting_print(*args, **kwargs):
            self.count += 1
            self.original_print(*args, **kwargs)

        __builtins__.print = counting_print
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Khôi phục lại hàm print gốc
        __builtins__.print = self.original_print
        print(f"Số lần gọi print(): {self.count}")

# Bài tập 3: Viết Context Manager để tắt/bật logging

LOG_ENABLED = True

class LoggingControl:
    def __init__(self, enable):
        self.enable = enable
        self.original_state = None

    def __enter__(self):
        global LOG_ENABLED
        self.original_state = LOG_ENABLED  # Lưu trạng thái cũ
        LOG_ENABLED = self.enable  # Cập nhật trạng thái mới
        print(f"Logging được {'bật' if self.enable else 'tắt'}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        global LOG_ENABLED
        LOG_ENABLED = self.original_state  # Khôi phục trạng thái cũ
        print(f"Đã khôi phục trạng thái logging: {'bật' if self.original_state else 'tắt'}")

# Hàm hỗ trợ logging
def log(message):
    if LOG_ENABLED:
        print(f"[LOG] {message}")

# Bài tập 4: Viết Context Manager tạo file tạm và tự xóa

@contextmanager
def temporary_file(filename):
    try:
        print(f"Tạo file tạm: {filename}")
        with open(filename, 'w') as f:
            f.write("Nội dung tạm thời\n")
        yield filename  # Trả về tên file để sử dụng
    finally:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Đã xóa file tạm: {filename}")

# Bài tập 5: Viết Context Manager giới hạn thời gian thực thi (timeout giả lập)

class Timeout:
    def __init__(self, seconds):
        self.seconds = seconds
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        print(f"Bắt đầu khối với timeout {self.seconds}s")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.time() - self.start_time
        print(f"Đã chạy trong {elapsed:.2f} giây")
        if elapsed > self.seconds:
            print("Cảnh báo: Khối code thực thi lâu hơn timeout!")
        else:
            print("Thực thi trong giới hạn thời gian.")
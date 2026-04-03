import time
import os
from contextlib import contextmanager

######################
# Bài tập 1: Đếm số dòng trong file
class LineCounter:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = None
        self.line_count = 0

    def __enter__(self):
        # Mở file để đọc
        self.file = open(self.filepath, 'r', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        # Không xử lý lỗi, để nguyên
        return False

    def count_lines(self):
        # Đọc và đếm từng dòng
        self.line_count = 0
        for line in self.file:
            self.line_count += 1
        return self.line_count


######################
# Bài tập 2: Tạm thời đổi thư mục
class TemporaryDirectory:
    def __init__(self, new_dir):
        self.new_dir = new_dir
        self.old_dir = None

    def __enter__(self):
        self.old_dir = os.getcwd()  # Lưu thư mục hiện tại
        os.chdir(self.new_dir)      # Chuyển đến thư mục mới
        return self.new_dir

    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.chdir(self.old_dir)      # Luôn quay lại thư mục cũ
        return False


######################
# Bài tập 3: Ghi log hành động
from datetime import datetime
class ActionLogger:
    def __init__(self, log_file):
        self.log_file = log_file

    def __enter__(self):
        self.start_time = datetime.now()
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f'[LOG] Bắt đầu: {self.start_time}\n')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        end_time = datetime.now()
        with open(self.log_file, 'a', encoding='utf-8') as f:
            if exc_type is None:
                f.write(f'[LOG] Kết thúc bình thường: {end_time}\n')
            else:
                f.write(f'[LOG] Kết thúc với lỗi {exc_type.__name__}: {exc_value} tại {end_time}\n')
        return False  # Không chặn ngoại lệ


######################
# Bài tập 4: Timer dùng contextmanager
@contextmanager
def timer_function():
    start = time.time()
    print('Bắt đầu đo thời gian...')
    try:
        yield  # Trả quyền điều khiển cho khối with
    finally:
        end = time.time()
        print(f'Thời gian thực thi: {end - start:.4f} giây')


######################
# Bài tập 5: Tạm thời tắt logging
LOGGING_ENABLED = True
class SilentMode:
    def __enter__(self):
        global LOGGING_ENABLED
        self.was_enabled = LOGGING_ENABLED  # Lưu trạng thái cũ
        LOGGING_ENABLED = False             # Tắt logging
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        global LOGGING_ENABLED
        LOGGING_ENABLED = self.was_enabled  # Khôi phục trạng thái
        return False

# --- Ví dụ sử dụng các lời giải ---
if __name__ == "__main__":
    # Bài 1
    with open('test_lines.txt', 'w') as f:
        f.write('Dòng 1\nDòng 2\nDòng 3\n')
    
    with LineCounter('test_lines.txt') as lc:
        print(f'Số dòng: {lc.count_lines()}')

    # Bài 2
    print(f'Thư mục hiện tại: {os.getcwd()}')
    with TemporaryDirectory('.'):
        print(f'Thư mục trong with: {os.getcwd()}')
    print(f'Ra khỏi with, quay lại: {os.getcwd()}')

    # Bài 3
    with ActionLogger('activity.log'):
        time.sleep(0.5)
        print("Hành động đang diễn ra...")

    # Bài 4
    with timer_function():
        time.sleep(0.3)

    # Bài 5
    print(f'Logging ban đầu: {LOGGING_ENABLED}')
    with SilentMode():
        print(f'Logging trong SilentMode: {LOGGING_ENABLED}')
    print(f'Logging sau khi thoát: {LOGGING_ENABLED}')

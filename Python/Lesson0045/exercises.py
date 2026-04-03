#####################
# Bài tập 1
# Tạo context manager ghi log thời gian bắt đầu và kết thúc
# Sử dụng print hoặc ghi vào file log
#####################
class LogExecution:
    pass  # Viết code tại đây


#####################
# Bài tập 2
# Context manager để đọc/ghi file JSON an toàn
# Nếu file tồn tại, đọc dữ liệu. Nếu không, tạo file mới với dữ liệu rỗng.
# Sau khi dùng xong, ghi lại dữ liệu nếu có thay đổi
#####################
class JSONFile:
    def __init__(self, filename, data=None):
        pass  # Viết code tại đây

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


#####################
# Bài tập 3
# Context manager đếm số dòng được xử lý trong file văn bản
# Sau khi đọc file, in ra số dòng đã xử lý
#####################
class CountLines:
    def __init__(self, filename):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


#####################
# Bài tập 4
# Tạo context manager tạm thời thay đổi biến môi trường
# Sử dụng contextlib.contextmanager
#####################
from contextlib import contextmanager

@contextmanager
def temporary_env(name, value):
    pass  # Viết code tại đây


#####################
# Bài tập 5
# Context manager xử lý ngoại lệ và ghi log
# Nếu có ngoại lệ, in ra log và kìm nén (không cho lan ra ngoài)
#####################
class SafeExecution:
    def __init__(self, log_file="error.log"):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass
from contextlib import contextmanager

# Bài tập 1:
# Viết một Context Manager dùng lớp để quản lý trạng thái "bận" của một thiết bị.
# Khi vào khối with, thiết bị chuyển sang trạng thái bận.
# Khi ra khỏi khối, thiết bị trở lại trạng thái rảnh.
# Gợi ý: Dùng thuộc tính `busy`

class DeviceManager:
    def __init__(self, device_name):
        self.device_name = device_name
        self.busy = False

    def __enter__(self):
        # TODO: Thiết lập thiết bị thành bận
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        # TODO: Đặt lại trạng thái rảnh
        pass


# Bài tập 2:
# Viết Context Manager dùng @contextmanager để tạm thời thay đổi thư mục làm việc.
# Khi vào khối, chuyển đến thư mục đã cho.
# Khi ra, quay lại thư mục ban đầu.
# Gợi ý: Dùng os.getcwd() và os.chdir()

def change_dir(target_dir):
    # TODO: Viết hàm context manager
    pass


# Bài tập 3:
# Viết Context Manager để ghi log thời gian bắt đầu và kết thúc một hành động.
# In ra: "[BẮT ĐẦU] Hành động: <tên>" và "[KẾT THÚC] Hành động: <tên>"
# Gợi ý: Dùng time.strftime để lấy thời gian hiện tại

def log_action(action_name):
    # TODO: Viết hàm context manager
    pass
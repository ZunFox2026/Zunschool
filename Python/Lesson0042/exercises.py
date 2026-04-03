####################
# Bài tập 1
# Viết hàm in thông tin chi tiết về một đối tượng: tên lớp, các thuộc tính và giá trị
# Không in các phương thức và thuộc tính bắt đầu bằng '_'
def print_object_info(obj):
    pass

####################
# Bài tập 2
# Tạo lớp CommandRunner với các lệnh: start, stop, restart, status
# Viết phương thức run(command) để gọi lệnh tương ứng
# Nếu lệnh không tồn tại, in thông báo lỗi
class CommandRunner:
    def __init__(self):
        self.state = "stopped"

    def start(self):
        if self.state == "stopped":
            self.state = "running"
            print("Đã khởi động.")
        else:
            print("Đã đang chạy.")

    def stop(self):
        if self.state == "running":
            self.state = "stopped"
            print("Đã dừng.")
        else:
            print("Đã dừng rồi.")

    def restart(self):
        self.stop()
        self.start()

    def status(self):
        print(f"Trạng thái: {self.state}")

    def run(self, command_name):
        # Gọi phương thức từ tên chuỗi
        pass

####################
# Bài tập 3
# Viết hàm log_call() in ra tên hàm đang gọi và các tham số đầu vào
# Sử dụng inspect để lấy thông tin
# Gợi ý: inspect.stack()[1] để lấy frame của hàm gọi
def log_call():
    pass

# Hàm ví dụ sử dụng log_call
def divide(a, b):
    log_call()
    return a / b if b != 0 else 0

####################
# Bài tập 4
# Viết hàm serialize_object(obj) trả về từ điển chứa các thuộc tính dữ liệu của đối tượng
def serialize_object(obj):
    """Chuyển đổi object thành dict chỉ chứa thuộc tính dữ liệu"""
    pass

####################
# Bài tập 5
# Viết hàm check_required_params(func) trả về danh sách các tham số bắt buộc (không có giá trị mặc định)
def check_required_params(func):
    pass
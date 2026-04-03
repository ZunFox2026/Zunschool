################################################################################
# Bài tập 1: Viết Context Manager để tạm thời thay đổi thư mục làm việc
# Gợi ý: Sử dụng os.getcwd() và os.chdir()

class TemporaryDirectory:
    def __init__(self, path):
        self.path = path
        self.original_dir = None

    def __enter__(self):
        # TODO: Lưu thư mục hiện tại và chuyển đến self.path
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        # TODO: Quay lại thư mục ban đầu
        pass


################################################################################
# Bài tập 2: Viết Context Manager để đếm số lượng dòng khi đọc file

class LineCountContext:
    def __init__(self, filename):
        self.filename = filename
        self.line_count = 0

    def __enter__(self):
        # TODO: Mở file và trả về file object, đồng thời đếm dòng
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        # TODO: In ra số dòng đã đọc
        pass


################################################################################
# Bài tập 3: Viết Context Manager bắt lỗi và ghi log, không ngắt chương trình

class SafeExecution:
    def __init__(self, log_file="error.log"):
        self.log_file = log_file

    def __enter__(self):
        # TODO: Trả về self hoặc bất kỳ giá trị cần thiết
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        # TODO: Nếu có lỗi, ghi vào file log và trả về True để ngăn lỗi
        pass


################################################################################
# Bài tập 4: Viết Context Manager quản lý bộ nhớ đệm (cache) trong khối lệnh

class TemporaryCache:
    def __init__(self, cache_dict):
        self.cache_dict = cache_dict
        self.backup = None

    def __enter__(self):
        # TODO: Sao lưu cache hiện tại
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        # TODO: Khôi phục cache như ban đầu
        pass


################################################################################
# Bài tập 5: In thông báo khi có ngoại lệ, nhưng cho phép chương trình tiếp tục

class NotifyOnError:
    def __enter__(self):
        print("Bắt đầu khối lệnh...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # TODO: Nếu có lỗi, in thông báo, nhưng không bắt
        pass
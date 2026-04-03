# exercises.py - Bài tập thực hành cho bài học 26

# Bài 1: Viết hàm chia hai số
# Viết hàm chia(a, b) trả về kết quả a / b
# Xử lý lỗi: chia cho 0 và kiểu dữ liệu không phải số

def chia(a, b):
    # TODO: Viết code tại đây
    pass


# Bài 2: Tạo ngoại lệ tùy chỉnh cho tuổi
# Tạo lớp AgeError kế thừa từ Exception
# Viết hàm kiem_tra_tuoi(tuoi) kiểm tra nếu tuổi < 0 hoặc > 150 thì ném lỗi

class AgeError(Exception):
    # TODO: Định nghĩa lớp
    pass

def kiem_tra_tuoi(tuoi):
    # TODO: Viết code tại đây
    pass


# Bài 3: Đọc danh sách tên từ file
# Viết hàm doc_danh_sach_ten(ten_file)
# Mỗi tên trên một dòng. Xử lý lỗi file không tồn tại, file rỗng

def doc_danh_sach_ten(ten_file):
    # TODO: Viết code tại đây
    pass


# Bài 4: Đăng nhập với xác thực
# Viết hàm dang_nhap(ten_dang_nhap, mat_khau)
# Nếu sai tên hoặc mật khẩu, ném lỗi LoginError

class LoginError(Exception):
    pass

def dang_nhap(ten_dang_nhap, mat_khau):
    # TODO: Viết code tại đây
    pass


# Bài 5: Kiểm tra nhiệt độ hợp lệ
# Tạo lớp Temperature
# Phương thức dat_nhiet_do(deg) - ném lỗi nếu deg < -273.15

class NhietDoQuaThapError(Exception):
    pass

class Temperature:
    def __init__(self):
        self.deg = 0

    def dat_nhiet_do(self, deg):
        # TODO: Viết code tại đây
        pass
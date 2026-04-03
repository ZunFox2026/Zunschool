# solutions.py - Lời giải bài tập bài học 26

# Bài 1: Viết hàm chia hai số

def chia(a, b):
    try:
        ket_qua = a / b
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0")
        return None
    except (TypeError, ValueError):
        print("Lỗi: Đối số phải là số")
        return None
    else:
        print(f"Kết quả: {a} / {b} = {ket_qua}")
        return ket_qua
    finally:
        print("Hoàn tất phép chia.")


# Bài 2: Tạo ngoại lệ tùy chỉnh cho tuổi

class AgeError(Exception):
    """Ngoại lệ khi tuổi không hợp lệ"""
    pass

def kiem_tra_tuoi(tuoi):
    try:
        if tuoi < 0:
            raise AgeError("Tuổi không thể âm")
        if tuoi > 150:
            raise AgeError("Tuổi không hợp lý (trên 150)")
    except AgeError as e:
        print(f"Lỗi tuổi: {e}")
        return False
    else:
        print(f"Tuổi {tuoi} là hợp lệ.")
        return True
    finally:
        print("Đã kiểm tra xong tuổi.")


# Bài 3: Đọc danh sách tên từ file

def doc_danh_sach_ten(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            danh_sach = [ten.strip() for ten in f.readlines()]
            if not danh_sach:
                raise ValueError("File rỗng")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'")
    except ValueError as e:
        print(f"Lỗi dữ liệu: {e}")
    else:
        print("Danh sách tên:")
        for ten in danh_sach:
            print(f"- {ten}")
    finally:
        print("Xử lý đọc file hoàn tất.")


# Bài 4: Đăng nhập với xác thực

class LoginError(Exception):
    """Ngoại lệ khi đăng nhập thất bại"""
    pass

def dang_nhap(ten_dang_nhap, mat_khau):
    ten_chinh = "admin"
    mat_khau_chinh = "123456"
    
    try:
        if ten_dang_nhap != ten_chinh:
            raise LoginError("Tên đăng nhập sai")
        if mat_khau != mat_khau_chinh:
            raise LoginError("Mật khẩu sai")
    except LoginError as e:
        print(f"Đăng nhập thất bại: {e}")
        return False
    else:
        print("Đăng nhập thành công!")
        return True
    finally:
        print("Xử lý đăng nhập xong.")


# Bài 5: Kiểm tra nhiệt độ hợp lệ

class NhietDoQuaThapError(Exception):
    """Ngoại lệ khi nhiệt độ dưới 0 độ K"""
    pass

class Temperature:
    def __init__(self):
        self.deg = 0

    def dat_nhiet_do(self, deg):
        try:
            if deg < -273.15:
                raise NhietDoQuaThapError("Nhiệt độ không thể dưới -273.15°C (0 K)")
            self.deg = deg
        except NhietDoQuaThapError as e:
            print(f"Lỗi nhiệt độ: {e}")
        else:
            print(f"Đặt nhiệt độ thành công: {self.deg}°C")
        finally:
            print("Cập nhật nhiệt độ hoàn tất.")
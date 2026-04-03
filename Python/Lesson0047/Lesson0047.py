"""
Python 47: Lập Trình Hướng Đối Tượng Cơ Bản
-------------------------------------------
Hướng dẫn cơ bản về lập trình hướng đối tượng (OOP) trong Python
- Định nghĩa lớp (class) và đối tượng (object)
- Thuộc tính (attributes) và phương thức (methods)
- Hàm khởi tạo __init__
- Tính đóng gói (encapsulation)
"""

# === 1. Định nghĩa một lớp cơ bản ===
class SinhVien:
    """
    Lớp SinhVien mô tả thông tin và hành vi của một sinh viên.
    """
    
    def __init__(self, ho_ten, mssv, tuoi):
        """
        Hàm khởi tạo - được gọi khi tạo đối tượng mới.
        :param ho_ten: Họ tên sinh viên
        :param mssv: Mã số sinh viên
        :param tuoi: Tuổi của sinh viên
        """
        self.ho_ten = ho_ten    # Thuộc tính công khai
        self.mssv = mssv
        self.tuoi = tuoi
    
    def hien_thi_thong_tin(self):
        """
        Phương thức hiển thị thông tin sinh viên.
        """
        print(f"Họ tên: {self.ho_ten}")
        print(f"MSSV: {self.mssv}")
        print(f"Tuổi: {self.tuoi}")
    
    def tang_tuoi(self):
        """
        Phương thức tăng tuổi thêm 1.
        """
        self.tuoi += 1
        print(f"{self.ho_ten} đã tăng tuổi lên {self.tuoi}.")


# === 2. Lớp với thuộc tính ẩn (tính đóng gói cơ bản) ===
class TaiKhoanNganHang:
    """
    Lớp mô phỏng tài khoản ngân hàng với tính bảo mật.
    """
    
    def __init__(self, chu_tai_khoan, so_du):
        self.chu_tai_khoan = chu_tai_khoan
        self.__so_du = so_du  # Thuộc tính ẩn (private) - dấu __
    
    def nap_tien(self, so_tien):
        if so_tien > 0:
            self.__so_du += so_tien
            print(f"Nạp {so_tien}đ thành công.")
        else:
            print("Số tiền nạp phải lớn hơn 0.")
    
    def rut_tien(self, so_tien):
        if 0 < so_tien <= self.__so_du:
            self.__so_du -= so_tien
            print(f"Rút {so_tien}đ thành công.")
        else:
            print("Số tiền rút không hợp lệ hoặc vượt quá số dư.")
    
    def xem_so_du(self):
        """
        Getter: Trả về số dư hiện tại.
        """
        print(f"Số dư hiện tại: {self.__so_du}đ")
        return self.__so_du


# === 3. Ví dụ sử dụng ===
def vi_du_1():
    print("=== VÍ DỤ 1: Sử dụng lớp SinhVien ===")
    sv1 = SinhVien("Nguyễn Văn A", "2024001", 19)
    sv1.hien_thi_thong_tin()
    sv1.tang_tuoi()
    sv1.hien_thi_thong_tin()


def vi_du_2():
    print("\n=== VÍ DỤ 2: Sử dụng lớp TaiKhoanNganHang ===")
    tk = TaiKhoanNganHang("Lê Thị B", 5000000)
    tk.nap_tien(2000000)
    tk.rut_tien(1000000)
    tk.xem_so_du()
    # Không thể truy cập trực tiếp: print(tk.__so_du) -> lỗi


# === 4. Bài tập nhỏ ===
"""
BÀI TẬP: Tạo lớp HinhChuNhat
- Có 2 thuộc tính: chieu_dai, chieu_rong
- Có các phương thức:
  + tinh_dien_tich(): trả về diện tích
  + tinh_chu_vi(): trả về chu vi
  + hien_thi(): in ra thông tin
- Tạo 2 đối tượng và thử dùng
"""
class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
    
    def hien_thi(self):
        print(f"Chiều dài: {self.chieu_dai}, Chiều rộng: {self.chieu_rong}")
        print(f"Diện tích: {self.tinh_dien_tich()}")
        print(f"Chu vi: {self.tinh_chu_vi()}")


def bai_tap():
    print("\n=== BÀI TẬP: Lớp Hình Chữ Nhật ===")
    hcn1 = HinhChuNhat(10, 5)
    hcn2 = HinhChuNhat(7, 3)
    
    print("Hình chữ nhật 1:")
    hcn1.hien_thi()
    
    print("\nHình chữ nhật 2:")
    hcn2.hien_thi()


# === Hàm chính ===
def main():
    print("PYTHON 47: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG CƠ BẢN")
    print("=" * 50)
    
    vi_du_1()
    vi_du_2()
    bai_tap()
    
    print("\nHoàn thành chương trình.")


# Chạy chương trình
if __name__ == "__main__":
    main()
```
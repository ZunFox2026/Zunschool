"""
Python 16: Lập Trình Hướng Đối Tượng Cơ Bản
File: oop_basic.py

Giới thiệu về:
- Định nghĩa lớp (class) và đối tượng (object)
- Thuộc tính (attributes) và phương thức (methods)
- Hàm khởi tạo __init__
- Tính đóng gói cơ bản

Sử dụng ví dụ về lớp "SinhVien" và "XeHoi"
"""

# Ví dụ 1: Lớp cơ bản - SinhVien
class SinhVien:
    """
    Lớp SinhVien biểu diễn thông tin và hành động của một sinh viên.
    """
    def __init__(self, ho_ten, mssv, tuoi):
        """
        Hàm khởi tạo: thiết lập các thuộc tính ban đầu
        :param ho_ten: Họ tên sinh viên (str)
        :param mssv: Mã số sinh viên (str)
        :param tuoi: Tuổi (int)
        """
        self.ho_ten = ho_ten  # Thuộc tính công khai
        self.mssv = mssv
        self.tuoi = tuoi
        self.diem = []  # Danh sách điểm rỗng ban đầu

    def them_diem(self, diem):
        """
        Phương thức thêm điểm vào danh sách
        :param diem: Điểm số (float hoặc int)
        """
        if 0 <= diem <= 10:
            self.diem.append(diem)
            print(f"Đã thêm điểm {diem} cho sinh viên {self.ho_ten}")
        else:
            print("Lỗi: Điểm phải nằm trong khoảng 0-10")

    def tinh_diem_trung_binh(self):
        """
        Tính điểm trung bình các môn học
        :return: Điểm trung bình (float) hoặc 0 nếu chưa có điểm
        """
        if len(self.diem) == 0:
            return 0
        return sum(self.diem) / len(self.diem)

    def hien_thi_thong_tin(self):
        """
        Hiển thị thông tin sinh viên
        """
        dtb = self.tinh_diem_trung_binh()
        print(f"Sinh viên: {self.ho_ten}")
        print(f"MSSV: {self.mssv}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Điểm: {self.diem}")
        print(f"Điểm trung bình: {dtb:.2f}")
        print("-" * 30)


# Ví dụ 2: Lớp XeHoi
class XeHoi:
    """
    Lớp XeHoi biểu diễn một chiếc xe hơi với các thuộc tính và hành động cơ bản.
    """
    def __init__(self, hang_xe, mau_sac, so_km=0):
        """
        Khởi tạo xe hơi
        :param hang_xe: Hãng xe (str)
        :param mau_sac: Màu sắc (str)
        :param so_km: Số km đã đi (int)
        """
        self.hang_xe = hang_xe
        self.mau_sac = mau_sac
        self.so_km = so_km
        self.toc_do = 0  # Tốc độ hiện tại (km/h)

    def tang_toc(self, toc_do_moi):
        """
        Tăng tốc xe
        :param toc_do_moi: Tốc độ mới (int)
        """
        if toc_do_moi > self.toc_do:
            self.toc_do = toc_do_moi
            print(f"{self.hang_xe} tăng tốc lên {self.toc_do} km/h")
        else:
            print("Không thể giảm tốc bằng cách tăng tốc!")

    def di_chuyen(self, km):
        """
        Di chuyển thêm một đoạn đường
        :param km: Số km di chuyển (int)
        """
        self.so_km += km
        print(f"Xe {self.hang_xe} đã di chuyển thêm {km} km, tổng: {self.so_km} km")

    def hien_thi_trang_thai(self):
        """
        Hiển thị trạng thái hiện tại của xe
        """
        print(f"Xe {self.hang_xe}, màu {self.mau_sac}")
        print(f"Số km đã đi: {self.so_km} km")
        print(f"Tốc độ hiện tại: {self.toc_do} km/h")
        print("-" * 30)


# Bài tập nhỏ: Tạo lớp HinhChuNhat
class HinhChuNhat:
    """
    Bài tập: Viết lớp Hình Chữ Nhật với chiều dài và chiều rộng,
    tính chu vi và diện tích.
    """
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def hien_thi(self):
        print(f"Hình chữ nhật: dài = {self.chieu_dai}, rộng = {self.chieu_rong}")
        print(f"Chu vi = {self.tinh_chu_vi()}, Diện tích = {self.tinh_dien_tich()}")


# Hàm main để chạy chương trình
def main():
    print("=== VÍ DỤ 1: LỚP SINHVIEN ===")
    sv1 = SinhVien("Nguyễn Văn A", "SV001", 20)
    sv2 = SinhVien("Trần Thị B", "SV002", 19)

    sv1.them_diem(8.5)
    sv1.them_diem(7.0)
    sv1.them_diem(9.0)
    sv1.hien_thi_thong_tin()

    sv2.them_diem(10)
    sv2.them_diem(9.5)
    sv2.hien_thi_thong_tin()

    print("\n=== VÍ DỤ 2: LỚP XEHÔI ===")
    xe1 = XeHoi("Toyota", "Đỏ")
    xe2 = XeHoi("Honda", "Xanh", 5000)

    xe1.tang_toc(60)
    xe1.di_chuyen(100)
    xe1.hien_thi_trang_thai()

    xe2.tang_toc(80)
    xe2.di_chuyen(200)
    xe2.hien_thi_trang_thai()

    print("\n=== BÀI TẬP: LỚP HINHCHUNHAT ===")
    hcn = HinhChuNhat(5, 3)
    hcn.hien_thi()


# Chạy chương trình
if __name__ == "__main__":
    main()
```

---

✅ **Tổng kết bài học:**
- Lớp (class): khuôn mẫu để tạo đối tượng
- `__init__`: hàm khởi tạo, chạy khi tạo đối tượng
- `self`: tham chiếu đến đối tượng hiện tại
- Thuộc tính: lưu trữ dữ liệu
- Phương thức: hàm hành động của đối tượng

📌 **Bài tập về nhà:**  
Tạo lớp `Sach` với các thuộc tính: `ten_sach`, `tac_gia`, `nam_xuat_ban`.  
Viết phương thức `hien_thi()` để in thông tin sách. Tạo 2 đối tượng và hiển thị.
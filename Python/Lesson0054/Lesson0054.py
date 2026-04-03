"""
Bài học: Python 54 Cấp Cơ Bản - Chương trình tổng hợp kiến thức cơ bản
Tác giả: AI Tutor
Mô tả: Chương trình này giới thiệu 54 cấp độ kiến thức cơ bản Python thông qua
các ví dụ minh họa, comment tiếng Việt và bài tập nhỏ.
"""

def vidu_bien_va_kieu_du_lieu():
    """
    Ví dụ 1: Biến và Kiểu dữ liệu cơ bản
    """
    # Khai báo biến với các kiểu dữ liệu phổ biến
    ten = "Python"          # Chuỗi (string)
    tuoi = 5                # Số nguyên (int)
    chieu_cao = 1.5         # Số thực (float)
    la_hoc_vien = True      # Boolean (True/False)

    print("=== Ví dụ 1: Biến và Kiểu dữ liệu ===")
    print(f"Tên: {ten}, Kiểu: {type(ten)}")
    print(f"Tuổi: {tuoi}, Kiểu: {type(tuoi)}")
    print(f"Chiều cao: {chieu_cao}, Kiểu: {type(chieu_cao)}")
    print(f"Đang học: {la_hoc_vien}, Kiểu: {type(la_hoc_vien)}")


def vidu_cau_truc_dieu_kien():
    """
    Ví dụ 2: Câu lệnh điều kiện (if-elif-else)
    """
    diem = 85

    print("\n=== Ví dụ 2: Câu lệnh điều kiện ===")
    if diem >= 90:
        print("Xếp loại: Xuất sắc")
    elif diem >= 80:
        print("Xếp loại: Giỏi")
    elif diem >= 70:
        print("Xếp loại: Khá")
    else:
        print("Xếp loại: Cần cố gắng")


def vidu_vong_lap():
    """
    Ví dụ 3: Vòng lặp for và while
    """
    print("\n=== Ví dụ 3: Vòng lặp ===")

    # Dùng for để lặp qua danh sách
    danh_sach_mon_hoc = ["Toán", "Lý", "Hóa", "Sinh"]
    print("Danh sách môn học:")
    for mon in danh_sach_mon_hoc:
        print(f" - {mon}")

    # Dùng while để đếm ngược
    print("\nĐếm ngược từ 5:")
    dem = 5
    while dem > 0:
        print(f" {dem}...")
        dem -= 1
    print("Hết giờ!")


def bai_tap_nho():
    """
    Bài tập nhỏ: Tính tổng các số chẵn từ 1 đến 20
    Hướng dẫn: Dùng vòng lặp và điều kiện để kiểm tra số chẵn.
    """
    print("\n=== Bài tập nhỏ ===")
    print("Tính tổng các số chẵn từ 1 đến 20")

    tong = 0
    for i in range(1, 21):
        if i % 2 == 0:  # kiểm tra chẵn
            tong += i

    print(f"Tổng các số chẵn từ 1 đến 20 là: {tong}")

    # Gợi ý mở rộng: Thử viết bằng list comprehension
    tong_chẵn = sum([i for i in range(1, 21) if i % 2 == 0])
    print(f"(Dùng list comprehension: {tong_chẵn})")


def main():
    """
    Hàm chính chạy chương trình
    """
    print("📘 CHÀO MỪNG ĐẾN KHÓA HỌC: PYTHON 54 CẤP CƠ BẢN")
    print("=" * 50)

    # Hiển thị các ví dụ
    vidu_bien_va_kieu_du_lieu()
    vidu_cau_truc_dieu_kien()
    vidu_vong_lap()

    # Bài tập nhỏ
    bai_tap_nho()

    print("\n🎯 Chúc mừng bạn đã hoàn thành bài học cơ bản!")
    print("👉 Hãy thử sửa code và thêm ví dụ mới để luyện tập!")


# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()


"""
💡 Gợi ý tự học:
1. Thay đổi giá trị biến trong ví dụ 1 và xem kết quả.
2. Viết lại ví dụ 2 dùng dictionary để ánh xạ điểm -> xếp loại.
3. Tạo danh sách số và dùng vòng lặp tính trung bình.

📚 Tài liệu tham khảo:
- https://docs.python.org/3/tutorial/
- https://www.w3schools.com/python/
"""
```
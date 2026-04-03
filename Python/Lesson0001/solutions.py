# solutions.py
# Lời giải bài tập - Bài 1: Biến, kiểu dữ liệu, nhập xuất

# Bài 1: Chào hỏi với tên và tuổi
def bai1():
    ten = input("Nhập tên của bạn: ")
    tuoi = int(input("Nhập tuổi của bạn: "))
    print(f"Chào bạn {ten}, bạn {tuoi} tuổi. Rất vui được gặp bạn!")

# Bài 2: Tính diện tích hình chữ nhật
def bai2():
    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    dien_tich = chieu_dai * chieu_rong
    print(f"Diện tích hình chữ nhật là: {dien_tich}")

# Bài 3: Chuyển đổi km sang mét
def bai3():
    km = float(input("Nhập quãng đường (km): "))
    m = km * 1000  # 1 km = 1000 m
    print(f"{km} km = {m} mét")

# Bài 4: Tính điểm trung bình 3 môn
def bai4():
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    diem_tb = (toan + ly + hoa) / 3
    print(f"Điểm trung bình 3 môn là: {diem_tb:.2f}")

# Bài 5: Tính tuổi từ năm sinh
def bai5():
    nam_sinh = int(input("Nhập năm sinh: "))
    tuoi = 2025 - nam_sinh  # Giả sử hiện tại là năm 2025
    print(f"Bạn sinh năm {nam_sinh}, hiện bạn {tuoi} tuổi.")

# Gọi các hàm để chạy lời giải (bỏ comment để xem kết quả)
bai1()
bai2()
bai3()
bai4()
bai5()
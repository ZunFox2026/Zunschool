"""
Bài 20: Python Cơ bản
Mục tiêu: Giới thiệu các khái niệm cơ bản trong Python như biến, kiểu dữ liệu, vòng lặp, điều kiện, hàm và xử lý lỗi đơn giản.
"""

# 1. Biến và kiểu dữ liệu cơ bản
# Python tự động xác định kiểu dữ liệu khi gán giá trị
ten = "Nguyễn Văn A"       # Chuỗi (string)
tuoi = 20                   # Số nguyên (int)
chieu_cao = 1.75            # Số thực (float)
la_sinh_vien = True         # Boolean (True/False)

# In thông tin ra màn hình
print("=== Ví dụ 1: Biến và kiểu dữ liệu ===")
print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Chiều cao: {chieu_cao} m")
print(f"Là sinh viên: {la_sinh_vien}")

# 2. Câu điều kiện (if-elif-else)
print("\n=== Ví dụ 2: Câu điều kiện ===")
diem = 85

if diem >= 90:
    xep_loai = "Xuất sắc"
elif diem >= 80:
    xep_loai = "Giỏi"
elif diem >= 70:
    xep_loai = "Khá"
elif diem >= 50:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print(f"Điểm: {diem} → Xếp loại: {xep_loai}")

# 3. Vòng lặp for và while
print("\n=== Ví dụ 3: Vòng lặp for ===")
so_nguyen = [1, 2, 3, 4, 5]
tong = 0

for so in so_nguyen:
    tong += so
    print(f"Đang cộng: {so}")

print(f"Tổng các số: {tong}")

# Vòng lặp while
print("\n=== Ví dụ 4: Vòng lặp while ===")
dem = 0
while dem < 3:
    print(f"Lần lặp thứ: {dem + 1}")
    dem += 1

# 4. Hàm trong Python
def tinh_binh_phuong(x):
    """
    Hàm tính bình phương của một số
    :param x: số cần tính bình phương
    :return: bình phương của x
    """
    return x ** 2

def nhap_thong_tin_hoc_sinh():
    """
    Hàm nhập thông tin học sinh
    :return: tên và điểm số
    """
    ten = input("Nhập tên học sinh: ")
    diem = float(input("Nhập điểm: "))
    return ten, diem

# Sử dụng hàm
print("\n=== Ví dụ 5: Sử dụng hàm ===")
print(f"Bình phương của 7 là: {tinh_binh_phuong(7)}")

# 5. Xử lý lỗi cơ bản với try-except
print("\n=== Ví dụ 6: Xử lý lỗi ===")
try:
    so_a = int(input("Nhập số nguyên thứ nhất: "))
    so_b = int(input("Nhập số nguyên thứ hai: "))
    ket_qua = so_a / so_b
    print(f"Kết quả chia: {ket_qua}")
except ValueError:
    print("Lỗi: Vui lòng nhập đúng số nguyên!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except Exception as e:
    print(f"Lỗi không xác định: {e}")

# Bài tập nhỏ: Viết chương trình kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    """
    Hàm kiểm tra một số có phải là số nguyên tố không
    :param n: số nguyên dương
    :return: True nếu là số nguyên tố, False nếu không
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    """
    Hàm chính để chạy chương trình
    """
    print("\n" + "="*40)
    print("BÀI TẬP NHỎ: KIỂM TRA SỐ NGUYÊN TỐ")
    print("="*40)

    try:
        n = int(input("Nhập một số nguyên dương: "))
        if kiem_tra_so_nguyen_to(n):
            print(f"{n} là số nguyên tố.")
        else:
            print(f"{n} không phải là số nguyên tố.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

    # Thêm ví dụ kiểm tra một vài số
    print("\n--- Kiểm tra sẵn một vài số ---")
    cac_so = [2, 3, 4, 17, 25, 29]
    for so in cac_so:
        ket_qua = "có" if kiem_tra_so_nguyen_to(so) else "không"
        print(f"{so} {ket_qua} phải là số nguyên tố")

if __name__ == "__main__":
    main()
```
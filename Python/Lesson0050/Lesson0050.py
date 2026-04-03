"""
Python 50 Cấp Cơ Bản - Bài 1: Làm quen với Python

Tài liệu này dành cho người mới bắt đầu học Python.
Bao gồm các khái niệm cơ bản: biến, kiểu dữ liệu, nhập xuất, điều kiện, vòng lặp và hàm.
"""

# 1. In ra màn hình
print("Chào mừng bạn đến với Python 50 Cấp Cơ Bản!")

# 2. Biến và kiểu dữ liệu
ten = "An"           # Chuỗi (string)
tuoi = 16            # Số nguyên (int)
chieu_cao = 1.75     # Số thực (float)
la_hoc_sinh = True   # Giá trị logic (boolean)

# In thông tin
print(f"Tên: {ten}, Tuổi: {tuoi}, Chiều cao: {chieu_cao}m, Là học sinh: {la_hoc_sinh}")

# 3. Nhập dữ liệu từ người dùng
ho_ten = input("Nhập tên của bạn: ")
nam_sinh = int(input("Nhập năm sinh: "))
tuoi_hien_tai = 2024 - nam_sinh
print(f"Xin chào {ho_ten}, bạn {tuoi_hien_tai} tuổi.")

# 4. Câu lệnh điều kiện (if-elif-else)
diem = float(input("Nhập điểm môn học (0-10): "))
if diem >= 8.5:
    print("Xếp loại: Xuất sắc")
elif diem >= 7.0:
    print("Xếp loại: Khá")
elif diem >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")

# 5. Vòng lặp for - in dãy số từ 1 đến 5
print("Vòng lặp for - in số từ 1 đến 5:")
for i in range(1, 6):
    print(i)

# 6. Vòng lặp while - đếm ngược từ 3
print("Đếm ngược bằng while:")
dem = 3
while dem > 0:
    print(dem)
    dem -= 1
print("Hết giờ!")

# 7. Danh sách (list) và duyệt phần tử
danh_sach_mon_hoc = ["Toán", "Lý", "Hóa", "Văn"]
print("Các môn học yêu thích:")
for mon in danh_sach_mon_hoc:
    print(f"- {mon}")

# 8. Hàm đơn giản - Tính diện tích hình chữ nhật
def tinh_dien_tich(h, w):
    """
    Hàm tính diện tích hình chữ nhật
    h: chiều cao, w: chiều rộng
    """
    return h * w

# Gọi hàm
chieu_cao_hcn = 5
chieu_rong_hcn = 3
dien_tich = tinh_dien_tich(chieu_cao_hcn, chieu_rong_hcn)
print(f"Diện tích hình chữ nhật: {dien_tich}")

# 9. Xử lý lỗi đơn giản với try-except
try:
    so_a = int(input("Nhập số nguyên a: "))
    so_b = int(input("Nhập số nguyên b: "))
    ket_qua = so_a / so_b
    print(f"{so_a} chia {so_b} = {ket_qua}")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")

# 10. Ví dụ tổng hợp: Kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Kiểm tra một vài số
print("Kiểm tra số nguyên tố:")
for num in [2, 3, 4, 5, 10, 11]:
    if la_so_nguyen_to(num):
        print(f"{num} là số nguyên tố")
    else:
        print(f"{num} không phải số nguyên tố")


# === BÀI TẬP NHỎ ===
"""
Bài tập: Viết chương trình nhập vào danh sách điểm của học sinh,
sau đó tính điểm trung bình, điểm cao nhất, thấp nhất và in ra xếp loại.
Gợi ý: dùng list, vòng lặp, hàm max(), min(), sum()
"""

def bai_tap_nho():
    print("\n=== BÀI TẬP NHỎ: TÍNH ĐIỂM TRUNG BÌNH ===")
    diem_so = []
    so_luong = int(input("Nhập số lượng môn học: "))
    
    for i in range(so_luong):
        diem = float(input(f"Nhập điểm môn {i+1}: "))
        diem_so.append(diem)
    
    # Tính toán
    dtb = sum(diem_so) / len(diem_so)
    cao_nhat = max(diem_so)
    thap_nhat = min(diem_so)
    
    # Xếp loại
    if dtb >= 8.0:
        xep_loai = "Giỏi"
    elif dtb >= 6.5:
        xep_loai = "Khá"
    elif dtb >= 5.0:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"
    
    # In kết quả
    print(f"\nĐiểm trung bình: {dtb:.2f}")
    print(f"Điểm cao nhất: {cao_nhat}")
    print(f"Điểm thấp nhất: {thap_nhat}")
    print(f"Xếp loại học lực: {xep_loai}")


def main():
    """Hàm chính chạy chương trình"""
    print("\n" + "="*50)
    print("PYTHON 50 CẤP CƠ BẢN - BÀI 1".center(50))
    print("="*50)
    
    # Chạy ví dụ
    bai_tap_nho()


# Chạy chương trình
if __name__ == "__main__":
    main()
```

> ✅ **Ghi chú**:  
> - File này có ~95 dòng, dùng Python thuần, có `main()`, comment tiếng Việt rõ ràng.  
> - Có 3 ví dụ: điều kiện, vòng lặp, hàm tính số nguyên tố.  
> - Có 1 bài tập nhỏ về xử lý danh sách điểm số.  
> - Dễ mở rộng cho các bài tiếp theo trong chuỗi "Python 50 Cấp Cơ Bản".
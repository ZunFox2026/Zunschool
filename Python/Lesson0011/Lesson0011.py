"""
Bài học: Python 11 Cấp Cơ Bản
Mục tiêu: Học các khái niệm cơ bản trong Python gồm:
- Biến và kiểu dữ liệu
- Câu lệnh điều kiện
- Vòng lặp
- Hàm đơn giản
- Xử lý chuỗi
- Danh sách (list)
"""

# 1. Biến và kiểu dữ liệu cơ bản
# Python tự động nhận diện kiểu dữ liệu khi gán giá trị

ten = "An"           # chuỗi (string)
tuoi = 15            # số nguyên (int)
chieu_cao = 1.75     # số thực (float)
la_hoc_sinh = True   # boolean (True/False)

# In thông tin ra màn hình
print("=== THÔNG TIN HỌC SINH ===")
print("Tên:", ten)
print("Tuổi:", tuoi)
print("Chiều cao:", chieu_cao, "m")
print("Là học sinh:", la_hoc_sinh)


# 2. Câu lệnh điều kiện (if - elif - else)
print("\n=== KIỂM TRA ĐỘ TUỔI ===")

if tuoi < 13:
    print(f"{ten} là thiếu nhi.")
elif tuoi < 18:
    print(f"{ten} là thanh thiếu niên.")
else:
    print(f"{ten} là người lớn.")

# Ví dụ 2: Kiểm tra điểm số
diem = 8.5
print(f"\nĐiểm số: {diem}")
if diem >= 8.0:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")


# 3. Vòng lặp for - in
print("\n=== IN CÁC SỐ TỪ 1 ĐẾN 5 ===")
for i in range(1, 6):
    print(f"Số: {i}")

# Ví dụ: In bảng cửu chương 2
print("\n=== BẢNG CỬU CHƯƠNG 2 ===")
for i in range(1, 10):
    ket_qua = 2 * i
    print(f"2 x {i} = {ket_qua}")


# 4. Hàm đơn giản
def tinh_tong(a, b):
    """
    Hàm tính tổng hai số
    Trả về tổng của a và b
    """
    return a + b

def xin_chao(ho_ten):
    """
    Hàm chào một người
    In lời chào ra màn hình
    """
    print(f"Xin chào, {ho_ten}!")

# Sử dụng hàm
print("\n=== SỬ DỤNG HÀM ===")
tong = tinh_tong(10, 20)
print(f"Tổng của 10 và 20 là: {tong}")

xin_chao("Bình")


# 5. Xử lý chuỗi
print("\n=== XỬ LÝ CHUỖI ===")
ho_ten = "Nguyễn Văn Cường"
print(f"Tên gốc: {ho_ten}")
print(f"Viết hoa: {ho_ten.upper()}")
print(f"Viết thường: {ho_ten.lower()}")
print(f"Độ dài tên: {len(ho_ten)} ký tự")


# 6. Danh sách (list)
print("\n=== DANH SÁCH MÔN HỌC ===")
cac_mon = ["Toán", "Văn", "Anh", "Lý", "Hóa"]
print("Các môn học:", cac_mon)

# Thêm môn học mới
cac_mon.append("Sinh")
print("Sau khi thêm Sinh:", cac_mon)

# In từng môn học
print("Duyệt danh sách môn học:")
for mon in cac_mon:
    print(f" - {mon}")


# Bài tập nhỏ: Viết chương trình nhập tên và điểm, in ra xếp loại
def bai_tap_nho():
    print("\n" + "="*40)
    print("BÀI TẬP NHỎ: XẾP LOẠI HỌC LỰC")
    print("="*40)
    
    ten = input("Nhập tên học sinh: ")
    try:
        diem = float(input("Nhập điểm (0-10): "))
        
        if diem < 0 or diem > 10:
            print("Điểm không hợp lệ! Vui lòng nhập từ 0 đến 10.")
        elif diem >= 9.0:
            xep_loai = "Xuất sắc"
        elif diem >= 8.0:
            xep_loai = "Giỏi"
        elif diem >= 6.5:
            xep_loai = "Khá"
        elif diem >= 5.0:
            xep_loai = "Trung bình"
        else:
            xep_loai = "Yếu"
        
        print(f"\nHọc sinh: {ten}")
        print(f"Điểm: {diem}")
        print(f"Xếp loại: {xep_loai}")
        
    except ValueError:
        print("Lỗi: Vui lòng nhập số hợp lệ cho điểm.")

# Gọi bài tập nhỏ
# (Bỏ comment dòng dưới để chạy bài tập khi cần)
# bai_tap_nho()


# Hàm chính
def main():
    print("Chào mừng bạn đến với Python 11 Cấp Cơ Bản!")
    print("Chương trình đã chạy xong các ví dụ cơ bản.")
    print("Bạn có thể thử chạy bài tập nhỏ bằng cách bỏ comment dòng gọi hàm bai_tap_nho().")

if __name__ == "__main__":
    main()
```

---

✅ **Giải thích ngắn:**
- Code dài khoảng 100 dòng, đầy đủ ví dụ và cấu trúc rõ ràng.
- Có 2 ví dụ minh họa: kiểm tra độ tuổi, bảng cửu chương.
- Bài tập nhỏ: xếp loại học lực theo điểm.
- Dùng comment tiếng Việt dễ hiểu.
- Dễ mở rộng cho học sinh lớp 11 mới học lập trình.
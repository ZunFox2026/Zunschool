# solutions.py - Lời giải bài tập: Cấu trúc rẽ nhánh

# Bài 1: Phân loại theo độ tuổi
print("=== Bài 1: Phân loại theo độ tuổi ===")
tuoi = int(input("Nhập tuổi của bạn: "))
if tuoi < 13:
    print("Bạn là trẻ em.")
elif tuoi < 18:  # tuoi >= 13 và < 18
    print("Bạn là thiếu niên.")
else:
    print("Bạn là người lớn.")
print()

# Bài 2: Xếp loại học lực dựa trên điểm trung bình
print("=== Bài 2: Xếp loại học lực ===")
diem_toan = float(input("Nhập điểm Toán: "))
diem_ly = float(input("Nhập điểm Lý: "))
diem_hoa = float(input("Nhập điểm Hóa: "))

# Tính điểm trung bình
dtb = (diem_toan + diem_ly + diem_hoa) / 3

if dtb >= 8.0:
    xep_loai = "Giỏi"
elif dtb >= 6.5:
    xep_loai = "Khá"
elif dtb >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print(f"Điểm trung bình: {dtb:.2f}")
print(f"Xếp loại: {xep_loai}")
print()

# Bài 3: Máy bán hàng tự động
print("=== Bài 3: Máy bán hàng tự động ===")
lua_chon = int(input("Chọn đồ uống (1: Coca, 2: Pepsi, 3: Nước): "))
if lua_chon == 1 or lua_chon == 2:
    print("Đồ uống có gas.")
elif lua_chon == 3:
    print("Đồ uống không gas.")
else:
    print("Lựa chọn không hợp lệ.")
print()

# Bài 4: Kiểm tra năm nhuận
print("=== Bài 4: Kiểm tra năm nhuận ===")
nam = int(input("Nhập năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")
print()

# Bài 5: Kiểm tra chia hết cho 3 và 5
print("=== Bài 5: Kiểm tra chia hết cho 3 và 5 ===")
so = int(input("Nhập một số nguyên: "))

chia_het_3 = (so % 3 == 0)
chia_het_5 = (so % 5 == 0)

if chia_het_3 and chia_het_5:
    print("Chia hết cho cả 3 và 5")
elif chia_het_3:
    print("Chia hết cho 3")
elif chia_het_5:
    print("Chia hết cho 5")
else:
    print("Không chia hết cho 3 hoặc 5")
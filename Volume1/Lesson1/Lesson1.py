
---

## 🐍 Volume1/Lesson1/Lesson1.py

```python
# ================================
# Bài 1: Biến, kiểu dữ liệu và nhập xuất
# Học cùng Zunny 🦊
# ================================

print("=== BÀI 1: LÀM QUEN VỚI PYTHON ===\n")

# ---------- 1. Khai báo biến và in ----------
ten = "Zunny"
tuoi = 3
diem_python = 9.5
hoc_sinh_gioi = True

print("Tên:", ten)
print("Tuổi:", tuoi)
print("Điểm Python:", diem_python)
print("Học sinh giỏi:", hoc_sinh_gioi)
print()

# ---------- 2. Kiểu dữ liệu ----------
a = 10          # int
b = 3.14        # float
c = "Hello"     # str
d = False       # bool

print("Kiểu của a:", type(a))
print("Kiểu của b:", type(b))
print("Kiểu của c:", type(c))
print("Kiểu của d:", type(d))
print()

# ---------- 3. Nhập dữ liệu từ bàn phím ----------
# input() luôn trả về str, cần ép kiểu nếu muốn số
name = input("Nhập tên của bạn: ")
age = int(input("Nhập tuổi của bạn: "))
print(f"Xin chào {name}, bạn {age} tuổi.\n")

# ---------- 4. Ép kiểu ----------
so_thap_phan = float(input("Nhập một số thập phân: "))
so_nguyen = int(so_thap_phan)   # cắt phần thập phân
print(f"Số thập phân: {so_thap_phan}")
print(f"Số nguyên sau khi ép: {so_nguyen}\n")

# ---------- 5. Tính toán cơ bản ----------
x = 15
y = 4
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")       # luôn trả về float
print(f"{x} // {y} = {x // y}")     # chia lấy phần nguyên
print(f"{x} % {y} = {x % y}")       # chia lấy phần dư
print(f"{x} ** {y} = {x ** y}")     # lũy thừa
print()

# ---------- 6. Nhập cạnh hình vuông ----------
canh = float(input("Nhập cạnh hình vuông: "))
chuvi = canh * 4
dientich = canh ** 2
print(f"Chu vi hình vuông: {chuvi}")
print(f"Diện tích hình vuông: {dientich}\n")

# ---------- 7. Nhập 2 số, tính tổng, hiệu, tích, thương ----------
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))
print(f"Tổng: {so1 + so2}")
print(f"Hiệu: {so1 - so2}")
print(f"Tích: {so1 * so2}")
if so2 != 0:
    print(f"Thương: {so1 / so2:.2f}")
else:
    print("Không thể chia cho 0")
print()

# ---------- 8. Đổi độ C sang độ F ----------
do_c = float(input("Nhập nhiệt độ (°C): "))
do_f = do_c * 9/5 + 32
print(f"{do_c}°C = {do_f:.2f}°F\n")

# ---------- 9. Đổi giây sang giờ:phút:giây ----------
tong_giay = int(input("Nhập số giây: "))
gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60
print(f"{tong_giay} giây = {gio} giờ {phut} phút {giay} giây\n")

# ---------- 10. Nhập tên và tuổi (nâng cao) ----------
ho_ten = input("Nhập họ và tên: ")
nam_sinh = int(input("Nhập năm sinh: "))
nam_hien_tai = 2026
tuoi_hien_tai = nam_hien_tai - nam_sinh
print(f"Chào {ho_ten}, năm nay bạn {tuoi_hien_tai} tuổi.\n")

# ---------- 11. Tính chu vi, diện tích hình tròn ----------
ban_kinh = float(input("Nhập bán kính hình tròn: "))
pi = 3.14159
chu_vi_tron = 2 * pi * ban_kinh
dien_tich_tron = pi * ban_kinh ** 2
print(f"Chu vi hình tròn: {chu_vi_tron:.2f}")
print(f"Diện tích hình tròn: {dien_tich_tron:.2f}\n")

# ---------- 12. Đổi tiền (USD -> VND) --------->
ty_gia = 25500
usd = float(input("Nhập số USD: "))
vnd = usd * ty_gia
print(f"{usd} USD = {vnd:,.0f} VND\n")

# ---------- 13. Tính trung bình cộng 3 số ----------
a1 = float(input("Số thứ 1: "))
a2 = float(input("Số thứ 2: "))
a3 = float(input("Số thứ 3: "))
tbc = (a1 + a2 + a3) / 3
print(f"Trung bình cộng: {tbc:.2f}\n")

# ---------- 14. Kiểm tra số chẵn lẻ (dùng if – giới thiệu) ----------
so_kiem_tra = int(input("Nhập một số nguyên: "))
if so_kiem_tra % 2 == 0:
    print(f"{so_kiem_tra} là số chẵn")
else:
    print(f"{so_kiem_tra} là số lẻ")
print()

# ---------- 15. Bài tập tổng hợp ----------
print("=== BÀI TẬP THỰC HÀNH ===")
# Bài 1: Tính tuổi khi biết năm sinh
ns = int(input("Nhập năm sinh: "))
nam_hien_tai2 = 2026
print(f"Tuổi của bạn: {nam_hien_tai2 - ns}")

# Bài 2: Tính diện tích tam giác vuông
day = float(input("Nhập độ dài đáy tam giác: "))
cao = float(input("Nhập chiều cao: "))
print(f"Diện tích tam giác: {0.5 * day * cao}")

# Bài 3: Nhập chuỗi và in ra độ dài
chuoi = input("Nhập một chuỗi bất kỳ: ")
print(f"Độ dài chuỗi: {len(chuoi)}")

print("\n🦊 Kết thúc Bài 1. Hãy thực hành lại các ví dụ trên!")

import math
import random

# Ví dụ 1: Xử lý chia cho 0 và nhập liệu
print("=== Ví dụ 1: Xử lý chia cho 0 ===")
try:
    a = int(input("Nhập số bị chia: "))
    b = int(input("Nhập số chia: "))
    ket_qua = a / b
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")
else:
    print(f"Kết quả: {ket_qua}")
finally:
    print("Chương trình kết thúc.\n")

# Ví dụ 2: Đọc file an toàn
print("=== Ví dụ 2: Đọc file an toàn ===")
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        noi_dung = f.read()
        print("Nội dung file:")
        print(noi_dung)
except FileNotFoundError:
    print("Lỗi: File 'data.txt' không tồn tại.")
except PermissionError:
    print("Lỗi: Không có quyền truy cập file.")
except Exception as e:
    print(f"Lỗi không xác định: {e}")
else:
    print("Đọc file thành công.")
finally:
    print("Hoàn tất thao tác đọc file.\n")

# Ví dụ 3: Xử lý nhập liệu tuổi
print("=== Ví dụ 3: Xử lý nhập liệu tuổi ===")
def nhap_tuoi():
    while True:
        try:
            tuoi = int(input("Nhập tuổi của bạn: "))
            if tuoi < 0:
                # Tạo lỗi tùy chỉnh nếu tuổi âm
                raise ValueError("Tuổi không thể âm.")
            break
        except ValueError as e:
            print(f"Lỗi: {e}. Vui lòng nhập lại.")
    print(f"Tuổi của bạn là: {tuoi}")

nhap_tuoi()

# Ví dụ 4: Tính căn bậc hai với xử lý ngoại lệ
print("\n=== Ví dụ 4: Tính căn bậc hai ===")
def tinh_can_bac_hai(x):
    try:
        if x < 0:
            raise ValueError("Không thể tính căn bậc hai của số âm.")
        return math.sqrt(x)
    except ValueError as e:
        print(f"Lỗi: {e}")
        return None

# Thử nghiệm
print(tinh_can_bac_hai(16))  # 4.0
print(tinh_can_bac_hai(-4))  # Lỗi
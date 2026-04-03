# main.py - Bài học 8: Lỗi và ngoại lệ (try-except)

# --- Ví dụ 1: Xử lý nhập số nguyên ---
print("=== Ví dụ 1: Nhập số nguyên ===")
try:
    so = int(input("Nhập một số nguyên: "))
    print(f"Bạn đã nhập: {so}")
except ValueError:
    print("Lỗi: Bạn phải nhập một số nguyên!")

# --- Ví dụ 2: Chia hai số an toàn ---
print("\n=== Ví dụ 2: Chia hai số ===")
try:
    a = float(input("Nhập số bị chia: "))
    b = float(input("Nhập số chia: "))
    ket_qua = a / b
    print(f"Kết quả: {ket_qua}")
except ZeroDivisionError:
    print("Không thể chia cho 0!")
except ValueError:
    print("Bạn phải nhập số hợp lệ!")

# --- Ví dụ 3: Truy cập danh sách an toàn ---
print("\n=== Ví dụ 3: Truy cập danh sách ===")
danh_sach = [10, 20, 30]
try:
    chi_so = int(input("Nhập chỉ số muốn truy cập (0-2): "))
    print(f"Giá trị tại vị trí {chi_so}: {danh_sach[chi_so]}")
except IndexError:
    print("Chỉ số vượt quá danh sách!")
except ValueError:
    print("Bạn phải nhập một số nguyên!")

# --- Ví dụ 4: Dùng else và finally ---
print("\n=== Ví dụ 4: Dùng else và finally ===")
try:
    x = int(input("Nhập một số dương: "))
    if x <= 0:
        raise ValueError("Số phải lớn hơn 0")
    print(f"Bạn đã nhập số hợp lệ: {x}")
except ValueError as e:
    print(f"Lỗi: {e}")
else:
    print("Không có lỗi xảy ra!")
finally:
    print("Khối finally luôn được thực thi.")
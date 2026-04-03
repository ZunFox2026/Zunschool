### Bài học Python số 36: Xử lý ngoại lệ nâng cao

# Ví dụ 1: Sử dụng try, except, else, finally khi chia hai số

def chia_hai_so(a, b):
    try:
        ket_qua = a / b
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0")
        return None
    except TypeError:
        print("Lỗi: Đầu vào phải là số")
        return None
    else:
        print(f"Kết quả chia là: {ket_qua}")
        return ket_qua
    finally:
        print("Hoàn thành quá trình chia.")

# Chạy thử ví dụ 1
print("=== Ví dụ 1: Chia hai số ===")
chia_hai_so(10, 2)
chia_hai_so(10, 0)
chia_hai_so(10, "abc")

# Ví dụ 2: Đọc file với xử lý ngoại lệ và finally để đóng file

def doc_file_an_toan(ten_file):
    file = None
    try:
        file = open(ten_file, 'r', encoding='utf-8')
        noi_dung = file.read()
        print("Đã đọc file thành công:")
        print(noi_dung)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print("Không có lỗi xảy ra khi đọc file.")
    finally:
        if file is not None and not file.closed:
            file.close()
            print("File đã được đóng an toàn.")

# Tạo file tạm để kiểm thử
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Xin chào từ file test!")

print("\n=== Ví dụ 2: Đọc file an toàn ===")
doc_file_an_toan("test.txt")
doc_file_an_toan("khong_ton_tai.txt")

# Ví dụ 3: Sử dụng raise để kiểm tra dữ liệu đầu vào

def tinh_can_bac_hai(x):
    if x < 0:
        raise ValueError("Không thể tính căn bậc hai của số âm")
    import math
    return math.sqrt(x)

print("\n=== Ví dụ 3: Dùng raise để phát sinh lỗi ===")
try:
    print(tinh_can_bac_hai(9))
    print(tinh_can_bac_hai(-4))
except ValueError as e:
    print(f"Lỗi: {e}")

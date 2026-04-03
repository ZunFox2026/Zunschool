### BÀI TẬP 1: Chia hai số với kiểm tra lỗi

def chia_hai_so(a, b):
    # Kiểm tra kiểu dữ liệu
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Cả hai tham số phải là số (int hoặc float)")
    if b == 0:
        raise ZeroDivisionError("Không thể chia cho số 0")
    return a / b

# Kiểm thử
try:
    print(chia_hai_so(10, 2))   # 5.0
    print(chia_hai_so(10, 0))   # Lỗi ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    print(f"Lỗi: {e}")

try:
    print(chia_hai_so("abc", 2))  # Lỗi ValueError
except (ValueError, ZeroDivisionError) as e:
    print(f"Lỗi: {e}")


### BÀI TẬP 2: Kiểm tra số điện thoại

class SoDienThoaiSaiDinhDangError(Exception):
    """Ngoại lệ khi số điện thoại sai định dạng"""
    def __init__(self, sdt, message="Số điện thoại không hợp lệ"):
        self.sdt = sdt
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.sdt}"

def kiem_tra_so_dien_thoai(sdt):
    # Chuyển về chuỗi để xử lý
    sdt_str = str(sdt)
    
    # Kiểm tra độ dài
    if len(sdt_str) != 10:
        raise SoDienThoaiSaiDinhDangError(sdt, "Số điện thoại phải có đúng 10 chữ số")
    
    # Kiểm tra chữ số đầu
    if not sdt_str.startswith('0'):
        raise SoDienThoaiSaiDinhDangError(sdt, "Số điện thoại phải bắt đầu bằng '0'")
    
    # Kiểm tra tất cả ký tự là số
    if not sdt_str.isdigit():
        raise SoDienThoaiSaiDinhDangError(sdt, "Số điện thoại chỉ được chứa các chữ số")
    
    return True

# Kiểm thử
try:
    kiem_tra_so_dien_thoai("0901234567")
    print("Số điện thoại hợp lệ")
except SoDienThoaiSaiDinhDangError as e:
    print(e)

try:
    kiem_tra_so_dien_thoai("9901234567")  # Không bắt đầu bằng 0
except SoDienThoaiSaiDinhDangError as e:
    print(e)

try:
    kiem_tra_so_dien_thoai("abc")  # Không phải số
except SoDienThoaiSaiDinhDangError as e:
    print(e)


### BÀI TẬP 3: Đọc file với finally

def doc_file(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
            print("Nội dung file:")
            print(noi_dung)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'")
    except Exception as e:
        print(f"Lỗi không xác định khi đọc file: {e}")
    finally:
        print("Hoàn tất việc đọc file.")

# Kiểm thử (giả sử file không tồn tại)
doc_file("file_khong_ton_tai.txt")
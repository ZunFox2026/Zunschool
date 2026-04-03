## Bài học Python số 30: Xử lý ngoại lệ và tự định nghĩa Exception

# --- Ví dụ 1: Xử lý lỗi nhập số ---

# Chương trình yêu cầu người dùng nhập số nguyên

print("--- Ví dụ 1: Nhập số nguyên an toàn ---")

while True:
    try:
        n = int(input("Nhập một số nguyên: "))
        print(f"Bạn đã nhập: {n}")
        break  # Thoát vòng lặp nếu nhập đúng
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    except KeyboardInterrupt:
        print("\nNgười dùng đã hủy nhập.")
        break

# --- Ví dụ 2: Đọc file an toàn ---

print("\n--- Ví dụ 2: Đọc file an toàn ---")

filename = "data.txt"

def doc_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print("Nội dung file:")
            print(content)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{filename}'")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print("Đọc file thành công!")
    finally:
        print("Hoàn tất thao tác đọc file.")

doc_file(filename)

# --- Ví dụ 3: Tự định nghĩa ngoại lệ ---

print("\n--- Ví dụ 3: Tự định nghĩa ngoại lệ cho ngân hàng ---")

class SoDuKhongDuError(Exception):
    """Ngoại lệ khi số dư tài khoản không đủ để rút tiền"""
    def __init__(self, so_du, so_tien_rut):
        self.so_du = so_du
        self.so_tien_rut = so_tien_rut
        super().__init__(f"Số dư không đủ: cần {so_tien_rut}, hiện có {so_du}")

class TaiKhoanNganHang:
    def __init__(self, so_du):
        self.so_du = so_du

    def rut_tien(self, so_tien):
        try:
            if so_tien <= 0:
                raise ValueError("Số tiền rút phải lớn hơn 0")
            if so_tien > self.so_du:
                raise SoDuKhongDuError(self.so_du, so_tien)
            self.so_du -= so_tien
            print(f"Rút tiền thành công! Số dư còn lại: {self.so_du}")
        except SoDuKhongDuError as e:
            print(f"Lỗi rút tiền: {e}")
        except ValueError as e:
            print(f"Lỗi giá trị: {e}")

# Sử dụng
tk = TaiKhoanNganHang(1000000)
tk.rut_tien(500000)  # Thành công
tk.rut_tien(700000)  # Lỗi: số dư không đủ
tk.rut_tien(-100000)  # Lỗi: số tiền âm
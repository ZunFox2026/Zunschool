# main.py - Bài học 25: Xử lý ngoại lệ nâng cao

# --- Ví dụ 1: Bắt nhiều loại ngoại lệ riêng biệt ---
print("=== Ví dụ 1: Xử lý lỗi chia cho 0 và kiểu dữ liệu sai ===")

def chia_hai_so():
    try:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        ket_qua = a / b
        print(f"Kết quả: {a} / {b} = {ket_qua}")
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số hợp lệ!")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
    else:
        print("Phép chia thành công!")
    finally:
        print("--- Hoàn tất xử lý ---")

# Gọi hàm (bạn có thể nhập thử: a=10, b=0 hoặc a=abc)
# chia_hai_so()  # Bỏ comment để thử


# --- Ví dụ 2: Đọc file an toàn với xử lý ngoại lệ ---
print("\n=== Ví dụ 2: Đọc file với xử lý lỗi ===")

def doc_file_an_toan(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
            print(f"Nội dung file {ten_file}:")
            print(noi_dung)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'!")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'!")
    except Exception as e:
        print(f"Lỗi không xác định khi đọc file: {e}")
    else:
        print("Đọc file thành công!")
    finally:
        print("Hoạt động đọc file đã kết thúc.")

# Tạo file mẫu để thử (nếu chưa có)
with open("du_lieu.txt", "w", encoding="utf-8") as f:
    f.write("Xin chào, đây là dữ liệu thử nghiệm!\nDòng thứ hai.")

# Gọi hàm đọc file
# doc_file_an_toan("du_lieu.txt")      # Thành công
# doc_file_an_toan("khong_ton_tai.txt") # Lỗi FileNotFoundError


# --- Ví dụ 3: Tạo và sử dụng ngoại lệ tùy chỉnh ---
print("\n=== Ví dụ 3: Ngoại lệ tùy chỉnh ===")

class TuoiKhongHopLeError(Exception):
    """Lớp ngoại lệ tùy chỉnh khi tuổi không hợp lệ"""
    def __init__(self, tuoi, tin_nhan="Tuổi phải nằm trong khoảng 0 đến 120"):
        self.tuoi = tuoi
        self.tin_nhan = tin_nhan
        super().__init__(self.tin_nhan)

    def __str__(self):
        return f"TuoiKhongHopLeError: {self.tin_nhan} (tuổi nhập: {self.tuoi})"

def kiem_tra_tuoi(tuoi):
    try:
        tuoi = int(tuoi)
        if tuoi < 0 or tuoi > 120:
            raise TuoiKhongHopLeError(tuoi)
        print(f"Tuổi hợp lệ: {tuoi} tuổi")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên!")
    except TuoiKhongHopLeError as e:
        print(e)  # In chi tiết lỗi tùy chỉnh
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

# Thử các trường hợp
kiem_tra_tuoi(25)     # Hợp lệ
kiem_tra_tuoi(-5)     # Lỗi tùy chỉnh
kiem_tra_tuoi("abc")  # Lỗi ValueError

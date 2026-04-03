import math
import json

# Bài tập 1: Hàm chia hai số
def chia_hai_so(a, b):
    try:
        ket_qua = a / b
        return ket_qua
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
        return None

# Bài tập 2: Đọc file data.txt
def doc_file_data():
    try:
        with open("data.txt", "r", encoding="utf-8") as f:
            noi_dung = f.read()
            print("Nội dung file:")
            print(noi_dung)
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file 'data.txt'!")
    except Exception as e:
        print(f"Lỗi khác: {e}")

# Bài tập 3: Tính căn bậc hai
def tinh_can_bac_hai(x):
    try:
        if x < 0:
            raise ValueError("Không thể tính căn bậc hai của số âm!")
        return math.sqrt(x)
    except ValueError as ve:
        print(f"Lỗi: {ve}")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None

# Bài tập 4: Nhập danh sách số từ người dùng
def nhap_danh_sach_so():
    try:
        nhap = input("Nhập các số, cách nhau bởi dấu phẩy: ")
        chuoi_so = nhap.split(",")
        danh_sach = []
        
        for chuoi in chuoi_so:
            try:
                so = float(chuoi.strip())
                danh_sach.append(so)
            except ValueError:
                print(f"'{chuoi.strip()}' không phải là số, bỏ qua.")
        
        print("Danh sách số hợp lệ:", danh_sach)
        return danh_sach
        
    except Exception as e:
        print(f"Lỗi khi xử lý nhập liệu: {e}")
        return []

# Bài tập 5: Đọc file JSON
def doc_du_lieu_json(ten_file):
    try:
        with open(ten_file, "r", encoding="utf-8") as f:
            du_lieu = json.load(f)
            return du_lieu
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'!")
    except json.JSONDecodeError as jde:
        print(f"Lỗi: File không phải định dạng JSON hợp lệ - {jde}")
    except Exception as e:
        print(f"Lỗi khác khi đọc file: {e}")
    return None
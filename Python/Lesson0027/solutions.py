# solutions.py
# Lời giải bài tập - Bài 27: Xử lý ngoại lệ

# Bài 1: Viết hàm chia hai số, xử lý chia cho 0
def chia_hai_so(a, b):
    try:
        ket_qua = a / b
        return ket_qua
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
        return None

# Bài 2: Nhập danh sách số từ người dùng
def nhap_danh_sach_so():
    danh_sach = []
    try:
        so_luong = int(input("Nhập số lượng phần tử: "))
    except ValueError:
        print("Lỗi: Số lượng phải là một số nguyên!")
        return []

    for i in range(so_luong):
        while True:
            try:
                so = float(input(f"Nhập số thứ {i+1}: "))
                danh_sach.append(so)
                break  # Thoát vòng lặp nếu nhập đúng
            except ValueError:
                print("Vui lòng nhập một số hợp lệ!")
    return danh_sach

# Bài 3: Đọc file và in nội dung
def doc_file_in_noi_dung(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
            print("Nội dung file:")
            print(noi_dung)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'!")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
    finally:
        print("Hoàn tất thao tác đọc file.")

# Bài 4: Tính căn bậc hai
import math
def tinh_can_bac_hai(x):
    try:
        if x < 0:
            raise ValueError("Không thể tính căn bậc hai của số âm!")
        return math.sqrt(x)
    except ValueError as e:
        print(f"Lỗi: {e}")
        return None

# Bài 5: Truy cập phần tử trong danh sách
def truy_cap_phan_tu(danh_sach, chi_so):
    try:
        # Chuyển chi_so thành số nguyên nếu cần
        chi_so = int(chi_so)
        print(f"Giá trị tại vị trí {chi_so}: {danh_sach[chi_so]}")
    except ValueError:
        print("Lỗi: Chỉ số phải là một số nguyên!")
    except IndexError:
        print("Lỗi: Chỉ số vượt quá kích thước danh sách!")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
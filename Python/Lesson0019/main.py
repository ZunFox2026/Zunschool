# main.py - Bài học 19: Xử lý ngoại lệ

# Ví dụ 1: Đọc file an toàn
def doc_file_an_toan(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
            print("Nội dung file:")
            print(noi_dung)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'")
    except PermissionError:
        print(f"Lỗi: Không có quyền truy cập file '{ten_file}'")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print("Đọc file thành công!")
    finally:
        print("Hoàn tất thao tác đọc file.")

# Gọi hàm (giả sử file khong_ton_tai.txt không có)
doc_file_an_toan("khong_ton_tai.txt")

print("-" * 40)

# Ví dụ 2: Tính trung bình điểm số
def tinh_trung_binh(danh_sach_diem):
    try:
        # Kiểm tra danh sách có rỗng không
        if len(danh_sach_diem) == 0:
            raise ValueError("Danh sách điểm rỗng!")
        
        tong = sum(danh_sach_diem)
        trung_binh = tong / len(danh_sach_diem)
        return trung_binh
    except TypeError:
        print("Lỗi: Danh sách chứa phần tử không phải số!")
        return None
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None

# Thử với các dữ liệu khác nhau
diem_hop_le = [8.5, 9.0, 7.5, 10.0]
diem_rong = []
diem_sai_kieu = [8, 9, "abc", 7]

print(f"Trung bình điểm hợp lệ: {tinh_trung_binh(diem_hop_le)}")
print(f"Trung bình điểm rỗng: {tinh_trung_binh(diem_rong)}")
print(f"Trung bình điểm sai kiểu: {tinh_trung_binh(diem_sai_kieu)}")

print("-" * 40)

# Ví dụ 3: Mô phỏng rút tiền tại ATM
def rut_tien(so_du, so_tien_rut):
    try:
        # Chuyển sang số thực để đảm bảo
        so_du = float(so_du)
        so_tien_rut = float(so_tien_rut)
        
        if so_tien_rut <= 0:
            raise ValueError("Số tiền rút phải lớn hơn 0.")
        
        if so_tien_rut > so_du:
            raise ValueError("Số dư không đủ để thực hiện giao dịch.")
        
        so_du_con_lai = so_du - so_tien_rut
        print(f"Rút tiền thành công! Số dư còn lại: {so_du_con_lai:.2f} VNĐ")
        return so_du_con_lai
        
    except ValueError as e:
        # Bắt lỗi chuyển kiểu và lỗi logic
        if "could not convert" in str(e):
            print("Lỗi: Vui lòng nhập số hợp lệ.")
        else:
            print(f"Lỗi: {e}")
        return so_du
    except Exception as e:
        print(f"Lỗi hệ thống: {e}")
        return so_du

# Thử nghiệm các trường hợp
print("Giao dịch 1: Rút 100000 từ số dư 500000")
rut_tien(500000, 100000)

print("Giao dịch 2: Rút -50000")
rut_tien(500000, -50000)

print("Giao dịch 3: Rút 600000 (vượt số dư)")
rut_tien(500000, 600000)

print("Giao dịch 4: Nhập sai định dạng")
rut_tien(500000, "abc")
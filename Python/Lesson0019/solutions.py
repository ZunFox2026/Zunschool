# solutions.py - Lời giải Bài 19

# Bài 1: Viết hàm chia hai số, xử lý các lỗi có thể xảy ra
def chia_hai_so(a, b):
    try:
        # Chuyển đổi kiểu dữ liệu nếu cần
        a = float(a)
        b = float(b)
        
        if b == 0:
            raise ZeroDivisionError("Không thể chia cho 0")
        
        ket_qua = a / b
        print(f"Kết quả: {a} / {b} = {ket_qua}")
        return ket_qua
        
    except ZeroDivisionError as e:
        print(f"Lỗi chia cho 0: {e}")
        return None
    except ValueError:
        print("Lỗi: Vui lòng nhập số hợp lệ")
        return None
    except TypeError:
        print("Lỗi: Kiểu dữ liệu không hợp lệ")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None

# Bài 2: Nhập tuổi hợp lệ
def nhap_tuoi():
    while True:
        try:
            tuoi = int(input("Nhập tuổi của bạn: "))
            
            if tuoi <= 0:
                raise ValueError("Tuổi phải là số nguyên dương")
            
            if tuoi > 150:
                print("Tuổi quá lớn, vui lòng nhập lại.")
                continue
            
            print(f"Tuổi hợp lệ: {tuoi}")
            return tuoi
            
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Lỗi: Tuổi phải là một số nguyên")
            else:
                print(f"Lỗi: {e}")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

# Bài 3: Đọc file và đếm số dòng
def dem_so_dong(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            so_dong = 0
            for dong in f:
                so_dong += 1
            print(f"File '{ten_file}' có {so_dong} dòng.")
            return so_dong
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'")
        return 0
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'")
        return 0
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return 0

# Bài 4: Tìm phần tử lớn nhất trong danh sách
def tim_lon_nhat(danh_sach):
    try:
        if len(danh_sach) == 0:
            raise ValueError("Danh sách rỗng, không thể tìm giá trị lớn nhất")
        
        # Kiểm tra tất cả phần tử có phải số không
        for phan_tu in danh_sach:
            if not isinstance(phan_tu, (int, float)):
                raise TypeError(f"Phần tử '{phan_tu}' không phải là số")
        
        gia_tri_lon_nhat = max(danh_sach)
        print(f"Giá trị lớn nhất: {gia_tri_lon_nhat}")
        return gia_tri_lon_nhat
        
    except ValueError as e:
        print(f"Lỗi: {e}")
        return None
    except TypeError as e:
        print(f"Lỗi kiểu dữ liệu: {e}")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None

# Bài 5: Tính chỉ số BMI
def tinh_bmi(can_nang, chieu_cao):
    try:
        # Chuyển đổi sang số thực
        can_nang = float(can_nang)
        chieu_cao = float(chieu_cao)
        
        # Kiểm tra giá trị hợp lệ
        if can_nang <= 0:
            raise ValueError("Cân nặng phải lớn hơn 0")
        if chieu_cao <= 0:
            raise ValueError("Chiều cao phải lớn hơn 0")
        
        bmi = can_nang / (chieu_cao ** 2)
        print(f"Chỉ số BMI: {bmi:.2f}")
        
        # Phân loại BMI đơn giản
        if bmi < 18.5:
            print("Phân loại: Gầy")
        elif bmi < 25:
            print("Phân loại: Bình thường")
        elif bmi < 30:
            print("Phân loại: Thừa cân")
        else:
            print("Phân loại: Béo phì")
        
        return round(bmi, 2)
        
    except ValueError as e:
        if "could not convert" in str(e):
            print("Lỗi: Vui lòng nhập số hợp lệ cho cân nặng và chiều cao")
        else:
            print(f"Lỗi dữ liệu: {e}")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None
### Lời giải bài tập xử lý ngoại lệ

# Bài 1: Nhập tuổi hợp lệ
def nhap_tuoi():
    while True:
        try:
            tuoi = int(input("Nhập tuổi (1-120): "))
            if 1 <= tuoi <= 120:
                return tuoi
            else:
                print("Tuổi phải từ 1 đến 120.")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

# Bài 2: Đọc danh sách tên từ file
def doc_danh_sach_ten(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            danh_sach = []
            for dong in f:
                ten = dong.strip()
                if ten:  # Chỉ thêm nếu tên không rỗng
                    danh_sach.append(ten)
            return danh_sach
    except FileNotFoundError:
        print(f"Không tìm thấy file: {ten_file}")
        return []
    except PermissionError:
        print(f"Không có quyền đọc file: {ten_file}")
        return []
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return []

# Bài 3: Tính trung bình các số
def tinh_trung_binh(danh_sach):
    try:
        if not danh_sach:
            raise ValueError("Danh sách rỗng")
        
        tong = 0
        for phan_tu in danh_sach:
            try:
                so = float(phan_tu)
                tong += so
            except (ValueError, TypeError):
                print(f"Bỏ qua giá trị không hợp lệ: {phan_tu}")
        
        if tong == 0 and len(danh_sach) > 0:
            # Có thể tất cả phần tử đều bị bỏ qua
            return 0
            
        return tong / len(danh_sach)
        
    except Exception as e:
        print(f"Lỗi khi tính trung bình: {e}")
        return None

# Bài 4: Kiểm tra email hợp lệ
class InvalidEmailError(Exception):
    """Ngoại lệ khi email không hợp lệ"""
    pass

def kiem_tra_email(email):
    try:
        if not isinstance(email, str):
            raise InvalidEmailError("Email phải là chuỗi ký tự")
        
        if '@' not in email or '.' not in email:
            raise InvalidEmailError("Email phải chứa @ và .")
        
        if email.startswith('@') or email.endswith('@'):
            raise InvalidEmailError("@ không được ở đầu hoặc cuối email")
        
        print("Email hợp lệ.")
        
    except InvalidEmailError as e:
        print(f"Lỗi email: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

# Bài 5: Tính chỉ số BMI
def tinh_bmi(can_nang, chieu_cao):
    try:
        # Chuyển kiểu dữ liệu nếu cần
        can_nang = float(can_nang)
        chieu_cao = float(chieu_cao)
        
        if can_nang <= 0:
            raise ValueError("Cân nặng phải lớn hơn 0")
        if chieu_cao <= 0:
            raise ValueError("Chiều cao phải lớn hơn 0")
        
        bmi = can_nang / (chieu_cao ** 2)
        
        print(f"Chỉ số BMI: {bmi:.2f}")
        
        # Phân loại BMI
        if bmi < 18.5:
            print("Gầy")
        elif 18.5 <= bmi < 25:
            print("Bình thường")
        elif 25 <= bmi < 30:
            print("Hơi béo")
        else:
            print("Béo phì")
            
    except ValueError as e:
        print(f"Lỗi giá trị: {e}")
    except TypeError:
        print("Cân nặng và chiều cao phải là số")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
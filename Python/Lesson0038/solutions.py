####################
# Bài tập 1: Hàm chia hai số
####################

def chia_hai_so(a, b):
    try:
        # Chuyển đổi sang số thực để tránh lỗi kiểu dữ liệu
        so_a = float(a)
        so_b = float(b)
        
        ket_qua = so_a / so_b
        print(f"Kết quả {so_a} / {so_b} = {ket_qua}")
        return ket_qua
        
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
    except (ValueError, TypeError):
        print("Lỗi: Vui lòng nhập các giá trị số hợp lệ!")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")


####################
# Bài tập 2: Đếm số dòng trong file
####################

def dem_so_dong(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            so_dong = sum(1 for line in f)
            print(f"File '{ten_file}' có {so_dong} dòng.")
            return so_dong
            
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'!")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'!")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")


####################
# Bài tập 3: Tìm phần tử lớn nhất trong danh sách
####################

def tim_lon_nhat(danh_sach):
    try:
        if len(danh_sach) == 0:
            raise ValueError("Danh sách rỗng!")
        
        # Kiểm tra từng phần tử có phải là số không
        danh_sach_so = []
        for phan_tu in danh_sach:
            if isinstance(phan_tu, (int, float)):
                danh_sach_so.append(phan_tu)
            else:
                try:
                    # Thử chuyển đổi sang số
                    so = float(phan_tu)
                    danh_sach_so.append(so)
                except:
                    raise TypeError(f"Phần tử '{phan_tu}' không phải là số!")
        
        gia_tri_lon_nhat = max(danh_sach_so)
        print(f"Phần tử lớn nhất là: {gia_tri_lon_nhat}")
        return gia_tri_lon_nhat
        
    except ValueError as e:
        print(f"Lỗi giá trị: {e}")
    except TypeError as e:
        print(f"Lỗi kiểu dữ liệu: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")


####################
# Bài tập 4: Đăng nhập với giới hạn 3 lần thử
####################

def dang_nhap():
    MAX_LAN = 3
    tai_khoan_dung = "admin"
    mat_khau_dung = "123456"
    
    for lan in range(MAX_LAN):
        try:
            print(f"Lần thử {lan + 1}/{MAX_LAN}")
            ten = input("Tên đăng nhập: ").strip()
            mat_khau = input("Mật khẩu: ").strip()
            
            if not ten or not mat_khau:
                print("Lỗi: Tên hoặc mật khẩu không được để trống!")
                continue
            
            if ten == tai_khoan_dung and mat_khau == mat_khau_dung:
                print("Đăng nhập thành công!")
                return True
            else:
                print("Sai tên hoặc mật khẩu!")
                
        except KeyboardInterrupt:
            print("\nHủy đăng nhập bởi người dùng.")
            return False
        
    print("Bạn đã thử quá số lần cho phép. Đăng nhập thất bại.")
    return False


####################
# Bài tập 5: Chuyển chuỗi thành danh sách số
####################

def chuoi_sang_danh_sach_so(chuoi):
    try:
        if not chuoi or not chuoi.strip():
            raise ValueError("Chuỗi rỗng!")
        
        # Tách chuỗi theo dấu phẩy
        danh_sach_chuoi = chuoi.split(',')
        danh_sach_so = []
        
        for chuoi_so in danh_sach_chuoi:
            chuoi_so = chuoi_so.strip()  # Xóa khoảng trắng
            if not chuoi_so:
                raise ValueError("Có phần tử rỗng sau dấu phẩy!")
            
            try:
                so = float(chuoi_so)
                danh_sach_so.append(so)
            except ValueError:
                raise ValueError(f"'{chuoi_so}' không phải là số hợp lệ!")
        
        print(f"Danh sách số: {danh_sach_so}")
        return danh_sach_so
        
    except ValueError as e:
        print(f"Lỗi định dạng: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
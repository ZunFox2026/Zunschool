# solutions.py - Lời giải bài tập xử lý ngoại lệ

import math
import json

# Bài 1: Tính căn bậc hai với xử lý lỗi

def tinh_can_bac_hai(x):
    try:
        # Kiểm tra kiểu dữ liệu
        if not isinstance(x, (int, float)):
            raise TypeError("Giá trị phải là số!")
        
        if x < 0:
            raise ValueError("Không thể tính căn bậc hai của số âm!")
        
        return math.sqrt(x)
    
    except TypeError as e:
        print(f"Lỗi kiểu dữ liệu: {e}")
        return None
    except ValueError as e:
        print(f"Lỗi giá trị: {e}")
        return None
    except Exception as e:
        print(f"Lỗi không mong đợi: {e}")
        return None

# Bài 2: Đọc danh sách từ file JSON an toàn

def doc_danh_sach_tu_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                print("Dữ liệu trong file không phải là danh sách.")
                return []
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        return []
    except json.JSONDecodeError:
        print(f"File {filename} không chứa dữ liệu JSON hợp lệ.")
        return []
    except PermissionError:
        print(f"Không có quyền đọc file: {filename}")
        return []
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return []

# Bài 3: Chọn phần tử từ danh sách với xử lý lỗi

def chon_phan_tu(danh_sach):
    if not danh_sach:
        print("Danh sách rỗng, không thể chọn phần tử.")
        return
    
    while True:
        try:
            chi_so = int(input(f"Nhập chỉ số (0 đến {len(danh_sach)-1}): "))
            phan_tu = danh_sach[chi_so]
            print(f"Phần tử tại vị trí {chi_so}: {phan_tu}")
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên!")
        except IndexError:
            print(f"Chỉ số không hợp lệ. Vui lòng nhập từ 0 đến {len(danh_sach)-1}.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")
            break
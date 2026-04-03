# main.py
# Bài học 18: Xử lý ngoại lệ trong Python

# Ví dụ 1: Đọc file điểm số và tính trung bình
# Giả sử file diem.txt chứa các số trên mỗi dòng

print("=== Ví dụ 1: Đọc file và tính trung bình điểm ===")

def doc_va_tinh_diem():
    try:
        with open("diem.txt", "r", encoding="utf-8") as f:
            diem = []
            for dong in f:
                dong = dong.strip()
                if dong:  # Bỏ qua dòng trống
                    diem.append(float(dong))
            
        if len(diem) == 0:
            print("File rỗng!")
            return
            
        trung_binh = sum(diem) / len(diem)
        print(f"Điểm trung bình: {trung_binh:.2f}")
        
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file diem.txt!")
    except ValueError:
        print("Lỗi: File chứa dữ liệu không phải số!")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print("Đọc và tính toán thành công!")
    finally:
        print("Hoàn thành quá trình xử lý file.")

# Tạo file diem.txt để minh họa
with open("diem.txt", "w", encoding="utf-8") as f:
    f.write("8.5\n9.0\n7.5\n10\n")

doc_va_tinh_diem()

# Xóa file sau khi xong để minh họa lỗi
import os
os.remove("diem.txt")
print("\nSau khi xóa file...")
doc_va_tinh_diem()  # Lần gọi này sẽ báo lỗi file không tồn tại


# Ví dụ 2: Xử lý đầu vào tuổi khi đăng ký
print("\n\n=== Ví dụ 2: Xử lý đầu vào tuổi ===")

def nhap_tuoi():
    while True:
        try:
            tuoi = int(input("Nhập tuổi của bạn: "))
            
            if tuoi <= 0:
                raise ValueError("Tuổi phải là số nguyên dương.")
            if tuoi > 150:
                print("Tuổi này có vẻ không hợp lý, nhưng vẫn chấp nhận.")
            
            print(f"Tuổi của bạn là: {tuoi}")
            break
            
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Lỗi: Bạn phải nhập một số nguyên!")
            else:
                print(f"Lỗi: {e}")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

# Gọi hàm (bạn có thể thử nhập chữ hoặc số âm)
# nhap_tuoi()  # Bỏ comment để chạy


# Ví dụ 3: Tính toán an toàn với danh sách
print("\n\n=== Ví dụ 3: Truy cập danh sách an toàn ===")

def tinh_trung_binh_danh_sach(danh_sach):
    try:
        tong = sum(danh_sach)
        trung_binh = tong / len(danh_sach)
        return trung_binh
    except ZeroDivisionError:
        print("Danh sách rỗng, không thể tính trung bình.")
        return None
    except TypeError:
        print("Danh sách chứa phần tử không phải số!")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None

# Thử với các danh sách khác nhau
print(tinh_trung_binh_danh_sach([1, 2, 3, 4, 5]))  # Kết quả: 3.0
print(tinh_trung_binh_danh_sach([]))               # Kết quả: None + thông báo
print(tinh_trung_binh_danh_sach([1, 'a', 3]))      # Kết quả: None + thông báo
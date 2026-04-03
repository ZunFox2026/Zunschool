"""
Bài 41: Xử Lý Ngoại Lệ (Exception Handling) trong Python

Mục tiêu:
- Hiểu khái niệm ngoại lệ (exception) trong Python.
- Biết cách sử dụng try, except, else, finally để xử lý lỗi.
- Áp dụng trong các tình huống thực tế như chia cho 0, truy cập chỉ số ngoài danh sách, v.v.

Tác giả: Python Learning
Ngày: 2023
"""

def vi_du_1_chia_cho_0():
    """
    Ví dụ 1: Xử lý lỗi chia cho 0
    """
    print("=== Ví dụ 1: Xử lý lỗi chia cho 0 ===")
    try:
        a = int(input("Nhập số bị chia a: "))
        b = int(input("Nhập số chia b: "))
        ket_qua = a / b
        print(f"Kết quả: {a} / {b} = {ket_qua}")
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print("Phép chia thành công!")
    finally:
        print("Kết thúc xử lý phép chia.")


def vi_du_2_truy_cap_danh_sach():
    """
    Ví dụ 2: Xử lý lỗi truy cập chỉ số ngoài danh sách
    """
    print("\n=== Ví dụ 2: Truy cập chỉ số ngoài danh sách ===")
    danh_sach = ['táo', 'chuối', 'cam', 'xoài']
    print("Danh sách hiện tại:", danh_sach)

    try:
        chi_so = int(input("Nhập chỉ số muốn truy cập: "))
        print(f"Phần tử tại vị trí {chi_so}: {danh_sach[chi_so]}")
    except IndexError:
        print("Lỗi: Chỉ số vượt quá độ dài của danh sách!")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên!")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
    else:
        print("Truy cập danh sách thành công!")
    finally:
        print("Hoàn tất thao tác truy cập danh sách.")


def vi_du_3_xu_ly_file():
    """
    Ví dụ 3: Xử lý lỗi khi đọc file không tồn tại
    """
    print("\n=== Ví dụ 3: Đọc file văn bản ===")
    ten_file = input("Nhập tên file cần đọc (ví dụ: data.txt): ")

    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
            print("Nội dung file:")
            print(noi_dung)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'!")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'!")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
    else:
        print("Đọc file thành công!")
    finally:
        print("Kết thúc thao tác với file.")


def bai_tap_nho():
    """
    Bài tập nhỏ: Viết chương trình yêu cầu người dùng nhập tuổi.
    - Nếu tuổi không phải số, báo lỗi.
    - Nếu tuổi âm hoặc lớn hơn 150, coi là dữ liệu không hợp lệ.
    - Dùng ngoại lệ để xử lý.
    """
    print("\n=== Bài tập nhỏ: Nhập tuổi hợp lệ ===")
    try:
        tuoi = int(input("Nhập tuổi của bạn: "))
        if tuoi < 0 or tuoi > 150:
            raise ValueError("Tuổi không hợp lệ: phải nằm trong khoảng 0-150.")
        print(f"Tuổi của bạn là: {tuoi}")
    except ValueError as e:
        # Nếu lỗi do chuyển đổi kiểu, e sẽ không có thông báo tùy chỉnh
        if "invalid literal" in str(e):
            print("Lỗi: Tuổi phải là một số nguyên!")
        else:
            print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print("Cảm ơn bạn đã nhập tuổi hợp lệ!")
    finally:
        print("Kết thúc chương trình nhập tuổi.")


def main():
    """
    Hàm chính chạy các ví dụ và bài tập
    """
    print("📘 BÀI 41: XỬ LÝ NGOẠI LỆ TRONG PYTHON\n")
    
    # Chạy các ví dụ
    vi_du_1_chia_cho_0()
    vi_du_2_truy_cap_danh_sach()
    vi_du_3_xu_ly_file()
    
    # Bài tập nhỏ
    bai_tap_nho()

    print("\n🎯 Kiến thức cần nhớ:")
    print(" - try: khối lệnh có thể phát sinh lỗi")
    print(" - except: xử lý lỗi tương ứng")
    print(" - else: chạy nếu không có lỗi")
    print(" - finally: luôn chạy dù có lỗi hay không")
    print(" - Có thể bắt nhiều loại ngoại lệ riêng biệt.")


# Gọi hàm main khi chạy file
if __name__ == "__main__":
    main()
```

---

**Ghi chú:**
- File này khoảng 100 dòng, có đầy đủ ví dụ và bài tập nhỏ.
- Mỗi phần được comment rõ ràng bằng tiếng Việt.
- Có sử dụng `try`, `except`, `else`, `finally`.
- Bài tập nhỏ giúp người học luyện tập xử lý ngoại lệ thực tế.
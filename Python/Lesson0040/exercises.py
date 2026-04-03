### BÀI TẬP 1
# Viết hàm `chia_hai_so(a, b)` nhận hai số a và b.
# Nếu b == 0, gây ra ngoại lệ ZeroDivisionError với thông báo rõ ràng.
# Nếu a hoặc b không phải số, gây ra ValueError.
# Hàm trả về kết quả a / b.
# Sử dụng try-except để gọi hàm và xử lý lỗi.

def chia_hai_so(a, b):
    # Gợi ý: Dùng isinstance() để kiểm tra kiểu dữ liệu
    pass

# Gọi và kiểm thử
# try:
#     print(chia_hai_so(10, 2))
#     print(chia_hai_so(10, 0))
# except (ValueError, ZeroDivisionError) as e:
#     print(e)


### BÀI TẬP 2
# Tạo một lớp ngoại lệ tùy chỉnh tên là `SoDienThoaiSaiDinhDangError`.
# Ngoại lệ này được ném ra khi số điện thoại không đúng định dạng (ví dụ: không đủ 10 chữ số, không bắt đầu bằng '0').
# Viết hàm `kiem_tra_so_dien_thoai(sdt)` để kiểm tra và có thể ném lỗi.

class SoDienThoaiSaiDinhDangError(Exception):
    pass

def kiem_tra_so_dien_thoai(sdt):
    # Gợi ý: Kiểm tra độ dài, ký tự, và ký tự đầu
    pass


### BÀI TẬP 3
# Viết chương trình đọc một file văn bản.
# Nếu file không tồn tại, in thông báo.
# Nếu có lỗi khi đọc (quyền, định dạng...), xử lý riêng.
# Dù có lỗi hay không, in ra "Hoàn tất việc đọc file."
# Sử dụng khối finally.

def doc_file(ten_file):
    # Gợi ý: Dùng try-except-finally, mở file với 'r'
    pass
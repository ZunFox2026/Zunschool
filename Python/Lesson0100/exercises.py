import inspect
import functools

# Bài tập 1: Viết hàm kiểm tra tham số bắt buộc
# Viết hàm `kiem_tra_tham_so_bat_buoc(func)` nhận vào một hàm
# và trả về danh sách tên các tham số bắt buộc (không có giá trị mặc định)

def bai_tap_1():
    # TODO: Viết hàm kiem_tra_tham_so_bat_buoc ở đây
    pass

# Bài tập 2: Tạo decorator kiểm tra kiểu tham số
# Viết decorator `kiem_tra_kieu` sử dụng `inspect.signature`
# để kiểm tra kiểu của các tham số đầu vào dựa trên type hints.
# Nếu kiểu không khớp, in cảnh báo (không chặn thực thi)

def bai_tap_2():
    # TODO: Viết decorator kiem_tra_kieu ở đây
    pass

# Bài tập 3: Liệt kê tất cả lớp con trong một module
# Viết hàm `liet_ke_lop_con(base_class, module)`
# trả về danh sách tên các lớp con kế thừa từ base_class trong module

def bai_tap_3():
    # TODO: Viết hàm liet_ke_lop_con ở đây
    pass

# Bài tập 4: Ghi log tên hàm gọi trước đó
# Viết hàm `ham_duoc_goi_truoc()` sử dụng inspect
# để trả về tên của hàm đã gọi hàm hiện tại
# Nếu không phải do hàm khác gọi, trả về "trực tiếp"

def bai_tap_4():
    # TODO: Viết hàm ham_duoc_goi_truoc ở đây
    pass

if __name__ == "__main__":
    # Gọi các hàm bài tập để kiểm tra
    bai_tap_1()
    bai_tap_2()
    bai_tap_3()
    bai_tap_4()
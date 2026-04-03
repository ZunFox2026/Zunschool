# Bài tập 1: Viết hàm chào hỏi cá nhân hóa
def chao_hoi(ho, ten):
    """
    In lời chào với họ và tên đầy đủ
    """
    print(f"Chào bạn {ho} {ten}!")

# Gọi thử hàm
chao_hoi("Nguyễn", "Nam")

# Bài tập 2: Tính điểm trung bình
def tinh_diem_trung_binh(toan, ly, hoa):
    """
    Tính và trả về điểm trung bình của 3 môn học
    """
    diem_tb = (toan + ly + hoa) / 3
    return diem_tb

# Gọi thử hàm
print(f"Điểm trung bình: {tinh_diem_trung_binh(8, 7, 9):.2f}")

# Bài tập 3: Kiểm tra độ dài mật khẩu
def kiem_tra_mat_khau(mat_khau):
    """
    Kiểm tra mật khẩu có ít nhất 8 ký tự không
    Trả về True nếu đạt, ngược lại False
    """
    return len(mat_khau) >= 8

# Gọi thử hàm
print(kiem_tra_mat_khau("1234567"))   # False
print(kiem_tra_mat_khau("mypass123")) # True

# Bài tập 4: Tính tuổi từ năm sinh
def tinh_tuoi(nam_sinh):
    """
    Tính tuổi dựa trên năm sinh, giả sử năm hiện tại là 2025
    """
    nam_hien_tai = 2025
    return nam_hien_tai - nam_sinh

# Gọi thử hàm
print(f"Tuổi: {tinh_tuoi(2000)}")

# Bài tập 5: In menu
def in_menu():
    """
    In ra menu lựa chọn đơn giản
    """
    print("--- MENU ---")
    print("1. Thêm")
    print("2. Sửa")
    print("3. Xóa")
    print("0. Thoát")

# Gọi thử hàm
in_menu()

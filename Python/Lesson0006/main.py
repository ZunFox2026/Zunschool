# main.py
# Các ví dụ minh họa cho bài học 6: Tuple, Set, Dictionary

# --- VÍ DỤ 1: Tuple - Lưu thông tin học sinh ---
print("=== VÍ DỤ 1: TUPLE ===")

# Khai báo một tuple chứa thông tin học sinh
tuple_student = ("Trần Minh Anh", 16, "Lớp 10A", "Toán")

# Truy cập các phần tử trong tuple theo chỉ số
tên = tuple_student[0]
tuổi = tuple_student[1]
lớp = tuple_student[2]
môn_yêu_thích = tuple_student[3]

print(f"Học sinh: {tên}")
print(f"Tuổi: {tuổi}")
print(f"Lớp: {lớp}")
print(f"Môn yêu thích: {môn_yêu_thích}")

# Tuple không thể thay đổi
# tuple_student[1] = 17  # Sẽ lỗi nếu mở comment

# --- VÍ DỤ 2: Set - Loại bỏ trùng lặp và tìm môn học chung ---
print("\n=== VÍ DỤ 2: SET ===")

# Danh sách môn học của hai học sinh (có thể trùng)
minh_subjects = ["Toán", "Lý", "Hóa", "Anh", "Toán"]
lan_subjects = ["Lý", "Sinh", "Hóa", "Anh", "Văn", "Lý"]

# Chuyển thành set để loại bỏ trùng và làm phép toán tập hợp
set_minh = set(minh_subjects)
set_lan = set(lan_subjects)

# Tìm các môn học mà cả hai cùng học (giao)
common_subjects = set_minh & set_lan  # hoặc set_minh.intersection(set_lan)

# Tìm tất cả các môn học mà ít nhất một trong hai học (hợp)
all_subjects = set_minh | set_lan  # hoặc set_minh.union(set_lan)

print(f"Môn học của Minh: {set_minh}")
print(f"Môn học của Lan: {set_lan}")
print(f"Môn học chung: {common_subjects}")
print(f"Tất cả môn học: {all_subjects}")

# --- VÍ DỤ 3: Dictionary - Quản lý điểm số học sinh ---
print("\n=== VÍ DỤ 3: DICTIONARY ===")

# Tạo một từ điển để lưu điểm các môn học
dict_scores = {
    "Toán": 8.5,
    "Lý": 7.0,
    "Hóa": 9.0,
    "Anh": 6.5,
    "Văn": 7.5
}

# Truy cập điểm một môn
print(f"Điểm Toán: {dict_scores['Toán']}")

# Thêm điểm môn mới
dict_scores["Sử"] = 8.0

# Cập nhật điểm môn Anh
dict_scores["Anh"] = 7.0

# In tất cả các môn và điểm
print("\nĐiểm các môn học:")
for subject, score in dict_scores.items():
    print(f"{subject}: {score}")

# Tính điểm trung bình
tb = sum(dict_scores.values()) / len(dict_scores)
print(f"\nĐiểm trung bình: {tb:.2f}")
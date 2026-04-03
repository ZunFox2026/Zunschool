# solutions.py
# Lời giải bài tập cho bài học 6: Tuple, Set, Dictionary

# --- Bài 1: Tạo tuple thông tin cá nhân ---
tuple_info = ("Lê Thị Hoa", 25, "Hà Nội", "Giáo viên")
print(f"Tôi tên là {tuple_info[0]}, {tuple_info[1]} tuổi, đến từ {tuple_info[2]}, làm nghề {tuple_info[3]}.\n")

# --- Bài 2: Loại bỏ từ trùng trong danh sách ---
word_list = ["xin", "chào", "tạm", "biệt", "xin", "chào", "lại"]
unique_words = set(word_list)  # Chuyển thành set để loại bỏ trùng
deduplicated_list = list(unique_words)  # Chuyển lại thành list (nếu cần)
print(f"Danh sách từ không trùng: {deduplicated_list}\n")

# --- Bài 3: Đếm tần suất xuất hiện của chữ cái ---
text = "dodung"
char_count = {}  # Tạo từ điển rỗng để đếm

for char in text:
    if char in char_count:
        char_count[char] += 1  # Nếu đã có, tăng giá trị lên 1
    else:
        char_count[char] = 1   # Nếu chưa có, khởi tạo bằng 1

print(f"Tần suất chữ cái: {char_count}\n")

# --- Bài 4: Tìm phần tử chung trong hai danh sách ---
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)
common_elements = set1 & set2  # Hoặc set1.intersection(set2)

print(f"Phần tử chung: {common_elements}\n")

# --- Bài 5: Quản lý thông tin sách trong thư viện ---
book_info = {
    "tieu_de": "Lập trình Python từ A đến Z",
    "tac_gia": "Nguyễn Văn Py",
    "nam_xuat_ban": 2023,
    "so_trang": 450,
    "dang_sach": "bìa cứng"
}

print(f"Sách '{book_info['tieu_de']}' của tác giả {book_info['tac_gia']}, "
      f"xuất bản năm {book_info['nam_xuat_ban']}, {book_info['so_trang']} trang, "
      f"dạng {book_info['dang_sach']}.")
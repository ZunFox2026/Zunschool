# exercises.py
# Bài tập thực hành cho bài học 6: Tuple, Set, Dictionary

# --- Bài 1: Tạo tuple thông tin cá nhân ---
# Viết chương trình tạo một tuple chứa tên, tuổi, quê quán và nghề nghiệp.
# Sau đó in ra thông tin theo định dạng:
# "Tôi tên là [tên], [tuổi] tuổi, đến từ [quê quán], làm nghề [nghề nghiệp]."

# Gợi ý: Tạo tuple và truy cập các phần tử bằng chỉ số

# --- Bài 2: Loại bỏ từ trùng trong danh sách ---
# Cho danh sách các từ: ["xin", "chào", "tạm", "biệt", "xin", "chào", "lại"]
# Hãy chuyển thành set để loại bỏ từ trùng, rồi in ra danh sách từ không trùng.

# Gợi ý: Dùng set() để loại bỏ trùng, rồi chuyển về list nếu cần

# --- Bài 3: Đếm tần suất xuất hiện của chữ cái ---
# Viết chương trình đếm số lần xuất hiện của mỗi chữ cái trong chuỗi sau:
# "dodung"
# Kết quả nên là một dictionary, ví dụ: {'d': 2, 'o': 1, 'u': 1, 'n': 1, 'g': 1}

# Gợi ý: Dùng vòng lặp và kiểm tra nếu chữ cái đã có trong dict thì cộng thêm, chưa có thì gán = 1

# --- Bài 4: Tìm phần tử chung trong hai danh sách ---
# Cho hai danh sách:
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# Hãy tìm và in ra các phần tử xuất hiện ở cả hai danh sách (dùng set)

# Gợi ý: Chuyển hai list thành set rồi dùng phép giao (&)

# --- Bài 5: Quản lý thông tin sách trong thư viện ---
# Tạo một dictionary để lưu thông tin một cuốn sách với các khóa:
# "tieu_de", "tac_gia", "nam_xuat_ban", "so_trang", "dang_sach" (bìa mềm/bìa cứng)
# In ra thông tin sách theo định dạng:
# "Sách '[tieu_de]' của tác giả [tac_gia], xuất bản năm [nam_xuat_ban], [so_trang] trang, dạng [dang_sach]."

# Gợi ý: Tạo dictionary với các cặp khóa-giá trị phù hợp
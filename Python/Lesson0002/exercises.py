# exercises.py - Bài tập thực hành: Cấu trúc rẽ nhánh

# Bài 1: Viết chương trình nhập tuổi và in ra thông báo:
# - Nếu tuổi < 13: "Bạn là trẻ em."
# - Nếu 13 <= tuổi < 18: "Bạn là thiếu niên."
# - Nếu tuổi >= 18: "Bạn là người lớn."

# Gợi ý: Dùng if-elif-else

tuoi = int(input("Nhập tuổi của bạn: "))
# Viết mã của bạn ở đây


# Bài 2: Viết chương trình nhập điểm Toán, Lý, Hóa
# Tính điểm trung bình và xếp loại:
# - Nếu ĐTB >= 8.0: "Giỏi"
# - Nếu 6.5 <= ĐTB < 8.0: "Khá"
# - Nếu 5.0 <= ĐTB < 6.5: "Trung bình"
# - Nếu ĐTB < 5.0: "Yếu"

# Gợi ý: Dùng if-elif-else và hàm input()

diem_toan = float(input("Nhập điểm Toán: "))
diem_ly = float(input("Nhập điểm Lý: "))
diem_hoa = float(input("Nhập điểm Hóa: "))
# Viết mã của bạn ở đây


# Bài 3: Viết chương trình mô phỏng máy bán hàng tự động.
# Người dùng chọn đồ uống (1: Coca, 2: Pepsi, 3: Nước)
# Nếu chọn 1 hoặc 2: in "Đồ uống có gas."
# Nếu chọn 3: in "Đồ uống không gas."
# Nếu chọn khác: in "Lựa chọn không hợp lệ."

# Gợi ý: Dùng if-elif-else và so sánh ==

lua_chon = int(input("Chọn đồ uống (1: Coca, 2: Pepsi, 3: Nước): "))
# Viết mã của bạn ở đây


# Bài 4: Viết chương trình kiểm tra năm nhuận.
# Năm nhuận là năm chia hết cho 4, nhưng nếu chia hết cho 100 thì phải chia hết cho 400.
# Ví dụ: 2000 là năm nhuận, 1900 không phải.

# Gợi ý: Dùng if với nhiều điều kiện kết hợp (and, or)
nam = int(input("Nhập năm: "))
# Viết mã của bạn ở đây


# Bài 5: Viết chương trình nhập một số nguyên và kiểm tra:
# - Nếu số chia hết cho 3 và 5: in "Chia hết cho cả 3 và 5"
# - Nếu chỉ chia hết cho 3: in "Chia hết cho 3"
# - Nếu chỉ chia hết cho 5: in "Chia hết cho 5"
# - Nếu không chia hết cho cả hai: in "Không chia hết cho 3 hoặc 5"

# Gợi ý: Dùng if-elif-else và toán tử %
so = int(input("Nhập một số nguyên: "))
# Viết mã của bạn ở đây

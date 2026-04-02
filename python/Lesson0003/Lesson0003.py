# Bài 3: Làm việc với chuỗi

# Khai báo chuỗi
chuoi = "Xin chào, thế giới!"

# In chuỗi
print(chuoi)

# Độ dài chuỗi
print("Độ dài chuỗi:", len(chuoi))

# Lấy ký tự tại vị trí
print("Ký tự tại vị trí 0:", chuoi[0])

# Cắt chuỗi
print("Cắt chuỗi từ vị trí 4 đến 10:", chuoi[4:10])

# Ghép chuỗi
chuoi1 = "Xin chào, "
chuoi2 = "thế giới!"
print("Ghép chuỗi:", chuoi1 + chuoi2)

# Tìm kiếm chuỗi
print("Tìm kiếm chuỗi 'thế giới':", chuoi.find("thế giới"))

# Thay thế chuỗi
chuoi = chuoi.replace("thế giới", "Python")
print("Thay thế chuỗi:", chuoi)

# Chuyển đổi chuỗi
chuoi = chuoi.upper()
print("Chuyển đổi chuỗi sang chữ hoa:", chuoi)

# Chuyển đổi chuỗi
chuoi = chuoi.lower()
print("Chuyển đổi chuỗi sang chữ thường:", chuoi)

# Xóa khoảng trắng
chuoi = "   Xin chào, thế giới!   "
print("Xóa khoảng trắng:", chuoi.strip())

# Chia chuỗi
chuoi = "Xin chào, thế giới!"
print("Chia chuỗi:", chuoi.split(","))
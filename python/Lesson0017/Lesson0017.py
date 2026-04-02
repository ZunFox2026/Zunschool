# Mở tệp ở mode đọc
file = open("test.txt", "r")

# Đọc nội dung tệp
noidung = file.read()

# In nội dung tệp
print(noidung)

# Đóng tệp
file.close()

# Mở tệp ở mode ghi
file = open("test.txt", "w")

# Ghi nội dung vào tệp
file.write("Đây là nội dung mới")

# Đóng tệp
file.close()

# Mở tệp ở mode đọc
file = open("test.txt", "r")

# Đọc nội dung tệp
noidung = file.read()

# In nội dung tệp
print(noidung)

# Đóng tệp
file.close()

# Mở tệp ở mode thêm
file = open("test.txt", "a")

# Thêm nội dung vào tệp
file.write(" Nội dung thêm")

# Đóng tệp
file.close()

# Mở tệp ở mode đọc
file = open("test.txt", "r")

# Đọc nội dung tệp
noidung = file.read()

# In nội dung tệp
print(noidung)

# Đóng tệp
file.close()
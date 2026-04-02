# Mở tệp tin ở chế độ đọc
file = open("test.txt", "r")

# Đọc nội dung tệp tin
noidung = file.read()

# In nội dung tệp tin
print(noidung)

# Đóng tệp tin
file.close()

# Mở tệp tin ở chế độ ghi
file = open("test.txt", "w")

# Ghi nội dung vào tệp tin
file.write("Xin chào, thế giới!")

# Đóng tệp tin
file.close()

# Mở tệp tin ở chế độ thêm
file = open("test.txt", "a")

# Thêm nội dung vào tệp tin
file.write("\nThế giới Python!")

# Đóng tệp tin
file.close()

# Mở tệp tin ở chế độ đọc
file = open("test.txt", "r")

# Đọc nội dung tệp tin
noidung = file.read()

# In nội dung tệp tin
print(noidung)

# Đóng tệp tin
file.close()
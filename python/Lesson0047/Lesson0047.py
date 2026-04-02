# Mở tệp tin để đọc
file = open("test.txt", "r")
 
# Đọc nội dung tệp tin
noidung = file.read()
 
# In nội dung tệp tin
print(noidung)
 
# Đóng tệp tin
file.close()

# Mở tệp tin để ghi
file = open("test.txt", "w")
 
# Ghi nội dung vào tệp tin
file.write("Xin chào thế giới!")
 
# Đóng tệp tin
file.close()

# Mở tệp tin để đọc và ghi
file = open("test.txt", "r+")
 
# Đọc nội dung tệp tin
noidung = file.read()
print(noidung)
 
# Di chuyển con trỏ đến đầu tệp tin
file.seek(0)
 
# Ghi nội dung vào tệp tin
file.write("Xin chào thế giới mới!")
 
# Đóng tệp tin
file.close()

# Mở tệp tin để thêm nội dung
file = open("test.txt", "a")
 
# Thêm nội dung vào tệp tin
file.write("\nThêm nội dung mới")
 
# Đóng tệp tin
file.close()
# Mở tệp để đọc
file = open("test.txt", "r")
 
# Đọc nội dung tệp
noidung = file.read()
 
# In nội dung tệp
print(noidung)
 
# Đóng tệp
file.close()

# Mở tệp để ghi
file = open("test.txt", "w")
 
# Ghi nội dung vào tệp
file.write("Xin chào thế giới!")
 
# Đóng tệp
file.close()

# Mở tệp để đọc và ghi
file = open("test.txt", "r+")
 
# Đọc nội dung tệp
noidung = file.read()
print(noidung)
 
# Di chuyển con trỏ về đầu tệp
file.seek(0)
 
# Ghi nội dung vào tệp
file.write("Xin chào thế giới mới!")
 
# Đóng tệp
file.close()

# Sử dụng with để mở tệp
with open("test.txt", "r") as file:
    # Đọc nội dung tệp
    noidung = file.read()
    print(noidung)
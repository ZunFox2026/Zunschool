# Mở tệp tin trong chế độ đọc
f = open("test.txt", "r")

# Đọc nội dung tệp tin
content = f.read()

# In nội dung tệp tin
print(content)

# Đóng tệp tin
f.close()

# Mở tệp tin trong chế độ ghi
f = open("test.txt", "w")

# Ghi nội dung vào tệp tin
f.write("Xin chào, thế giới!")

# Đóng tệp tin
f.close()

# Mở tệp tin trong chế độ đọc và ghi
f = open("test.txt", "r+")

# Đọc nội dung tệp tin
content = f.read()

# In nội dung tệp tin
print(content)

# Di chuyển con trỏ đến đầu tệp tin
f.seek(0)

# Ghi nội dung vào tệp tin
f.write("Xin chào, thế giới mới!")

# Đóng tệp tin
f.close()

# Mở tệp tin trong chế độ thêm nội dung
f = open("test.txt", "a")

# Thêm nội dung vào tệp tin
f.write(" Thêm nội dung mới!")

# Đóng tệp tin
f.close()

# Sử dụng with để mở tệp tin
with open("test.txt", "r") as f:
    # Đọc nội dung tệp tin
    content = f.read()
    
    # In nội dung tệp tin
    print(content)
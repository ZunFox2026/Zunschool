# Bài 22: Làm việc với tệp

# Mở tệp ở chế độ đọc (r), ghi (w), thêm (a)
# 'r' là chế độ mặc định nếu không chỉ định
file = open('test.txt', 'w')

# Viết nội dung vào tệp
file.write('Xin chào, thế giới!\n')
file.write('Đây là nội dung của tệp test.txt\n')

# Đóng tệp
file.close()

# Mở tệp và đọc nội dung
file = open('test.txt', 'r')
noidung = file.read()
print(noidung)

# Đóng tệp
file.close()

# Mở tệp và đọc từng dòng
file = open('test.txt', 'r')
for dong in file:
    print(dong, end='')

# Đóng tệp
file.close()

# Sử dụng with để mở tệp, không cần đóng tệp
with open('test.txt', 'r') as file:
    print(file.read())
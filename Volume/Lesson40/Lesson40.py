# Mở tệp tin trong chế độ đọc (read)
f = open("test.txt", "r")

# Đọc nội dung tệp tin
noi_dung = f.read()

# In nội dung tệp tin
print("Nội dung tệp tin:")
print(noi_dung)

# Đóng tệp tin
f.close()

# Mở tệp tin trong chế độ ghi (write)
f = open("test.txt", "w")

# Ghi nội dung vào tệp tin
f.write("Xin chào, thế giới!")

# Đóng tệp tin
f.close()

# Mở tệp tin trong chế độ thêm (append)
f = open("test.txt", "a")

# Thêm nội dung vào tệp tin
f.write("\nĐây là nội dung thêm vào.")

# Đóng tệp tin
f.close()

# Xóa tệp tin
import os
os.remove("test.txt")
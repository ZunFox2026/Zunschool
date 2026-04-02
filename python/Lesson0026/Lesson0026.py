# Bài 26: Làm quen với thư viện matplotlib

# Import thư viện matplotlib
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ
plt.plot(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ hàm số y = x^2')

# Thêm nhãn cho trục x và y
plt.xlabel('x')
plt.ylabel('y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị biểu đồ
plt.show()

# Tạo biểu đồ cột
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.bar(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ cột')

# Thêm nhãn cho trục x và y
plt.xlabel('x')
plt.ylabel('y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị biểu đồ
plt.show()

# Tạo biểu đồ tròn
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.pie(y, labels=x, autopct='%1.1f%%')

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ tròn')

# Hiển thị biểu đồ
plt.show()
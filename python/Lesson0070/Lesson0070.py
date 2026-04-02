# Nhập thư viện matplotlib
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo đồ thị
plt.plot(x, y)

# Thêm tiêu đề đồ thị
plt.title('Đồ thị hàm số y = x^2')

# Thêm nhãn cho trục x và y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị đồ thị
plt.show()

# Tạo đồ thị hình tròn
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo đồ thị
plt.plot(x, y, 'ro')

# Thêm tiêu đề đồ thị
plt.title('Đồ thị hàm số y = x^2 (hình tròn)')

# Thêm nhãn cho trục x và y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị đồ thị
plt.show()

# Tạo đồ thị hình thanh
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo đồ thị
plt.bar(x, y)

# Thêm tiêu đề đồ thị
plt.title('Đồ thị hàm số y = x^2 (hình thanh)')

# Thêm nhãn cho trục x và y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị đồ thị
plt.show()

# Tạo đồ thị hình pie
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo đồ thị
plt.pie(y, labels=x, autopct='%1.1f%%')

# Thêm tiêu đề đồ thị
plt.title('Đồ thị hàm số y = x^2 (hình pie)')

# Hiển thị đồ thị
plt.show()
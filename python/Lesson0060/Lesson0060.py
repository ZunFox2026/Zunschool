# Import thư viện matplotlib
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ
# Comment: plt.plot() dùng để tạo biểu đồ đường
plt.plot(x, y)

# Thêm tiêu đề cho biểu đồ
# Comment: plt.title() dùng để thêm tiêu đề
plt.title('Biểu đồ đường')

# Thêm nhãn cho trục x và y
# Comment: plt.xlabel() và plt.ylabel() dùng để thêm nhãn
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị biểu đồ
# Comment: plt.show() dùng để hiển thị biểu đồ
plt.show()

# Tạo biểu đồ cột
# Comment: plt.bar() dùng để tạo biểu đồ cột
plt.bar(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ cột')

# Thêm nhãn cho trục x và y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị biểu đồ
plt.show()

# Tạo biểu đồ tròn
# Comment: plt.pie() dùng để tạo biểu đồ tròn
plt.pie(y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ tròn')

# Hiển thị biểu đồ
plt.show()
# Import thư viện turtle
import turtle

# Tạo một màn hình mới
man_hinh = turtle.Screen()
man_hinh.setup(width=800, height=600)  # Thiết lập kích thước màn hình

# Tạo một con rùa mới
rua = turtle.Turtle()
rua.speed(1)  # Thiết lập tốc độ di chuyển của rùa

# Vẽ một hình vuông
for i in range(4):
    rua.forward(100)  # Di chuyển về phía trước 100 đơn vị
    rua.right(90)     # Quay phải 90 độ

# Vẽ một hình tam giác
rua.penup()           # Nâng bút lên
rua.goto(-200, 0)    # Di chuyển đến vị trí (-200, 0)
rua.pendown()        # Đặt bút xuống
for i in range(3):
    rua.forward(100)  # Di chuyển về phía trước 100 đơn vị
    rua.left(120)     # Quay trái 120 độ

# Vẽ một hình tròn
rua.penup()           # Nâng bút lên
rua.goto(200, 0)     # Di chuyển đến vị trí (200, 0)
rua.pendown()        # Đặt bút xuống
rua.circle(50)      # Vẽ một hình tròn với bán kính 50 đơn vị

# Giữ màn hình mở cho đến khi người dùng đóng nó
turtle.done()
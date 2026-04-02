# Import thư viện turtle
import turtle

# Tạo một màn hình mới
man_hinh = turtle.Screen()

# Đặt tiêu đề cho màn hình
man_hinh.title("Làm quen với thư viện turtle")

# Tạo một con rùa mới
rua = turtle.Turtle()

# Di chuyển con rùa đến vị trí (0, 0) và hướng lên trên
rua.penup()
rua.goto(0, 0)
rua.pendown()
rua.setheading(90)

# Vẽ một hình vuông
# Comment: con rùa sẽ di chuyển và vẽ theo hướng hiện tại
for i in range(4):
    rua.forward(100)  # Di chuyển con rùa 100 bước
    rua.right(90)      # Quay con rùa sang phải 90 độ

# Vẽ một hình tròn
# Comment: con rùa sẽ di chuyển và vẽ theo hướng hiện tại
rua.penup()
rua.goto(150, 0)
rua.pendown()
rua.circle(50)       # Vẽ một hình tròn bán kính 50

# Vẽ một đường thẳng
# Comment: con rùa sẽ di chuyển và vẽ theo hướng hiện tại
rua.penup()
rua.goto(-150, 0)
rua.pendown()
rua.setheading(0)     # Hướng con rùa sang phải
rua.forward(200)     # Di chuyển con rùa 200 bước

# Giữ màn hình mở cho đến khi người dùng đóng nó
turtle.done()
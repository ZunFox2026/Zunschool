## Giới thiệu
Thư viện turtle là một công cụ mạnh mẽ và thú vị trong Python, cho phép bạn tạo ra các hình dạng và đồ họa đơn giản. Thư viện này đặc biệt phù hợp với người mới bắt đầu, giúp họ làm quen với lập trình và tạo ra các dự án thú vị. Trong bài này, chúng ta sẽ khám phá các tính năng cơ bản của thư viện turtle và cách sử dụng nó để tạo ra các hình dạng và đồ họa.

## Lý thuyết
Thư viện turtle cung cấp một số chức năng cơ bản để tạo ra các hình dạng và đồ họa. Một số chức năng quan trọng bao gồm:
* `turtle.forward(distance)`: Di chuyển con trỏ turtle về phía trước một khoảng cách nhất định.
* `turtle.backward(distance)`: Di chuyển con trỏ turtle về phía sau một khoảng cách nhất định.
* `turtle.left(angle)`: Quay con trỏ turtle sang trái một góc nhất định.
* `turtle.right(angle)`: Quay con trỏ turtle sang phải một góc nhất định.
* `turtle.penup()`: Nâng bút lên, không vẽ khi di chuyển.
* `turtle.pendown()`: Đặt bút xuống, vẽ khi di chuyển.
Chúng ta cũng có thể thay đổi màu sắc và độ rộng của bút bằng cách sử dụng các chức năng như `turtle.pencolor(color)` và `turtle.width(width)`.

## Ví dụ
Dưới đây là một ví dụ đơn giản về việc sử dụng thư viện turtle để vẽ một hình vuông:
```python
import turtle

turtle.speed(1)  # Thiết lập tốc độ di chuyển của turtle
turtle.forward(100)  # Di chuyển về phía trước 100 đơn vị
turtle.right(90)  # Quay sang phải 90 độ
turtle.forward(100)  # Di chuyển về phía trước 100 đơn vị
turtle.right(90)  # Quay sang phải 90 độ
turtle.forward(100)  # Di chuyển về phía trước 100 đơn vị
turtle.right(90)  # Quay sang phải 90 độ
turtle.forward(100)  # Di chuyển về phía trước 100 đơn vị

turtle.done()  # Đợi người dùng đóng cửa sổ
```
Kết quả sẽ là một hình vuông với mỗi cạnh dài 100 đơn vị.

## Bài tập
Để rèn luyện kỹ năng sử dụng thư viện turtle, bạn có thể thử thực hiện các bài tập sau:
* Vẽ một hình tam giác đều với mỗi cạnh dài 100 đơn vị.
* Vẽ một hình tròn với bán kính 50 đơn vị.
* Vẽ một hình chữ nhật với chiều dài 150 đơn vị và chiều rộng 50 đơn vị.
* Tạo một hình ảnh với nhiều hình dạng và màu sắc khác nhau.
Hãy thử nghiệm và khám phá các chức năng của thư viện turtle để tạo ra các dự án thú vị và sáng tạo!
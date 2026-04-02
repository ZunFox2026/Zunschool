# Làm quen với thư viện Turtle

## Giới thiệu
Thư viện Turtle là một công cụ tuyệt vời trong Python giúp bạn tạo ra các hình ảnh và hoạt hình đơn giản. Với thư viện này, bạn có thể tạo ra các hình dạng khác nhau như đường thẳng, hình chữ nhật, hình tròn, hình đa giác, và thậm chí là các hình ảnh động. Thư viện Turtle rất phù hợp cho người mới bắt đầu học lập trình vì nó giúp bạn hiểu rõ về các khái niệm cơ bản như vòng lặp, điều kiện, và hàm.

## Lý thuyết
Thư viện Turtle cung cấp một số hàm và phương thức cơ bản để tạo ra các hình ảnh. Một số hàm và phương thức quan trọng bao gồm:
- `forward()`: Di chuyển con trỏ về phía trước một khoảng cách nhất định.
- `backward()`: Di chuyển con trỏ về phía sau một khoảng cách nhất định.
- `left()`: Quay con trỏ sang trái một góc nhất định.
- `right()`: Quay con trỏ sang phải một góc nhất định.
- `penup()`: Nâng bút lên, không vẽ khi di chuyển.
- `pendown()`: Đặt bút xuống, bắt đầu vẽ khi di chuyển.
- `color()`: Đặt màu cho con trỏ.
- `begin_fill()`: Bắt đầu tô màu cho hình dạng.
- `end_fill()`: Kết thúc tô màu cho hình dạng.

## Ví dụ
Dưới đây là một ví dụ đơn giản về việc sử dụng thư viện Turtle để vẽ một hình vuông:
```python
import turtle

# Tạo một cửa sổ mới
window = turtle.Screen()
window.bgcolor("white")

# Tạo một con trỏ mới
my_turtle = turtle.Turtle()

# Vẽ một hình vuông
for i in range(4):
    my_turtle.forward(100)  # Di chuyển về phía trước 100 đơn vị
    my_turtle.right(90)  # Quay sang phải 90 độ

# Đóng cửa sổ
window.mainloop()
```
Khi bạn chạy đoạn code trên, nó sẽ tạo ra một hình vuông với mỗi cạnh có độ dài 100 đơn vị.

## Bài tập
Bài tập này yêu cầu bạn sử dụng thư viện Turtle để vẽ một hình ngôi sao 5 cánh. Bạn cần sử dụng vòng lặp và hàm `forward()` và `right()` để tạo ra hình dạng này. Hãy thử nghiệm với các giá trị khác nhau cho độ dài cạnh và góc quay để tạo ra các hình ngôi sao khác nhau.
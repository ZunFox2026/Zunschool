# Làm quen với thư viện Turtle
## Giới thiệu
Thư viện Turtle là một công cụ tuyệt vời trong Python, giúp bạn dễ dàng tạo ra các hình ảnh và hình dạng khác nhau trên màn hình. Với Turtle, bạn có thể tạo ra các hình ảnh từ đơn giản đến phức tạp, từ hình học cơ bản đến hình ảnh động. Thư viện này đặc biệt hữu ích cho người mới bắt đầu học lập trình, vì nó giúp bạn hiểu rõ về các khái niệm cơ bản như vòng lặp, điều kiện và hàm.

## Lý thuyết
Thư viện Turtle cung cấp một số hàm và phương thức cơ bản để tạo ra các hình ảnh. Bạn có thể di chuyển con trỏ (hay còn gọi là "rùa") trên màn hình bằng cách sử dụng các hàm như `forward()`, `backward()`, `left()`, `right()`. Bạn cũng có thể thay đổi màu sắc của con trỏ và nền bằng cách sử dụng các hàm như `pencolor()`, `fillcolor()`, `bgcolor()`. Ngoài ra, bạn còn có thể tạo ra các hình dạng khác nhau bằng cách sử dụng các hàm như `circle()`, `rectangle()`, `triangle()`.

Ví dụ, để tạo ra một hình vuông, bạn có thể sử dụng các hàm sau:
- `turtle.forward(100)` để di chuyển con trỏ 100 đơn vị về phía trước
- `turtle.right(90)` để xoay con trỏ 90 độ về phía phải
- `turtle.forward(100)` để di chuyển con trỏ 100 đơn vị về phía trước
- `turtle.right(90)` để xoay con trỏ 90 độ về phía phải
- `turtle.forward(100)` để di chuyển con trỏ 100 đơn vị về phía trước
- `turtle.right(90)` để xoay con trỏ 90 độ về phía phải
- `turtle.forward(100)` để di chuyển con trỏ 100 đơn vị về phía trước

## Ví dụ
Dưới đây là một ví dụ đơn giản về việc sử dụng thư viện Turtle để tạo ra một hình vuông:
```python
import turtle

# Tạo một hình vuông
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

# Giữ màn hình mở
turtle.done()
```
Khi chạy đoạn mã này, bạn sẽ thấy một hình vuông được tạo ra trên màn hình.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một hình ngôi sao năm cánh bằng cách sử dụng thư viện Turtle. Để thực hiện bài tập này, bạn cần sử dụng các hàm như `forward()`, `right()` và `loop` để tạo ra các cánh của ngôi sao. Gợi ý: mỗi cánh của ngôi sao có thể được tạo ra bằng cách di chuyển con trỏ về phía trước và xoay nó 144 độ về phía phải. Hãy thử nghiệm và tìm ra cách để tạo ra một hình ngôi sao năm cánh hoàn hảo!
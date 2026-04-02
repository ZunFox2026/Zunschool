# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình, vì nó cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin trên máy tính. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với tệp tin trong Python.

## Lý thuyết
Trong Python, bạn có thể làm việc với tệp tin bằng cách sử dụng các hàm như `open()`, `read()`, `write()`, và `close()`. Hàm `open()` được sử dụng để mở một tệp tin, trong khi hàm `read()` và `write()` được sử dụng để đọc và ghi dữ liệu vào tệp tin. Cuối cùng, hàm `close()` được sử dụng để đóng tệp tin.

Có ba chế độ mở tệp tin trong Python:
- `r`: Mở tệp tin để đọc.
- `w`: Mở tệp tin để ghi, nếu tệp tin đã tồn tại thì sẽ bị xóa.
- `a`: Mở tệp tin để ghi, nếu tệp tin đã tồn tại thì sẽ thêm dữ liệu vào cuối tệp tin.

## Ví dụ
Dưới đây là một ví dụ về cách làm việc với tệp tin trong Python:
```python
# Mở tệp tin để ghi
f = open("test.txt", "w")

# Ghi dữ liệu vào tệp tin
f.write("Xin chào, thế giới!")

# Đóng tệp tin
f.close()

# Mở tệp tin để đọc
f = open("test.txt", "r")

# Đọc dữ liệu từ tệp tin
data = f.read()

# In dữ liệu
print(data)

# Đóng tệp tin
f.close()
```
Trong ví dụ này, chúng ta mở một tệp tin tên là `test.txt` để ghi dữ liệu, sau đó ghi chuỗi `Xin chào, thế giới!` vào tệp tin. Tiếp theo, chúng ta mở lại tệp tin để đọc dữ liệu và in ra màn hình.

## Bài tập
Để luyện tập kỹ năng làm việc với tệp tin, bạn có thể thực hiện các bài tập sau:
- Tạo một tệp tin tên là `tong.txt` và ghi dữ liệu vào tệp tin.
- Đọc dữ liệu từ tệp tin `tong.txt` và in ra màn hình.
- Tạo một chương trình để ghi dữ liệu vào tệp tin và đọc dữ liệu từ tệp tin.
- Thử nghiệm với các chế độ mở tệp tin khác nhau và quan sát kết quả.
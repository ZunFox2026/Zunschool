# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một phần quan trọng trong lập trình. Trong bài này, chúng ta sẽ tìm hiểu về cách đọc và ghi tệp tin trong Python. Đây là kỹ năng cơ bản nhưng rất cần thiết cho bất kỳ lập trình viên nào. Với kiến thức này, bạn có thể lưu trữ và đọc dữ liệu từ tệp tin, giúp cho chương trình của bạn trở nên linh hoạt và mạnh mẽ hơn.

## Lý thuyết
Trong Python, chúng ta có thể làm việc với tệp tin bằng cách sử dụng hàm `open()`. Hàm này trả về một đối tượng tệp tin, cho phép chúng ta đọc và ghi dữ liệu vào tệp tin. Có nhiều chế độ mở tệp tin, bao gồm:
- `r`: Mở tệp tin để đọc.
- `w`: Mở tệp tin để ghi. Nếu tệp tin đã tồn tại, nội dung của nó sẽ bị xóa.
- `a`: Mở tệp tin để ghi thêm. Nếu tệp tin đã tồn tại, dữ liệu mới sẽ được thêm vào cuối tệp tin.
- `r+`: Mở tệp tin để đọc và ghi.

Chúng ta cũng cần lưu ý về việc đóng tệp tin sau khi sử dụng. Điều này giúp giải phóng tài nguyên và tránh những vấn đề không mong muốn. Chúng ta có thể đóng tệp tin bằng cách sử dụng phương thức `close()`.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách làm việc với tệp tin trong Python:
```python
# Mở tệp tin để đọc
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Mở tệp tin để ghi
file = open("example.txt", "w")
file.write("Xin chào, thế giới!")
file.close()

# Mở tệp tin để ghi thêm
file = open("example.txt", "a")
file.write("\nThêm một dòng mới.")
file.close()
```
Trong ví dụ trên, chúng ta đã mở tệp tin `example.txt` để đọc, ghi, và ghi thêm. Sau mỗi lần sử dụng, chúng ta đã đóng tệp tin để giải phóng tài nguyên.

## Bài tập
Để củng cố kiến thức, bạn hãy thử thực hiện các bài tập sau:
- Tạo một tệp tin mới với tên `hello.txt` và ghi vào đó dòng chữ "Xin chào, thế giới!".
- Đọc nội dung của tệp tin `hello.txt` và in ra màn hình.
- Thêm một dòng mới vào tệp tin `hello.txt` với nội dung "Tôi học Python!".
- Đọc lại nội dung của tệp tin `hello.txt` và in ra màn hình để kiểm tra kết quả.
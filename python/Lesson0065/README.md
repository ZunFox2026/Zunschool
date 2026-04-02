# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình. Trong bài này, chúng ta sẽ tìm hiểu cách đọc và ghi dữ liệu vào tệp tin bằng ngôn ngữ lập trình Python. Đây là một chủ đề cơ bản nhưng rất quan trọng trong việc phát triển ứng dụng.

## Lý thuyết
Để làm việc với tệp tin trong Python, chúng ta cần sử dụng hàm `open()`. Hàm này sẽ mở tệp tin và trả về một đối tượng tệp tin. Chúng ta có thể đọc hoặc ghi dữ liệu vào tệp tin bằng cách sử dụng các phương thức của đối tượng này.

Có ba chế độ mở tệp tin chính:
- `r`: Mở tệp tin để đọc.
- `w`: Mở tệp tin để ghi. Nếu tệp tin đã tồn tại, nội dung sẽ bị xóa.
- `a`: Mở tệp tin để thêm nội dung. Nếu tệp tin đã tồn tại, nội dung mới sẽ được thêm vào cuối tệp tin.

Để đọc dữ liệu từ tệp tin, chúng ta có thể sử dụng phương thức `read()`. Để ghi dữ liệu vào tệp tin, chúng ta có thể sử dụng phương thức `write()`.

## Ví dụ
Ví dụ dưới đây minh họa cách đọc và ghi dữ liệu vào tệp tin:
```python
# Mở tệp tin để ghi
f = open("test.txt", "w")
f.write("Xin chào, thế giới!")
f.close()

# Mở tệp tin để đọc
f = open("test.txt", "r")
print(f.read())
f.close()
```
Kết quả của ví dụ trên sẽ là:
```
Xin chào, thế giới!
```
Chúng ta cũng có thể sử dụng câu lệnh `with` để mở tệp tin. Điều này sẽ giúp tự động đóng tệp tin khi chúng ta không cần sử dụng nó nữa.

```python
with open("test.txt", "r") as f:
    print(f.read())
```
## Bài tập
Bài tập dưới đây sẽ giúp bạn thực hành kỹ năng làm việc với tệp tin:
- Tạo một tệp tin tên là `hello.txt` và ghi vào đó dòng chữ "Xin chào, thế giới!".
- Đọc nội dung của tệp tin `hello.txt` và in nó ra màn hình.
- Thêm nội dung "Đây là một bài tập về tệp tin" vào cuối tệp tin `hello.txt`.
- Đọc lại nội dung của tệp tin `hello.txt` và in nó ra màn hình.

Hãy thử thực hiện các bước trên và xem kết quả. Điều này sẽ giúp bạn hiểu rõ hơn về cách làm việc với tệp tin trong Python.
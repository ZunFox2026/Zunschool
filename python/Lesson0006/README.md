# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và đọc dữ liệu từ các tệp tin. Trong Python, việc này có thể được thực hiện một cách dễ dàng và linh hoạt. Bài này sẽ hướng dẫn bạn cách làm việc với tệp trong Python, bao gồm cả việc đọc và viết tệp.

## Lý thuyết
Trong Python, chúng ta có thể làm việc với tệp bằng cách sử dụng hàm `open()`. Hàm này sẽ trả về một đối tượng tệp, cho phép chúng ta thực hiện các操作 như đọc, viết, hoặc đóng tệp. Có nhiều chế độ mở tệp khác nhau, bao gồm:
- `r`: Mở tệp để đọc.
- `w`: Mở tệp để viết, nếu tệp đã tồn tại thì nội dung sẽ bị xóa.
- `a`: Mở tệp để thêm nội dung vào cuối tệp.
- `r+`: Mở tệp để đọc và viết.
- `x`: Mở tệp để tạo mới, nếu tệp đã tồn tại thì sẽ báo lỗi.

Sau khi mở tệp, chúng ta có thể sử dụng các phương thức như `read()`, `write()`, `close()` để đọc, viết và đóng tệp.

## Ví dụ
Ví dụ sau sẽ minh họa cách mở một tệp tin và đọc nội dung của nó:
```python
# Mở tệp tin để đọc
f = open('example.txt', 'r')

# Đọc nội dung của tệp tin
content = f.read()

# In nội dung của tệp tin
print(content)

# Đóng tệp tin
f.close()
```
Ví dụ sau sẽ minh họa cách mở một tệp tin và viết nội dung vào đó:
```python
# Mở tệp tin để viết
f = open('example.txt', 'w')

# Viết nội dung vào tệp tin
f.write('Xin chào, thế giới!')

# Đóng tệp tin
f.close()
```
## Bài tập
Bài tập 1: Tạo một tệp tin mới có tên là `hello.txt` và viết nội dung "Xin chào, thế giới!" vào đó.
Bài tập 2: Đọc nội dung của tệp tin `hello.txt` và in nó ra màn hình.
Bài tập 3: Thêm nội dung "Đây là một bài tập về tệp tin" vào cuối tệp tin `hello.txt`.
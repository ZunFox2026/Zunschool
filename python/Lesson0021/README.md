# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và đọc dữ liệu từ các tệp tin. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với tệp tin trong Python, bao gồm cả việc đọc và ghi dữ liệu.

## Lý thuyết
Trong Python, chúng ta có thể làm việc với tệp tin bằng cách sử dụng các hàm như `open()`, `read()`, `write()`, và `close()`. Hàm `open()` được sử dụng để mở một tệp tin, trong khi hàm `read()` và `write()` được sử dụng để đọc và ghi dữ liệu vào tệp tin. Cuối cùng, hàm `close()` được sử dụng để đóng tệp tin khi chúng ta đã xong việc với nó.

Có hai chế độ mở tệp tin chính: chế độ đọc (`'r'`) và chế độ ghi (`'w'`). Chế độ đọc cho phép chúng ta đọc dữ liệu từ tệp tin, trong khi chế độ ghi cho phép chúng ta ghi dữ liệu vào tệp tin. Nếu tệp tin không tồn tại, chế độ ghi sẽ tạo một tệp tin mới.

## Ví dụ
Dưới đây là một ví dụ minh họa cách đọc và ghi dữ liệu vào một tệp tin:
```
# Mở tệp tin ở chế độ ghi
f = open('example.txt', 'w')

# Ghi dữ liệu vào tệp tin
f.write('Xin chào, thế giới!')

# Đóng tệp tin
f.close()

# Mở tệp tin ở chế độ đọc
f = open('example.txt', 'r')

# Đọc dữ liệu từ tệp tin
data = f.read()

# In dữ liệu
print(data)

# Đóng tệp tin
f.close()
```
Kết quả của ví dụ trên sẽ là `Xin chào, thế giới!` được ghi vào tệp tin `example.txt` và sau đó được đọc và in ra màn hình.

## Bài tập
Bài tập này yêu cầu bạn thực hiện các bước sau:
- Tạo một tệp tin mới có tên `hello.txt`.
- Ghi chuỗi `Xin chào, lập trình viên!` vào tệp tin.
- Đọc dữ liệu từ tệp tin và in nó ra màn hình.
- Đóng tệp tin.
- Xóa tệp tin `hello.txt` sau khi hoàn thành bài tập.

Hãy nhớ sử dụng các hàm `open()`, `write()`, `read()`, và `close()` để thực hiện các bước trên. Chúc bạn thành công!
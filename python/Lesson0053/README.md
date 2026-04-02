# Làm việc với Files
## Giới thiệu
Làm việc với files là một phần quan trọng trong lập trình Python. Files cho phép chúng ta lưu trữ và đọc dữ liệu từ bên ngoài chương trình, giúp tăng tính linh hoạt và khả năng sử dụng của chương trình. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với files trong Python, bao gồm cả việc đọc và ghi files.

## Lý thuyết
Trong Python, chúng ta có thể làm việc với files bằng cách sử dụng hàm `open()`. Hàm này trả về một đối tượng file, chúng ta có thể sử dụng để đọc hoặc ghi dữ liệu vào file. Có nhiều chế độ mở file khác nhau, bao gồm:
- `r`: Mở file để đọc
- `w`: Mở file để ghi, nếu file đã tồn tại thì sẽ bị xóa
- `a`: Mở file để ghi, nếu file đã tồn tại thì sẽ được thêm vào cuối file
- `r+`: Mở file để đọc và ghi
- `w+`: Mở file để đọc và ghi, nếu file đã tồn tại thì sẽ bị xóa
- `a+`: Mở file để đọc và ghi, nếu file đã tồn tại thì sẽ được thêm vào cuối file

Chúng ta cũng cần lưu ý đến việc đóng file sau khi sử dụng, để tránh浪 phí tài nguyên hệ thống. Chúng ta có thể đóng file bằng cách sử dụng hàm `close()`.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách làm việc với files trong Python:
```python
# Mở file để đọc
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

# Mở file để ghi
file = open('example.txt', 'w')
file.write('Hello, World!')
file.close()

# Mở file để đọc và ghi
file = open('example.txt', 'r+')
content = file.read()
print(content)
file.write('Đây là nội dung mới')
file.close()
```
## Bài tập
Bài tập này yêu cầu bạn tạo một chương trình Python có thể đọc và ghi files. Chương trình sẽ có các chức năng sau:
- Đọc nội dung của một file và in ra màn hình
- Ghi nội dung vào một file
- Thêm nội dung vào cuối một file

Yêu cầu:
- Tạo một file mới có tên `example.txt` và thêm nội dung vào file này
- Đọc nội dung của file `example.txt` và in ra màn hình
- Ghi nội dung vào file `example.txt`
- Thêm nội dung vào cuối file `example.txt`

Khi hoàn thành bài tập này, bạn sẽ có một chương trình Python có thể làm việc với files một cách linh hoạt và hiệu quả.
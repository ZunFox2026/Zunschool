# Làm quen với thư viện requests
## Giới thiệu
Thư viện `requests` là một trong những thư viện phổ biến nhất trong Python, giúp cho việc gửi và nhận yêu cầu HTTP trở nên đơn giản và dễ dàng. Thư viện này cung cấp một giao diện đơn giản và trực quan để tương tác với các máy chủ web, cho phép bạn gửi yêu cầu GET, POST, PUT, DELETE và nhiều hơn nữa.

## Lý thuyết
Thư viện `requests` hỗ trợ các phương thức yêu cầu HTTP sau:
- GET: Lấy thông tin từ máy chủ
- POST: Gửi thông tin đến máy chủ
- PUT: Cập nhật thông tin trên máy chủ
- DELETE: Xóa thông tin trên máy chủ
Để sử dụng thư viện `requests`, bạn cần nhập nó vào chương trình Python của mình bằng câu lệnh `import requests`. Sau đó, bạn có thể sử dụng các phương thức yêu cầu HTTP bằng cách gọi các hàm tương ứng, chẳng hạn như `requests.get()`, `requests.post()`, `requests.put()`, `requests.delete()`.

## Ví dụ
Ví dụ về việc gửi yêu cầu GET đến trang web https://www.google.com:
```python
import requests

response = requests.get('https://www.google.com')
print(response.status_code)
print(response.text)
```
Kết quả sẽ hiển thị mã trạng thái của yêu cầu (200 nếu thành công) và nội dung của trang web.

Ví dụ về việc gửi yêu cầu POST đến trang web https://www.example.com với dữ liệu `name=John&age=30`:
```python
import requests

data = {'name': 'John', 'age': 30}
response = requests.post('https://www.example.com', data=data)
print(response.status_code)
print(response.text)
```
Kết quả sẽ hiển thị mã trạng thái của yêu cầu (200 nếu thành công) và nội dung của trang web sau khi gửi dữ liệu.

## Bài tập
Bài tập 1: Gửi yêu cầu GET đến trang web https://www.facebook.com và hiển thị mã trạng thái của yêu cầu.
Bài tập 2: Gửi yêu cầu POST đến trang web https://www.example.com với dữ liệu `name=Jane&age=25` và hiển thị nội dung của trang web sau khi gửi dữ liệu.
Bài tập 3: Tạo một chương trình Python sử dụng thư viện `requests` để lấy thông tin về thời tiết tại một thành phố cụ thể.
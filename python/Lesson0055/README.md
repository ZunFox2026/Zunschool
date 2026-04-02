# Làm quen với thư viện requests
## Giới thiệu
Thư viện `requests` là một trong những thư viện phổ biến nhất trong Python, giúp chúng ta gửi và nhận dữ liệu từ các trang web một cách dễ dàng. Thư viện này cung cấp một giao diện đơn giản và trực quan để thực hiện các yêu cầu HTTP, bao gồm GET, POST, PUT, DELETE, v.v. Trong bài này, chúng ta sẽ tìm hiểu về cách sử dụng thư viện `requests` để gửi và nhận dữ liệu từ các trang web.

## Lý thuyết
Để bắt đầu sử dụng thư viện `requests`, chúng ta cần hiểu về các phương thức yêu cầu HTTP cơ bản. Các phương thức này bao gồm:
- GET: Lấy dữ liệu từ một trang web
- POST: Gửi dữ liệu đến một trang web
- PUT: Cập nhật dữ liệu trên một trang web
- DELETE: Xóa dữ liệu trên một trang web
Thư viện `requests` cung cấp các hàm tương ứng với từng phương thức này, bao gồm `get()`, `post()`, `put()`, `delete()`. Khi gửi một yêu cầu, chúng ta có thể truyền các tham số như URL, dữ liệu, header, v.v.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng thư viện `requests` để lấy dữ liệu từ một trang web:
```python
import requests

url = "https://www.example.com"
response = requests.get(url)

print(response.status_code)  # In mã trạng thái của yêu cầu
print(response.text)  # In nội dung của trang web
```
Trong ví dụ này, chúng ta sử dụng hàm `get()` để gửi một yêu cầu GET đến trang web `https://www.example.com`. Sau đó, chúng ta in mã trạng thái của yêu cầu và nội dung của trang web.

## Bài tập
Để thực hành sử dụng thư viện `requests`, hãy thực hiện các bài tập sau:
- Gửi một yêu cầu GET đến trang web `https://www.google.com` và in nội dung của trang web.
- Gửi một yêu cầu POST đến trang web `https://httpbin.org/post` với dữ liệu `{"name": "Zunny", "age": 25}` và in nội dung của phản hồi.
- Sử dụng thư viện `requests` để lấy dữ liệu từ một trang web và lưu vào một tệp tin.
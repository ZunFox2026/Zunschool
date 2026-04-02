# Làm quen với thư viện Requests
## Giới thiệu
Thư viện Requests là một trong những thư viện phổ biến nhất trong Python, giúp bạn gửi và nhận dữ liệu từ các trang web một cách dễ dàng. Với Requests, bạn có thể gửi các yêu cầu HTTP như GET, POST, PUT, DELETE,... và nhận lại dữ liệu từ máy chủ.

## Lý thuyết
Để sử dụng thư viện Requests, bạn cần hiểu một số khái niệm cơ bản về HTTP. HTTP (Hypertext Transfer Protocol) là một giao thức truyền tải dữ liệu trên internet. Các yêu cầu HTTP bao gồm:
- GET: Lấy dữ liệu từ máy chủ
- POST: Gửi dữ liệu đến máy chủ
- PUT: Cập nhật dữ liệu trên máy chủ
- DELETE: Xóa dữ liệu trên máy chủ

Thư viện Requests cung cấp các phương thức tương ứng với các yêu cầu HTTP này. Ví dụ, `requests.get()` để gửi yêu cầu GET, `requests.post()` để gửi yêu cầu POST,...

## Ví dụ
Dưới đây là một ví dụ về việc sử dụng thư viện Requests để lấy dữ liệu từ một trang web:
```python
import requests

# Gửi yêu cầu GET đến trang web
response = requests.get('https://www.example.com')

# In ra mã trạng thái của yêu cầu
print(response.status_code)

# In ra nội dung của trang web
print(response.text)
```
Trong ví dụ trên, chúng ta gửi một yêu cầu GET đến trang web `https://www.example.com` và in ra mã trạng thái của yêu cầu cũng như nội dung của trang web.

## Bài tập
Bài tập cho bạn:
- Sử dụng thư viện Requests để lấy dữ liệu từ trang web `https://jsonplaceholder.typicode.com/todos/1`
- In ra mã trạng thái của yêu cầu
- In ra nội dung của trang web
- Sử dụng phương thức `requests.post()` để gửi dữ liệu đến trang web `https://jsonplaceholder.typicode.com/todos`
- In ra mã trạng thái của yêu cầu
- In ra nội dung của trang web sau khi gửi dữ liệu

Hãy thử thực hiện các bài tập trên và khám phá thêm về thư viện Requests!
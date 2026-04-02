# Làm quen với thư viện requests
## Giới thiệu
Thư viện `requests` là một trong những thư viện phổ biến nhất trong Python, giúp cho việc gửi và nhận yêu cầu HTTP trở nên đơn giản và dễ dàng. Với `requests`, bạn có thể gửi các yêu cầu GET, POST, PUT, DELETE, v.v. đến một máy chủ web và nhận lại phản hồi. Bài viết này sẽ giới thiệu về cách sử dụng thư viện `requests` và cung cấp các ví dụ minh họa.

## Lý thuyết
Thư viện `requests` cung cấp một số phương thức chính để gửi yêu cầu HTTP, bao gồm:
- `requests.get()`: Gửi yêu cầu GET đến một URL.
- `requests.post()`: Gửi yêu cầu POST đến một URL.
- `requests.put()`: Gửi yêu cầu PUT đến một URL.
- `requests.delete()`: Gửi yêu cầu DELETE đến một URL.

Mỗi phương thức này đều trả về một đối tượng `Response`, chứa thông tin về phản hồi từ máy chủ web. Đối tượng `Response` có các thuộc tính như `status_code`, `text`, `json()`, v.v.

## Ví dụ
Dưới đây là một số ví dụ về cách sử dụng thư viện `requests`:
- Gửi yêu cầu GET đến một URL:
```python
import requests

url = "https://www.example.com"
response = requests.get(url)

print(response.status_code)  # In ra mã trạng thái HTTP
print(response.text)  # In ra nội dung HTML của trang web
```
- Gửi yêu cầu POST đến một URL:
```python
import requests

url = "https://www.example.com/api/create"
data = {"name": "John Doe", "age": 30}
response = requests.post(url, json=data)

print(response.status_code)  # In ra mã trạng thái HTTP
print(response.json())  # In ra nội dung JSON của phản hồi
```
## Bài tập
Bài tập này yêu cầu bạn viết một chương trình Python sử dụng thư viện `requests` để gửi yêu cầu GET đến một URL và in ra mã trạng thái HTTP và nội dung HTML của trang web.

- Yêu cầu:
  - Gửi yêu cầu GET đến URL: `https://www.example.com`
  - In ra mã trạng thái HTTP của phản hồi
  - In ra nội dung HTML của trang web
- Gợi ý:
  - Sử dụng phương thức `requests.get()` để gửi yêu cầu GET
  - Sử dụng thuộc tính `status_code` và `text` của đối tượng `Response` để lấy mã trạng thái HTTP và nội dung HTML
- Deadline: 1 tuần kể từ ngày bắt đầu bài tập

Khi hoàn thành bài tập, bạn sẽ có kiến thức cơ bản về cách sử dụng thư viện `requests` và có thể áp dụng vào các dự án thực tế.
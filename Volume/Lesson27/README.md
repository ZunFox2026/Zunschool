# Làm quen với thư viện Requests
## Giới thiệu
Thư viện Requests là một trong những thư viện phổ biến nhất trong Python, giúp bạn gửi yêu cầu HTTP và tương tác với các trang web một cách đơn giản. Trong bài này, chúng ta sẽ tìm hiểu về cách sử dụng thư viện Requests để gửi yêu cầu GET, POST, PUT, DELETE và cách xử lý các phản hồi từ máy chủ.

## Lý thuyết
Thư viện Requests cung cấp một số phương thức chính để gửi yêu cầu HTTP, bao gồm:
- `requests.get()`: Gửi yêu cầu GET đến máy chủ.
- `requests.post()`: Gửi yêu cầu POST đến máy chủ.
- `requests.put()`: Gửi yêu cầu PUT đến máy chủ.
- `requests.delete()`: Gửi yêu cầu DELETE đến máy chủ.

Mỗi phương thức này đều trả về một đối tượng `Response`, chứa thông tin về phản hồi từ máy chủ, bao gồm mã trạng thái, tiêu đề và nội dung phản hồi.

## Ví dụ
Dưới đây là một số ví dụ về cách sử dụng thư viện Requests:
- Gửi yêu cầu GET đến trang web google.com:
  ```python
import requests
response = requests.get('https://www.google.com')
print(response.status_code)  # In mã trạng thái của phản hồi
```
- Gửi yêu cầu POST đến máy chủ với dữ liệu:
  ```python
import requests
data = {'key': 'value'}
response = requests.post('https://example.com', data=data)
print(response.text)  # In nội dung phản hồi
```
- Gửi yêu cầu PUT để cập nhật dữ liệu:
  ```python
import requests
data = {'key': 'new_value'}
response = requests.put('https://example.com', data=data)
print(response.status_code)  # In mã trạng thái của phản hồi
```
- Gửi yêu cầu DELETE để xóa dữ liệu:
  ```python
import requests
response = requests.delete('https://example.com')
print(response.status_code)  # In mã trạng thái của phản hồi
```

## Bài tập
Để rèn luyện kỹ năng sử dụng thư viện Requests, bạn có thể thực hiện các bài tập sau:
- Gửi yêu cầu GET đến trang web yêu thích của bạn và in mã trạng thái của phản hồi.
- Tạo một máy chủ giả lập (ví dụ bằng Flask hoặc Django) và gửi yêu cầu POST đến máy chủ đó với dữ liệu.
- Sử dụng thư viện Requests để lấy dữ liệu từ một API công cộng (ví dụ như API về thời tiết hoặc giá cả chứng khoán) và in kết quả.
- Gửi yêu cầu PUT và DELETE đến máy chủ giả lập và kiểm tra kết quả.
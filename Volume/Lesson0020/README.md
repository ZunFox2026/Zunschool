# Làm quen với thư viện requests
## Giới thiệu
Thư viện requests là một trong những thư viện phổ biến nhất trong Python, giúp cho việc gửi và nhận dữ liệu từ các máy chủ web trở nên dễ dàng hơn. Thư viện này hỗ trợ các phương thức gửi yêu cầu HTTP như GET, POST, PUT, DELETE, v.v. và cung cấp các tính năng như xử lý cookie, header, và dữ liệu JSON.

## Lý thuyết
Để sử dụng thư viện requests, trước tiên bạn cần cài đặt nó vào môi trường Python của mình. Điều này có thể được thực hiện bằng cách chạy lệnh `pip install requests` trong cửa sổ lệnh. Sau khi cài đặt, bạn có thể nhập thư viện vào chương trình của mình bằng lệnh `import requests`.

Thư viện requests cung cấp nhiều phương thức để gửi yêu cầu HTTP, bao gồm:
- `requests.get()`: Gửi yêu cầu GET đến một URL.
- `requests.post()`: Gửi yêu cầu POST đến một URL.
- `requests.put()`: Gửi yêu cầu PUT đến một URL.
- `requests.delete()`: Gửi yêu cầu DELETE đến một URL.

Mỗi phương thức này đều trả về một đối tượng Response, chứa thông tin về kết quả của yêu cầu, bao gồm mã trạng thái HTTP, header, và nội dung phản hồi.

## Ví dụ
Dưới đây là một ví dụ về việc sử dụng thư viện requests để gửi yêu cầu GET đến trang chủ của Google:
```python
import requests

url = "https://www.google.com"
response = requests.get(url)

print("Mã trạng thái:", response.status_code)
print("Header:")
for key, value in response.headers.items():
    print(key, ":", value)
print("Nội dung phản hồi:")
print(response.text)
```
Trong ví dụ này, chúng ta gửi yêu cầu GET đến trang chủ của Google và in ra mã trạng thái, header, và nội dung phản hồi.

## Bài tập
Để làm quen với thư viện requests, bạn có thể thử các bài tập sau:
- Gửi yêu cầu GET đến một trang web và in ra nội dung phản hồi.
- Gửi yêu cầu POST đến một trang web với dữ liệu JSON và in ra nội dung phản hồi.
- Sử dụng thư viện requests để gửi yêu cầu DELETE đến một trang web và kiểm tra kết quả.
- Tìm hiểu về cách xử lý cookie và header trong thư viện requests và viết một ví dụ minh họa.

Bằng cách hoàn thành các bài tập này, bạn sẽ có thể làm quen với thư viện requests và sử dụng nó một cách hiệu quả trong các dự án của mình.
# Làm quen với thư viện Requests
## Giới thiệu
Thư viện Requests là một trong những thư viện phổ biến nhất trong Python, được sử dụng để gửi HTTP request và nhận response từ server. Với thư viện này, bạn có thể dễ dàng thực hiện các tác vụ như lấy dữ liệu từ một trang web, gửi dữ liệu đến server, hoặc thậm chí là tải file về máy tính.

Thư viện Requests cung cấp một cách đơn giản và trực quan để tương tác với các dịch vụ web, giúp bạn tiết kiệm thời gian và công sức khi làm việc với các ứng dụng web. Trong bài này, chúng ta sẽ tìm hiểu cách sử dụng thư viện Requests để gửi HTTP request và nhận response từ server.

## Lý thuyết
Để sử dụng thư viện Requests, bạn cần hiểu về các loại HTTP request và cách chúng được sử dụng. Có beberapa loại HTTP request phổ biến, bao gồm:

* GET: Lấy dữ liệu từ server
* POST: Gửi dữ liệu đến server
* PUT: Cập nhật dữ liệu trên server
* DELETE: Xóa dữ liệu trên server

Thư viện Requests cung cấp các phương thức tương ứng với từng loại HTTP request này, giúp bạn dễ dàng thực hiện các tác vụ trên.

Ngoài ra, thư viện Requests cũng cung cấp các tùy chọn để bạn có thể tùy chỉnh các thông số của HTTP request, như header, param, data, v.v.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng thư viện Requests để lấy dữ liệu từ một trang web:
```python
import requests

url = "https://www.example.com"
response = requests.get(url)

print(response.status_code)
print(response.text)
```
Trong ví dụ này, chúng ta sử dụng phương thức `get()` của thư viện Requests để gửi một HTTP GET request đến trang web `https://www.example.com`. Sau đó, chúng ta in ra status code và nội dung của response.

## Bài tập
Bài tập này yêu cầu bạn sử dụng thư viện Requests để lấy dữ liệu từ một trang web và in ra nội dung của response.

Yêu cầu:

* Lấy dữ liệu từ trang web `https://www.google.com`
* In ra status code của response
* In ra nội dung của response

Gợi ý:

* Sử dụng phương thức `get()` của thư viện Requests để gửi HTTP GET request đến trang web
* Sử dụng thuộc tính `status_code` và `text` của response để lấy status code và nội dung của response

Hãy thử thực hiện bài tập này và xem kết quả!
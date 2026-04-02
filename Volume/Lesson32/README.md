# Làm quen với thư viện Requests
## Giới thiệu
Thư viện Requests là một trong những thư viện phổ biến nhất trong Python, giúp bạn gửi yêu cầu HTTP và tương tác với các dịch vụ web một cách dễ dàng. Với Requests, bạn có thể gửi yêu cầu GET, POST, PUT, DELETE và nhiều phương thức khác, cũng như xử lý các phản hồi từ máy chủ.

Thư viện Requests cung cấp một giao diện đơn giản và trực quan, giúp bạn tiết kiệm thời gian và công sức khi làm việc với các dịch vụ web. Trong bài viết này, chúng ta sẽ tìm hiểu cách sử dụng thư viện Requests để gửi yêu cầu và xử lý phản hồi.

## Lý thuyết
Để sử dụng thư viện Requests, bạn cần hiểu một số khái niệm cơ bản về HTTP và cách thức hoạt động của thư viện. Dưới đây là một số điểm chính:

* **Yêu cầu HTTP**: Yêu cầu HTTP là một thông điệp được gửi từ máy khách (trình duyệt, ứng dụng) đến máy chủ để yêu cầu thực hiện một hành động cụ thể, chẳng hạn như lấy dữ liệu, gửi dữ liệu, cập nhật dữ liệu.
* **Phương thức HTTP**: Các phương thức HTTP phổ biến bao gồm GET, POST, PUT, DELETE, HEAD, OPTIONS, v.v.
* **Thư viện Requests**: Thư viện Requests cung cấp các chức năng để gửi yêu cầu HTTP và xử lý phản hồi từ máy chủ.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng thư viện Requests để gửi yêu cầu GET và lấy dữ liệu từ một trang web:
```python
import requests

# Gửi yêu cầu GET đến trang web
response = requests.get('https://www.example.com')

# Kiểm tra mã trạng thái của phản hồi
if response.status_code == 200:
    # Lấy dữ liệu từ phản hồi
    data = response.text
    print(data)
else:
    print('Lỗi:', response.status_code)
```
Trong ví dụ này, chúng ta sử dụng hàm `requests.get()` để gửi yêu cầu GET đến trang web `https://www.example.com`. Sau đó, chúng ta kiểm tra mã trạng thái của phản hồi bằng cách sử dụng thuộc tính `status_code` của đối tượng `response`. Nếu mã trạng thái là 200 (OK), chúng ta lấy dữ liệu từ phản hồi bằng cách sử dụng thuộc tính `text` của đối tượng `response`.

## Bài tập
Bài tập này yêu cầu bạn sử dụng thư viện Requests để gửi yêu cầu POST đến một trang web và lấy dữ liệu từ phản hồi. Các bước thực hiện như sau:

* Tìm kiếm một trang web có API công khai và cho phép gửi yêu cầu POST.
* Sử dụng hàm `requests.post()` để gửi yêu cầu POST đến trang web đó.
* Kiểm tra mã trạng thái của phản hồi và lấy dữ liệu từ phản hồi nếu cần.
* In ra dữ liệu đã lấy được.

Hãy thử thực hiện bài tập này và khám phá thêm về thư viện Requests và cách sử dụng nó trong các dự án thực tế.
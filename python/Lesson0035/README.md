# Xử lý hình ảnh
Bài học này sẽ giới thiệu về cách xử lý hình ảnh sử dụng thư viện Python. Chúng ta sẽ tìm hiểu về các khái niệm cơ bản, cách đọc và hiển thị hình ảnh, cũng như thực hiện các操作 cơ bản trên hình ảnh.

## Giới thiệu
Xử lý hình ảnh là một phần quan trọng trong nhiều lĩnh vực như máy tính, trí tuệ nhân tạo, và truyền thông đa phương tiện. Thư viện Python cung cấp nhiều công cụ và chức năng để giúp bạn xử lý hình ảnh một cách hiệu quả. Trong bài học này, chúng ta sẽ tập trung vào cách sử dụng thư viện Pillow, một trong những thư viện xử lý hình ảnh phổ biến nhất trong Python.

## Lý thuyết
Trước khi bắt đầu, chúng ta cần hiểu một số khái niệm cơ bản về hình ảnh. Hình ảnh được đại diện bởi một ma trận các điểm ảnh (pixel), mỗi điểm ảnh có giá trị màu sắc tương ứng. Các hình ảnh có thể được lưu trữ dưới nhiều định dạng khác nhau như JPEG, PNG, GIF, v.v. 

Thư viện Pillow cho phép bạn đọc và hiển thị hình ảnh, cũng như thực hiện các phép toán cơ bản như cắt, sao chép, và dán. Bạn cũng có thể sử dụng thư viện này để thay đổi kích thước hình ảnh, xoay hình ảnh, và áp dụng các hiệu ứng đặc biệt.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách đọc và hiển thị hình ảnh sử dụng thư viện Pillow:
```python
from PIL import Image

# Đọc hình ảnh từ tệp tin
image = Image.open('image.jpg')

# Hiển thị hình ảnh
image.show()
```
Trong ví dụ này, chúng ta sử dụng hàm `Image.open()` để đọc hình ảnh từ tệp tin 'image.jpg', sau đó sử dụng phương thức `show()` để hiển thị hình ảnh.

## Bài tập
Bài tập này yêu cầu bạn thực hiện các bước sau:

1. Cài đặt thư viện Pillow bằng cách chạy lệnh `pip install pillow` trong terminal.
2. Tạo một tệp tin Python mới và nhập thư viện Pillow.
3. Đọc hình ảnh từ tệp tin 'image.jpg' và hiển thị hình ảnh.
4. Thay đổi kích thước hình ảnh thành 50% kích thước ban đầu và hiển thị hình ảnh mới.
5. Xoay hình ảnh 45 độ và hiển thị hình ảnh mới.

Khi hoàn thành bài tập này, bạn sẽ hiểu rõ hơn về cách xử lý hình ảnh sử dụng thư viện Pillow và có thể áp dụng kiến thức này vào các dự án thực tế.
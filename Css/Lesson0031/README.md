# Bài 31: Tìm hiểu về Media Queries
## Giới thiệu
Media Queries là một tính năng trong CSS cho phép bạn áp dụng các kiểu dáng khác nhau tùy thuộc vào các điều kiện cụ thể của thiết bị hoặc trình duyệt. Điều này giúp bạn tạo ra các trang web và ứng dụng đáp ứng, có thể thích nghi với nhiều loại thiết bị và kích thước màn hình khác nhau. Trong bài học này, chúng ta sẽ tìm hiểu về cơ bản của Media Queries và cách sử dụng chúng trong thiết kế web.

## Lý thuyết
Media Queries dựa trên việc kiểm tra các điều kiện như chiều rộng và chiều cao của màn hình, hướng thiết bị (ngang hoặc dọc), độ phân giải, và nhiều yếu tố khác. Bạn có thể sử dụng `@media` trong CSS để định nghĩa các khối Media Queries. Ví dụ, để áp dụng một phong cách cho các màn hình có chiều rộng tối đa 768 pixel, bạn có thể viết:
```css
@media (max-width: 768px) {
  /* Các thuộc tính CSS ở đây sẽ được áp dụng khi chiều rộng màn hình không vượt quá 768px */
  body {
    background-color: lightblue;
  }
}
```
Điều này cho phép bạn điều khiển cách trang web của bạn trông như thế nào trên các thiết bị di động, máy tính bảng, hoặc máy tính để bàn.

## Ví dụ
Một ví dụ phổ biến về việc sử dụng Media Queries là điều chỉnh kích thước phông chữ và khoảng cách giữa các phần tử dựa trên kích thước màn hình. Ví dụ:
```css
@media (min-width: 1200px) {
  /* Đối với màn hình lớn */
  .container {
    font-size: 18px;
    padding: 20px;
  }
}

@media (max-width: 768px) {
  /* Đối với màn hình nhỏ */
  .container {
    font-size: 14px;
    padding: 10px;
  }
}
```
Điều này giúp đảm bảo rằng nội dung của bạn dễ đọc và dễ sử dụng trên nhiều thiết bị khác nhau.

## Bài tập
Bài tập cho bạn là tạo một trang web đơn giản có thể thay đổi màu nền và kích thước phông chữ dựa trên kích thước màn hình. Hãy thử áp dụng các kỹ thuật Media Queries đã học để tạo ra một trang web đáp ứng. Ví dụ, bạn có thể tạo một trang web có màu nền xanh khi xem trên điện thoại (chiều rộng màn hình dưới 768px), màu nền vàng khi xem trên máy tính bảng (chiều rộng màn hình từ 768px đến 1024px), và màu nền trắng khi xem trên máy tính để bàn (chiều rộng màn hình trên 1024px). Ngoài ra, hãy điều chỉnh kích thước phông chữ cho phù hợp với từng loại thiết bị. Sau khi hoàn thành, hãy thử nghiệm với các thiết bị hoặc trình duyệt khác nhau để xem kết quả.
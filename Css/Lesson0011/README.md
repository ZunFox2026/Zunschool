# Tìm hiểu về Media Query
## Giới thiệu
Media Query là một tính năng trong CSS cho phép developer định nghĩa các stylesheet khác nhau dựa trên các điều kiện cụ thể của thiết bị đầu cuối, chẳng hạn như độ rộng màn hình, độ phân giải, hướng màn hình,... Điều này giúp cho trang web có thể thích nghi với nhiều loại thiết bị và kích thước màn hình khác nhau, mang lại trải nghiệm người dùng tốt hơn.

## Lý thuyết
Media Query sử dụng câu lệnh `@media` trong CSS để xác định các điều kiện mà stylesheet sẽ được áp dụng. Cú pháp chung của Media Query là `@media loại_điều_kiện { /* stylesheet */ }`. Loại điều kiện thường được sử dụng bao gồm:
- `all`: Áp dụng cho tất cả các loại thiết bị.
- `screen`: Áp dụng cho các thiết bị hiển thị trên màn hình.
- `print`: Áp dụng cho các tài liệu được in ra.
- `max-width` và `min-width`: Áp dụng cho các thiết bị có độ rộng màn hình nhỏ hơn hoặc lớn hơn giá trị xác định.

Ví dụ:
```css
@media screen and (max-width: 768px) {
  body {
    background-color: #f2f2f2;
  }
}
```
Trong ví dụ trên, khi màn hình có độ rộng nhỏ hơn hoặc bằng 768px, màu nền của trang web sẽ được đổi thành #f2f2f2.

## Ví dụ
Một ví dụ khác về việc sử dụng Media Query để tạo layout đáp ứng:
```css
/* Định nghĩa layout cho màn hình lớn */
@media screen and (min-width: 1024px) {
  .container {
    width: 80%;
    margin: 0 auto;
  }
}

/* Định nghĩa layout cho màn hình nhỏ */
@media screen and (max-width: 768px) {
  .container {
    width: 100%;
    padding: 20px;
  }
}
```
Trong ví dụ này, khi màn hình có độ rộng lớn hơn hoặc bằng 1024px, container sẽ có chiều rộng 80% và được căn giữa. Khi màn hình có độ rộng nhỏ hơn hoặc bằng 768px, container sẽ có chiều rộng 100% và có padding 20px.

## Bài tập
Bài tập cho bạn:
- Tạo một trang web đơn giản với một div có class `box`.
- Sử dụng Media Query để đổi màu nền của div `box` khi màn hình có độ rộng nhỏ hơn 600px.
- Thêm một điều kiện để khi màn hình có độ rộng lớn hơn 1200px, div `box` sẽ có chiều rộng 50% và được căn giữa.
Hãy thử nghiệm và khám phá các khả năng của Media Query trong việc tạo ra các trang web đáp ứng!
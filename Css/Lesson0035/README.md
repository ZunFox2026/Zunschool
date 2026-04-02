# Tìm hiểu về Media Queries
## Giới thiệu
Media Queries là một tính năng trong CSS cho phép chúng ta áp dụng các kiểu dáng khác nhau dựa trên các điều kiện cụ thể của thiết bị hoặc trình duyệt. Điều này giúp chúng ta tạo ra các trang web và ứng dụng đáp ứng, có thể thích nghi với nhiều loại thiết bị và kích thước màn hình khác nhau. Trong bài này, chúng ta sẽ tìm hiểu về cơ bản của Media Queries và cách sử dụng chúng trong thiết kế web.

## Lý thuyết
Media Queries sử dụng cú pháp `@media` trong CSS để xác định các điều kiện mà các kiểu dáng sẽ được áp dụng. Các điều kiện này có thể bao gồm kích thước màn hình, hướng của thiết bị, độ phân giải, v.v. Ví dụ, chúng ta có thể sử dụng Media Queries để áp dụng các kiểu dáng khác nhau cho các thiết bị di động và máy tính bảng. Ví dụ:
```css
@media (max-width: 768px) {
  /* Các kiểu dáng cho thiết bị di động */
  body {
    font-size: 16px;
  }
}

@media (min-width: 769px) và (max-width: 1024px) {
  /* Các kiểu dáng cho máy tính bảng */
  body {
    font-size: 18px;
  }
}
```
Trong ví dụ trên, chúng ta sử dụng `@media` để xác định các điều kiện cho kích thước màn hình. Nếu kích thước màn hình nhỏ hơn hoặc bằng 768px, các kiểu dáng trong khối `@media` đầu tiên sẽ được áp dụng. Nếu kích thước màn hình nằm trong khoảng từ 769px đến 1024px, các kiểu dáng trong khối `@media` thứ hai sẽ được áp dụng.

## Ví dụ
Giả sử chúng ta muốn tạo một trang web có thể hiển thị khác nhau trên các thiết bị di động và máy tính để bàn. Chúng ta có thể sử dụng Media Queries để áp dụng các kiểu dáng khác nhau dựa trên kích thước màn hình. Ví dụ:
```css
/* Các kiểu dáng cho máy tính để bàn */
body {
  font-size: 20px;
  background-color: #f2f2f2;
}

/* Các kiểu dáng cho thiết bị di động */
@media (max-width: 768px) {
  body {
    font-size: 16px;
    background-color: #ccc;
  }
}
```
Trong ví dụ trên, chúng ta áp dụng các kiểu dáng khác nhau cho máy tính để bàn và thiết bị di động. Trên máy tính để bàn, font size là 20px và màu nền là #f2f2f2. Trên thiết bị di động, font size là 16px và màu nền là #ccc.

## Bài tập
Bài tập này yêu cầu bạn tạo một trang web đơn giản có thể hiển thị khác nhau trên các thiết bị di động và máy tính để bàn. Sử dụng Media Queries để áp dụng các kiểu dáng khác nhau dựa trên kích thước màn hình. Ví dụ, bạn có thể tạo một trang web có tiêu đề, hình ảnh và đoạn văn. Trên máy tính để bàn, tiêu đề có thể có font size lớn, hình ảnh có thể có kích thước lớn, và đoạn văn có thể có font size lớn. Trên thiết bị di động, tiêu đề có thể có font size nhỏ, hình ảnh có thể có kích thước nhỏ, và đoạn văn có thể có font size nhỏ. Hãy thử nghiệm với các kiểu dáng khác nhau và xem kết quả trên các thiết bị khác nhau.
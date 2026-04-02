# Tìm hiểu về Media Queries
## Giới thiệu
Media Queries là một tính năng trong CSS cho phép chúng ta áp dụng các kiểu樣 khác nhau dựa trên các điều kiện cụ thể của thiết bị hoặc môi trường mà trang web được hiển thị. Điều này giúp chúng ta tạo ra các trang web có khả năng thích nghi với nhiều loại thiết bị và kích thước màn hình khác nhau. Ví dụ, bạn có thể sử dụng Media Queries để tạo ra một thiết kế riêng biệt cho phiên bản di động và phiên bản máy tính bảng của trang web.

## Lý thuyết
Media Queries hoạt động dựa trên việc kiểm tra các điều kiện cụ thể của thiết bị, chẳng hạn như chiều rộng và chiều cao của màn hình, độ phân giải, hướng màn hình (nằm ngang hoặc đứng),... Sau đó, nếu điều kiện được thỏa mãn, các kiểu样 được định nghĩa trong khối Media Queries sẽ được áp dụng. Cú pháp cơ bản của Media Queries là `@media <kiểu_trạng_thái> { /* mã CSS */ }`, trong đó `<kiểu_trạng_thái>` có thể là `screen`, `print`, `all`,... hoặc các điều kiện cụ thể như `max-width`, `min-width`,...

Ví dụ về một Media Query đơn giản:
```css
@media (max-width: 768px) {
  body {
    background-color: lightblue;
  }
}
```
Trong ví dụ này, khi chiều rộng của màn hình nhỏ hơn hoặc bằng 768px, màu nền của trang web sẽ được đổi thành lightblue.

## Ví dụ
Giả sử chúng ta muốn tạo một trang web có thể thích nghi với cả thiết bị di động và máy tính. Chúng ta có thể sử dụng Media Queries để thay đổi kích thước font chữ và chiều rộng của các phần tử dựa trên chiều rộng của màn hình.

```css
/* Định nghĩa kiểu mặc định */
body {
  font-size: 16px;
}

/* Áp dụng cho màn hình có chiều rộng nhỏ hơn 768px */
@media (max-width: 768px) {
  body {
    font-size: 14px;
  }
  .container {
    width: 90%;
  }
}

/* Áp dụng cho màn hình có chiều rộng lớn hơn 1200px */
@media (min-width: 1200px) {
  body {
    font-size: 18px;
  }
  .container {
    width: 70%;
  }
}
```
Trong ví dụ này, khi chiều rộng của màn hình nhỏ hơn 768px, font chữ sẽ nhỏ hơn và chiều rộng của `.container` sẽ rộng hơn. Ngược lại, khi chiều rộng của màn hình lớn hơn 1200px, font chữ sẽ lớn hơn và chiều rộng của `.container` sẽ hẹp hơn.

## Bài tập
Bài tập này yêu cầu bạn tạo một trang web đơn giản có thể thích nghi với cả thiết bị di động và máy tính. Hãy sử dụng Media Queries để thay đổi:

- Kích thước font chữ của tiêu đề (`h1`) dựa trên chiều rộng của màn hình.
- Chiều rộng của một phần tử div (`#content`) dựa trên chiều rộng của màn hình.

Yêu cầu:
- Đối với màn hình di động (chiều rộng nhỏ hơn 600px), font chữ của tiêu đề nên là 18px và chiều rộng của `#content` nên là 100% của chiều rộng màn hình.
- Đối với màn hình máy tính (chiều rộng lớn hơn 1200px), font chữ của tiêu đề nên là 24px và chiều rộng của `#content` nên là 80% của chiều rộng màn hình.

Hãy thử nghiệm và điều chỉnh các giá trị để xem sự thay đổi trong thiết kế của trang web khi sử dụng trên các thiết bị khác nhau.
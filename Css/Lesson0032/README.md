# Tạo hình nền
Bài học này sẽ hướng dẫn bạn cách tạo hình nền cho một trang web bằng CSS.

## Giới thiệu
Hình nền là một phần quan trọng trong thiết kế trang web, giúp tạo ấn tượng và thu hút người dùng. Với CSS, bạn có thể dễ dàng tạo hình nền cho trang web của mình bằng cách sử dụng thuộc tính `background`. Trong bài học này, chúng ta sẽ tìm hiểu cách tạo hình nền cơ bản và một số kỹ thuật nâng cao.

## Lý thuyết
Để tạo hình nền, bạn cần sử dụng thuộc tính `background` trong CSS. Thuộc tính này cho phép bạn đặt hình nền cho một phần tử HTML. Có nhiều cách để đặt hình nền, bao gồm:
- Đặt hình nền bằng màu sắc: Bạn có thể sử dụng thuộc tính `background-color` để đặt màu sắc cho hình nền.
- Đặt hình nền bằng hình ảnh: Bạn có thể sử dụng thuộc tính `background-image` để đặt hình ảnh cho hình nền.
- Đặt hình nền bằng gradient: Bạn có thể sử dụng thuộc tính `background-image` với giá trị là một gradient để tạo hình nền gradient.

Ví dụ:
```css
body {
  background-color: #f2f2f2; /* Đặt màu sắc cho hình nền */
}

.div {
  background-image: url('hinhnen.jpg'); /* Đặt hình ảnh cho hình nền */
  background-repeat: no-repeat; /* Không lặp lại hình nền */
  background-size: cover; /* Đặt kích thước hình nền */
}
```

## Ví dụ
Chúng ta sẽ tạo một trang web có hình nền là một hình ảnh. Chúng ta sẽ sử dụng thuộc tính `background-image` để đặt hình ảnh cho hình nền.
```css
body {
  background-image: url('hinhnen.jpg');
  background-repeat: no-repeat;
  background-size: cover;
}
```
Kết quả là trang web của chúng ta sẽ có hình nền là hình ảnh `hinhnen.jpg`.

## Bài tập
Bài tập này sẽ yêu cầu bạn tạo một trang web có hình nền là một hình ảnh. Hãy thực hiện các bước sau:
- Tạo một tệp HTML và thêm một phần tử `div` vào đó.
- Tạo một tệp CSS và thêm thuộc tính `background-image` vào phần tử `div` để đặt hình ảnh cho hình nền.
- Thử nghiệm với các thuộc tính `background-repeat` và `background-size` để tạo hiệu ứng khác nhau.
- Đặt màu sắc cho hình nền bằng thuộc tính `background-color` và thử nghiệm với các giá trị khác nhau.
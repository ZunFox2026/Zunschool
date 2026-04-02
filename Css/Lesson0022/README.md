# Tạo hình ảnh nền động
## Giới thiệu
Tạo hình ảnh nền động là một kỹ thuật được sử dụng trong thiết kế web để tạo ra các hiệu ứng hình ảnh động thú vị và hấp dẫn. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hình ảnh nền động bằng cách sử dụng CSS. Bài học này sẽ giúp bạn hiểu cách sử dụng các thuộc tính CSS để tạo ra các hiệu ứng hình ảnh động cơ bản.

## Lý thuyết
Để tạo hình ảnh nền động, chúng ta cần sử dụng các thuộc tính CSS sau:
- `background-image`: để đặt hình ảnh nền
- `background-size`: để đặt kích thước hình ảnh nền
- `background-position`: để đặt vị trí hình ảnh nền
- `animation`: để tạo hiệu ứng động

Ví dụ, để tạo hình ảnh nền động, chúng ta có thể sử dụng mã CSS sau:
```css
.nen-dong {
  background-image: linear-gradient(to right, #ff0000, #00ff00);
  background-size: 400px 200px;
  background-position: 0% 0%;
  animation: dong 10s infinite;
}

@keyframes dong {
  0% {
    background-position: 0% 0%;
  }
  100% {
    background-position: 100% 0%;
  }
}
```
Trong ví dụ trên, chúng ta tạo một lớp `.nen-dong` với hình ảnh nền động sử dụng `linear-gradient`. Hình ảnh nền sẽ di chuyển từ trái sang phải trong vòng 10 giây và lặp lại mãi mãi.

## Ví dụ
Chúng ta có thể áp dụng kỹ thuật tạo hình ảnh nền động vào các trang web để tạo ra các hiệu ứng thú vị. Ví dụ, chúng ta có thể tạo một trang web với hình ảnh nền động như sau:
```css
.body {
  background-image: url('nen.jpg');
  background-size: cover;
  background-position: center;
  animation: zoom 10s infinite;
}

@keyframes zoom {
  0% {
    transform: scale(1);
  }
  100% {
    transform: scale(1.2);
  }
}
```
Trong ví dụ trên, chúng ta tạo một trang web với hình ảnh nền động bằng cách sử dụng thuộc tính `background-image` và `animation`. Hình ảnh nền sẽ được thu phóng từ 1 đến 1.2 trong vòng 10 giây và lặp lại mãi mãi.

## Bài tập
Bài tập cho bạn là tạo một trang web với hình ảnh nền động bằng cách sử dụng các thuộc tính CSS đã học. Hãy thử nghiệm với các hiệu ứng khác nhau, chẳng hạn như di chuyển, thu phóng, hoặc xoay hình ảnh nền. Bạn cũng có thể sử dụng các công cụ thiết kế web như Adobe XD hoặc Figma để tạo ra các thiết kế phức tạp hơn. Khi hoàn thành, hãy chia sẻ kết quả của bạn với mọi người và nhận xét về các hiệu ứng hình ảnh động mà bạn đã tạo ra.
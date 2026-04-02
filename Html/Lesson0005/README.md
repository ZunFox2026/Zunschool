# Tạo hình nền động
## Giới thiệu
Tạo hình nền động là một kỹ thuật được sử dụng trong thiết kế web để tạo ra các hình nền có hiệu ứng động, giúp trang web trở nên sinh động và hấp dẫn hơn. Trong bài học này, chúng ta sẽ tìm hiểu về cách tạo hình nền động bằng sử dụng HTML và CSS.

## Lý thuyết
Để tạo hình nền động, chúng ta có thể sử dụng thuộc tính `background` trong CSS. Chúng ta có thể sử dụng thuộc tính này để đặt một hình ảnh làm hình nền cho một phần tử HTML. Để tạo hiệu ứng động, chúng ta có thể sử dụng thuộc tính `animation` trong CSS. Thuộc tính này cho phép chúng ta tạo ra các hiệu ứng động cho các phần tử HTML.

Ví dụ, chúng ta có thể sử dụng mã HTML và CSS sau để tạo một hình nền động:
```html
<div class="background"></div>
```

```css
.background {
  background-image: linear-gradient(to right, #f00, #0f0, #00f);
  background-size: 100% 100%;
  animation: move 10s infinite;
}

@keyframes move {
  0% {
    background-position: 0% 0%;
  }
  100% {
    background-position: 100% 100%;
  }
}
```
Trong ví dụ trên, chúng ta sử dụng thuộc tính `background-image` để đặt một hình ảnh linear gradient làm hình nền. Chúng ta cũng sử dụng thuộc tính `animation` để tạo ra hiệu ứng động cho hình nền. Hiệu ứng động này sẽ di chuyển hình nền từ trái sang phải trong vòng 10 giây.

## Ví dụ
Chúng ta cũng có thể sử dụng mã HTML và CSS sau để tạo một hình nền động khác:
```html
<div class="background2"></div>
```

```css
.background2 {
  background-image: url('image.jpg');
  background-size: cover;
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
Trong ví dụ trên, chúng ta sử dụng thuộc tính `background-image` để đặt một hình ảnh làm hình nền. Chúng ta cũng sử dụng thuộc tính `animation` để tạo ra hiệu ứng động cho hình nền. Hiệu ứng động này sẽ thu phóng hình nền lên trong vòng 10 giây.

## Bài tập
Bài tập cho bạn là tạo một hình nền động bằng sử dụng HTML và CSS. Bạn có thể sử dụng các thuộc tính `background` và `animation` để tạo ra các hiệu ứng động khác nhau. Hãy thử nghiệm với các mã HTML và CSS khác nhau để tạo ra các hình nền động khác nhau. Bạn cũng có thể sử dụng các hình ảnh khác nhau để đặt làm hình nền. Hãy nhớ rằng, bạn có thể sử dụng thuộc tính `animation` để tạo ra các hiệu ứng động cho các phần tử HTML khác nhau, không chỉ là hình nền.
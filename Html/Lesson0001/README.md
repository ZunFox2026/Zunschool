# Tạo Hình Nền Động
Bài viết này hướng dẫn cách tạo hình nền động cơ bản bằng HTML và CSS.

## Giới thiệu
Hình nền động là một phần quan trọng trong thiết kế web, giúp trang web trở nên sinh động và thu hút người dùng. Với sự hỗ trợ của HTML và CSS, bạn có thể tạo ra các hình nền động đơn giản mà không cần sử dụng đến các công nghệ phức tạp như JavaScript. Trong bài viết này, chúng ta sẽ tìm hiểu cách tạo hình nền động cơ bản bằng HTML và CSS.

## Lý thuyết
Để tạo hình nền động, chúng ta sẽ sử dụng CSS để định nghĩa các kiểu dáng và hoạt ảnh cho hình nền. Chúng ta sẽ sử dụng thuộc tính `background` để đặt hình nền, và thuộc tính `animation` để tạo hoạt ảnh. Ví dụ:
```html
<div class="hinh-nen"></div>
```

```css
.hinh-nen {
  width: 100%;
  height: 100vh;
  background-image: linear-gradient(to right, #ff0000, #00ff00, #0000ff);
  background-size: 1000px 1000px;
  animation: hinh-nen-dong 10s ease infinite;
}

@keyframes hinh-nen-dong {
  0% {
    background-position: 0% 0%;
  }
  50% {
    background-position: 100% 100%;
  }
  100% {
    background-position: 0% 0%;
  }
}
```
Trong ví dụ trên, chúng ta đã tạo một div với lớp `.hinh-nen`, và định nghĩa kiểu dáng cho lớp này bằng CSS. Chúng ta đã sử dụng thuộc tính `background-image` để đặt hình nền là một dải màu, và thuộc tính `animation` để tạo hoạt ảnh cho hình nền.

## Ví dụ
Chúng ta có thể tạo nhiều loại hình nền động khác nhau bằng cách thay đổi thuộc tính `background-image` và `animation`. Ví dụ, chúng ta có thể tạo hình nền động với hình ảnh như sau:
```html
<div class="hinh-nen-2"></div>
```

```css
.hinh-nen-2 {
  width: 100%;
  height: 100vh;
  background-image: url('hinh-nen.jpg');
  background-size: cover;
  animation: hinh-nen-dong-2 10s ease infinite;
}

@keyframes hinh-nen-dong-2 {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}
```
Trong ví dụ trên, chúng ta đã tạo một div với lớp `.hinh-nen-2`, và định nghĩa kiểu dáng cho lớp này bằng CSS. Chúng ta đã sử dụng thuộc tính `background-image` để đặt hình nền là một hình ảnh, và thuộc tính `animation` để tạo hoạt ảnh cho hình nền.

## Bài tập
Bài tập cho bạn là tạo một hình nền động với hình ảnh hoặc màu sắc tự chọn. Hãy thử nghiệm với các thuộc tính `background-image`, `background-size`, `animation` để tạo ra các hiệu ứng khác nhau. Bạn có thể sử dụng các công cụ như CodePen hoặc JSFiddle để thử nghiệm và chia sẻ kết quả với mọi người.
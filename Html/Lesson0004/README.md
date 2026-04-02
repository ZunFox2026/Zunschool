# Tạo hiệu ứng hình ảnh
## Giới thiệu
Bài học này sẽ hướng dẫn bạn cách tạo hiệu ứng hình ảnh đơn giản bằng HTML và CSS. Bạn sẽ học cách thêm hiệu ứng vào hình ảnh, chẳng hạn như hiệu ứng hover, hiệu ứng chuyển động, và hiệu ứng bóng. Những kỹ năng này sẽ giúp bạn tạo ra các trang web hấp dẫn và thu hút người dùng.

## Lý thuyết
Để tạo hiệu ứng hình ảnh, bạn cần hiểu về các thuộc tính CSS sau:
- `transition`: thuộc tính này cho phép bạn tạo hiệu ứng chuyển đổi giữa các trạng thái khác nhau của phần tử.
- `transform`: thuộc tính này cho phép bạn thay đổi hình dạng và kích thước của phần tử.
- `box-shadow`: thuộc tính này cho phép bạn tạo bóng cho phần tử.
- `opacity`: thuộc tính này cho phép bạn điều chỉnh độ trong suốt của phần tử.
- `hover`: trạng thái này được kích hoạt khi người dùng di chuột qua phần tử.

Ví dụ, để tạo hiệu ứng hover cho hình ảnh, bạn có thể sử dụng código sau:
```html
<img src="image.jpg" class="image">
```
```css
.image {
  transition: transform 0.5s;
}

.image:hover {
  transform: scale(1.1);
}
```
Trong ví dụ trên, khi người dùng di chuột qua hình ảnh, hình ảnh sẽ được phóng to lên 1.1 lần.

## Ví dụ
Dưới đây là một ví dụ về tạo hiệu ứng hình ảnh bằng CSS:
```html
<div class="container">
  <img src="image.jpg" class="image">
</div>
```
```css
.container {
  width: 500px;
  height: 300px;
  margin: 40px auto;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s, box-shadow 0.5s;
}

.image:hover {
  transform: scale(1.1);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
```
Trong ví dụ trên, khi người dùng di chuột qua hình ảnh, hình ảnh sẽ được phóng to lên 1.1 lần và có bóng xung quanh.

## Bài tập
Bài tập này sẽ yêu cầu bạn tạo hiệu ứng hình ảnh bằng CSS. Hãy tạo một trang web với một hình ảnh và thêm hiệu ứng hover vào hình ảnh đó. Khi người dùng di chuột qua hình ảnh, hình ảnh nên được phóng to lên 1.2 lần và có bóng xung quanh. Ngoài ra, bạn cũng nên thêm hiệu ứng chuyển động vào hình ảnh khi người dùng di chuột qua.
```html
<div class="container">
  <img src="image.jpg" class="image">
</div>
```
Hãy tự viết mã CSS để tạo hiệu ứng hình ảnh như mô tả trên. Sau khi hoàn thành, bạn sẽ có một trang web với hình ảnh có hiệu ứng hover và chuyển động.
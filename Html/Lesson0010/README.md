# Tạo hiệu ứng hình ảnh
## Giới thiệu
Trong thiết kế web, việc tạo hiệu ứng hình ảnh là một phần quan trọng để làm cho trang web trở nên hấp dẫn và sinh động hơn. Với sự hỗ trợ của HTML và CSS, chúng ta có thể tạo ra nhiều hiệu ứng hình ảnh khác nhau, từ đơn giản đến phức tạp. Bài viết này sẽ hướng dẫn bạn cách tạo hiệu ứng hình ảnh cơ bản bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng hình ảnh, chúng ta thường sử dụng các thuộc tính CSS như `opacity`, `transform`, `transition`,... Trong đó:
- `opacity` được dùng để điều chỉnh độ trong suốt của hình ảnh.
- `transform` được dùng để thực hiện các phép biến đổi như xoay, lật, thay đổi kích thước hình ảnh.
- `transition` được dùng để tạo hiệu ứng chuyển tiếp mượt mà giữa các trạng thái khác nhau.
Ví dụ, chúng ta có thể tạo hiệu ứng mờ hình ảnh khi di chuột qua bằng cách sử dụng `opacity` và `transition` như sau:
```html
<img src="image.jpg" alt="Hình ảnh" style="opacity: 0.5; transition: opacity 0.5s;">
```
```css
img:hover {
  opacity: 1;
}
```

## Ví dụ
Chúng ta có thể tạo hiệu ứng hình ảnh bằng cách kết hợp các thuộc tính CSS khác nhau. Ví dụ, tạo hiệu ứng xoay hình ảnh khi di chuột qua:
```html
<img src="image.jpg" alt="Hình ảnh" class="image-rotate">
```
```css
.image-rotate {
  transition: transform 0.5s;
}

.image-rotate:hover {
  transform: rotate(360deg);
}
```
Hoặc tạo hiệu ứng thay đổi kích thước hình ảnh khi di chuột qua:
```html
<img src="image.jpg" alt="Hình ảnh" class="image-zoom">
```
```css
.image-zoom {
  transition: transform 0.5s;
}

.image-zoom:hover {
  transform: scale(1.2);
}
```

## Bài tập
Bài tập này yêu cầu bạn tạo hiệu ứng hình ảnh cho một trang web đơn giản. Hãy thực hiện các bước sau:
- Tạo một trang web mới với một hình ảnh.
- Thêm hiệu ứng mờ hình ảnh khi di chuột qua bằng cách sử dụng `opacity` và `transition`.
- Thêm hiệu ứng xoay hình ảnh khi di chuột qua bằng cách sử dụng `transform` và `transition`.
- Thêm hiệu ứng thay đổi kích thước hình ảnh khi di chuột qua bằng cách sử dụng `transform` và `transition`.
- Chạy thử trang web và kiểm tra các hiệu ứng hình ảnh.
Khi hoàn thành bài tập này, bạn sẽ có kiến thức cơ bản về tạo hiệu ứng hình ảnh bằng HTML và CSS, và có thể áp dụng vào các dự án web thực tế.
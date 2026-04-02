# Tìm hiểu về Accessibility trong CSS
## Giới thiệu
Accessibility (tính năng tiếp cận) là một phần quan trọng trong thiết kế web, đảm bảo rằng trang web của bạn có thể được sử dụng bởi mọi người, bao gồm cả những người có khả năng tiếp cận hạn chế. Trong CSS, chúng ta có thể áp dụng các kỹ thuật và thuộc tính để cải thiện tính năng tiếp cận của trang web. Bài viết này sẽ giới thiệu về tính năng tiếp cận trong CSS và cách áp dụng chúng.

## Lý thuyết
Tính năng tiếp cận trong CSS liên quan đến việc thiết kế trang web để mọi người có thể sử dụng, bao gồm cả những người có khả năng tiếp cận hạn chế. Một số nguyên tắc cơ bản của tính năng tiếp cận trong CSS bao gồm:
* Sử dụng màu sắc và độ tương phản phù hợp để đảm bảo nội dung dễ đọc.
* Cung cấp替 thế cho nội dung đa phương tiện, chẳng hạn như ảnh và video.
* Sử dụng semantic HTML để cung cấp cấu trúc cho trang web.
* Áp dụng các thuộc tính ARIA (Accessible Rich Internet Applications) để cung cấp thông tin cho người dùng về các thành phần và tính năng của trang web.

Ví dụ, chúng ta có thể sử dụng thuộc tính `color` và `background-color` để đảm bảo độ tương phản giữa văn bản và nền:
```css
body {
  color: #333;
  background-color: #f9f9f9;
}
```
Hoặc sử dụng thuộc tính `alt` để cung cấp thay thế cho ảnh:
```css
img {
  alt: "Ảnh minh họa";
}
```
## Ví dụ
Một ví dụ về tính năng tiếp cận trong CSS là sử dụng thuộc tính `:focus` để tạo kiểu cho các phần tử khi chúng nhận được tiêu điểm. Điều này giúp người dùng có thể dễ dàng xác định được phần tử đang được tập trung:
```css
button:focus {
  outline: 2px solid #333;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}
```
Một ví dụ khác là sử dụng thuộc tính `font-size` và `line-height` để đảm bảo văn bản dễ đọc:
```css
body {
  font-size: 16px;
  line-height: 1.5;
}
```
## Bài tập
Bài tập này yêu cầu bạn áp dụng các kỹ thuật tính năng tiếp cận trong CSS vào một trang web. Hãy tạo một trang web đơn giản với một số phần tử, chẳng hạn như tiêu đề, đoạn văn, ảnh và nút. Áp dụng các thuộc tính và kỹ thuật tính năng tiếp cận để đảm bảo trang web của bạn có thể được sử dụng bởi mọi người.
* Sử dụng màu sắc và độ tương phản phù hợp.
* Cung cấp thay thế cho nội dung đa phương tiện.
* Sử dụng semantic HTML để cung cấp cấu trúc cho trang web.
* Áp dụng các thuộc tính ARIA để cung cấp thông tin cho người dùng.
Hãy thử nghiệm và áp dụng các kỹ thuật tính năng tiếp cận trong CSS để tạo ra một trang web thân thiện với người dùng.
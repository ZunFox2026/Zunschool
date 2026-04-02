# Tìm hiểu về Accessibility
## Giới thiệu
Khả năng tiếp cận (Accessibility) là một trong những yếu tố quan trọng trong thiết kế web hiện đại. Nó không chỉ giúp người dùng có thể dễ dàng truy cập và sử dụng trang web mà còn giúp tăng cường trải nghiệm người dùng. Trong bài này, chúng ta sẽ tìm hiểu về khả năng tiếp cận và cách áp dụng nó vào thiết kế web bằng CSS.

## Lý thuyết
Khả năng tiếp cận trong thiết kế web bao gồm nhiều khía cạnh khác nhau, bao gồm màu sắc, kích thước chữ, khoảng cách giữa các yếu tố,... Màu sắc là một trong những yếu tố quan trọng nhất, vì nó có thể ảnh hưởng đến khả năng đọc và hiểu của người dùng. Ví dụ, nếu màu nền và màu chữ слишком tương tự, người dùng có thể gặp khó khăn khi đọc nội dung. Chúng ta có thể sử dụng CSS để thiết lập màu sắc và kích thước chữ phù hợp, chẳng hạn như:
```css
body {
    background-color: #f2f2f2;
    color: #333;
    font-size: 16px;
}
```
Bên cạnh đó, chúng ta cũng cần đảm bảo rằng các yếu tố trên trang web có khoảng cách hợp lý để người dùng có thể dễ dàng đọc và hiểu. Ví dụ:
```css
p {
    margin-bottom: 20px;
}
```
## Ví dụ
Chúng ta có thể áp dụng khả năng tiếp cận vào một trang web đơn giản. Ví dụ, chúng ta có một trang web với nội dung sau:
```html
<h1>Tiêu đề</h1>
<p>Nội dung</p>
```
Chúng ta có thể sử dụng CSS để thiết lập màu sắc, kích thước chữ và khoảng cách giữa các yếu tố:
```css
h1 {
    color: #00698f;
    font-size: 24px;
    margin-bottom: 10px;
}

p {
    color: #666;
    font-size: 18px;
    margin-bottom: 20px;
}
```
Kết quả sẽ là một trang web với nội dung dễ đọc và hiểu.

## Bài tập
Bài tập cho bạn là tạo một trang web đơn giản với nội dung sau:
```html
<h1>Tiêu đề</h1>
<p>Nội dung</p>
<a href="#">Liên kết</a>
```
Sử dụng CSS để thiết lập màu sắc, kích thước chữ và khoảng cách giữa các yếu tố. Đảm bảo rằng trang web của bạn có khả năng tiếp cận cao và dễ sử dụng. Bạn có thể tham khảo các ví dụ trên và tự tạo ra một thiết kế独 đáo.
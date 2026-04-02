# Tìm hiểu về Media Query
## Giới thiệu
Media Query là một công cụ mạnh mẽ trong CSS giúp các nhà thiết kế web tạo ra các trang web đáp ứng, có thể tự động điều chỉnh giao diện và bố cục dựa trên kích thước màn hình, thiết bị và hướng của thiết bị. Với Media Query, bạn có thể viết các đoạn mã CSS khác nhau cho các loại thiết bị và kích thước màn hình khác nhau, giúp trang web của bạn trở nên linh hoạt và đẹp hơn trên mọi thiết bị.

## Lý thuyết
Media Query dựa trên việc sử dụng các điều kiện để áp dụng các đoạn mã CSS. Các điều kiện này thường liên quan đến các thuộc tính như chiều rộng và chiều cao của màn hình, loại thiết bị (máy tính để bàn, máy tính bảng, điện thoại di động), hướng của thiết bị (nằm ngang hoặc đứng) và nhiều yếu tố khác. Một Media Query cơ bản có thể được viết như sau:
```css
@media (max-width: 768px) {
  /* mã CSS sẽ được áp dụng khi chiều rộng màn hình nhỏ hơn hoặc bằng 768px */
}
```
Điều này cho phép bạn áp dụng các phong cách khác nhau tùy thuộc vào kích thước màn hình, giúp tạo ra một trải nghiệm người dùng đồng nhất trên nhiều thiết bị.

## Ví dụ
Để minh họa cách sử dụng Media Query, hãy xét một ví dụ về việc tạo một trang web có thanh điều hướng. Trên máy tính để bàn, bạn muốn thanh điều hướng có chiều rộng cố định, nhưng trên điện thoại di động, bạn muốn nó chiếm toàn bộ chiều rộng màn hình. Bạn có thể viết CSS như sau:
```css
/* CSS mặc định cho máy tính để bàn */
.navbar {
  width: 800px;
  margin: 0 auto;
}

/* Áp dụng Media Query cho điện thoại di động */
@media (max-width: 480px) {
  .navbar {
    width: 100%;
  }
}
```
 Trong ví dụ này, khi chiều rộng màn hình nhỏ hơn hoặc bằng 480px (thường là kích thước của điện thoại di động), thanh điều hướng sẽ chiếm toàn bộ chiều rộng màn hình.

## Bài tập
Để thực hành sử dụng Media Query, bạn có thể thực hiện các bài tập sau:
- Tạo một trang web có một cột văn bản. Sử dụng Media Query để khi chiều rộng màn hình nhỏ hơn 600px, văn bản sẽ có kích thước chữ nhỏ hơn.
- Thiết kế một trang web có hình ảnh. Áp dụng Media Query để khi chiều rộng màn hình nhỏ hơn 800px, hình ảnh sẽ được thu nhỏ lại.
- Tạo một trang web có menu điều hướng. Sử dụng Media Query để khi chiều rộng màn hình nhỏ hơn 400px, menu sẽ được ẩn đi và chỉ hiển thị khi người dùng click vào một nút cụ thể.

Bằng cách hoàn thành các bài tập này, bạn sẽ có thể nắm vững cách sử dụng Media Query để tạo ra các trang web đáp ứng và linh hoạt.
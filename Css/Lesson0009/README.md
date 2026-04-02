# Tạo Hình Nền
Bài học này sẽ hướng dẫn cách tạo hình nền cho trang web bằng CSS.

## Giới thiệu
Hình nền là một phần quan trọng của thiết kế web, giúp tạo ra ấn tượng và phong cách riêng cho trang web. Với CSS, bạn có thể dễ dàng tạo hình nền bằng cách sử dụng thuộc tính `background`. Trong bài học này, chúng ta sẽ tìm hiểu cách tạo hình nền cơ bản và một số kỹ thuật nâng cao.

## Lý thuyết
Để tạo hình nền, bạn cần sử dụng thuộc tính `background` trong CSS. Có nhiều loại hình nền khác nhau, bao gồm:
- Hình nền màu sắc: Sử dụng thuộc tính `background-color` để tạo hình nền màu sắc.
- Hình nền hình ảnh: Sử dụng thuộc tính `background-image` để tạo hình nền hình ảnh.
- Hình nền lặp lại: Sử dụng thuộc tính `background-repeat` để tạo hình nền lặp lại.

Ví dụ:
```css
body {
  background-color: #f2f2f2; /* Tạo hình nền màu sắc */
}

div {
  background-image: url('hinhnen.jpg'); /* Tạo hình nền hình ảnh */
  background-repeat: no-repeat; /* Không lặp lại hình nền */
}
```

## Ví dụ
Giả sử chúng ta muốn tạo một trang web có hình nền màu xanh lá cây và hình nền hình ảnh ở giữa trang. Chúng ta có thể viết CSS như sau:
```css
body {
  background-color: #32CD32; /* Tạo hình nền màu xanh lá cây */
}

#hinhnen {
  background-image: url('hinhnen.jpg'); /* Tạo hình nền hình ảnh */
  background-repeat: no-repeat; /* Không lặp lại hình nền */
  background-position: center; /* Đặt hình nền ở giữa trang */
  height: 500px; /* Đặt chiều cao cho phần tử */
  width: 500px; /* Đặt chiều rộng cho phần tử */
}
```

## Bài tập
Bài tập này yêu cầu bạn tạo một trang web có hình nền màu sắc và hình nền hình ảnh. Hãy thực hiện các bước sau:
- Tạo một tệp tin HTML mới và thêm một phần tử `div` vào trang.
- Tạo một tệp tin CSS mới và thêm thuộc tính `background-color` để tạo hình nền màu sắc.
- Thêm thuộc tính `background-image` để tạo hình nền hình ảnh.
- Thêm thuộc tính `background-repeat` để tạo hình nền lặp lại hoặc không lặp lại.
- Thêm thuộc tính `background-position` để đặt hình nền ở vị trí mong muốn.
- Đặt chiều cao và chiều rộng cho phần tử `div` để hình nền hiển thị rõ ràng.
- Lưu và xem kết quả trong trình duyệt.
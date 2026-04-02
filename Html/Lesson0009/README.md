# Tạo Trang Giới Thiệu
## Giới thiệu
Trong bài học này, chúng ta sẽ tìm hiểu cách tạo một trang giới thiệu cơ bản bằng HTML và CSS. Trang giới thiệu là một phần quan trọng của bất kỳ trang web nào, vì nó cung cấp thông tin về người tạo, sản phẩm hoặc dịch vụ. Với kiến thức HTML và CSS, bạn có thể tạo ra một trang giới thiệu đẹp và chuyên nghiệp.

## Lý thuyết
Để tạo một trang giới thiệu, chúng ta cần sử dụng các thẻ HTML như `h1`, `p`, `img` để chứa tiêu đề, nội dung và hình ảnh. Ngoài ra, chúng ta cũng cần sử dụng CSS để định dạng và tạo phong cách cho trang web. Một số thuộc tính CSS quan trọng mà chúng ta sẽ sử dụng bao gồm `color`, `font-size`, `background-color`, `text-align`.

Ví dụ, để tạo một tiêu đề với màu xanh và kích thước 24px, chúng ta có thể sử dụng mã HTML và CSS sau:
```html
<h1 style="color: blue; font-size: 24px;">Trang Giới Thiệu</h1>
```
Hoặc chúng ta có thể định nghĩa một lớp CSS và áp dụng nó cho tiêu đề:
```css
.tieu-de {
  color: blue;
  font-size: 24px;
}
```
```html
<h1 class="tieu-de">Trang Giới Thiệu</h1>
```
## Ví dụ
Dưới đây là một ví dụ hoàn chỉnh về tạo trang giới thiệu bằng HTML và CSS:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Trang Giới Thiệu</title>
  <style>
    body {
      background-color: #f2f2f2;
    }
    .noi-dung {
      width: 80%;
      margin: 40px auto;
      text-align: center;
    }
    .tieu-de {
      color: blue;
      font-size: 24px;
    }
  </style>
</head>
<body>
  <div class="noi-dung">
    <h1 class="tieu-de">Trang Giới Thiệu</h1>
    <p>Xin chào! Tôi là Zunny, trợ giảng HTML/CSS.</p>
    <img src="anh.jpg" alt="Ảnh giới thiệu">
  </div>
</body>
</html>
```
## Bài tập
Bài tập của bạn là tạo một trang giới thiệu cho bản thân hoặc cho một sản phẩm/dịch vụ mà bạn yêu thích. Hãy sử dụng các thẻ HTML và thuộc tính CSS mà chúng ta đã học để tạo ra một trang web đẹp và chuyên nghiệp. Một số yêu cầu cụ thể bao gồm:
- Tạo một tiêu đề với màu sắc và kích thước phù hợp
- Thêm một đoạn văn bản giới thiệu về bản thân hoặc sản phẩm/dịch vụ
- Thêm một hình ảnh liên quan đến chủ đề
- Sử dụng CSS để định dạng và tạo phong cách cho trang web
Chúc bạn thành công!
# Tạo hiệu ứng Loading
## Giới thiệu
Trong thời đại công nghệ số hiện nay, việc tạo ra các trang web động và tương tác là điều không thể thiếu. Một trong những yếu tố quan trọng để tăng trải nghiệm người dùng là tạo hiệu ứng loading. Hiệu ứng loading giúp người dùng biết rằng trang web đang tải dữ liệu và chờ đợi, từ đó giảm cảm giác chờ đợi và tăng sự hài lòng. Trong bài học này, chúng ta sẽ tìm hiểu về cách tạo hiệu ứng loading bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng loading, chúng ta cần sử dụng các kỹ thuật sau:
- Sử dụng thẻ HTML để tạo ra cấu trúc cơ bản của hiệu ứng loading.
- Sử dụng CSS để tạo ra các hiệu ứng động và phong cách cho hiệu ứng loading.
- Sử dụng thuộc tính `animation` trong CSS để tạo ra hiệu ứng động.

Ví dụ về cấu trúc HTML cơ bản cho hiệu ứng loading:
```html
<div class="loading">
  <div class="loading-spinner"></div>
</div>
```
Ví dụ về CSS để tạo hiệu ứng động:
```css
.loading-spinner {
  border: 8px solid #f3f3f3;
  border-top: 8px solid #3498db;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```
## Ví dụ
Dưới đây là một ví dụ hoàn chỉnh về tạo hiệu ứng loading bằng HTML và CSS:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Tạo hiệu ứng Loading</title>
  <style>
    .loading {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
    .loading-spinner {
      border: 8px solid #f3f3f3;
      border-top: 8px solid #3498db;
      border-radius: 50%;
      width: 60px;
      height: 60px;
      animation: spin 2s linear infinite;
    }
    @keyframes spin {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }
  </style>
</head>
<body>
  <div class="loading">
    <div class="loading-spinner"></div>
  </div>
</body>
</html>
```
## Bài tập
Bài tập cho bạn:
- Tạo một hiệu ứng loading với hình dạng khác (ví dụ: hình vuông, hình tam giác,...).
- Thay đổi màu sắc và kích thước của hiệu ứng loading.
- Thêm hiệu ứng động cho hiệu ứng loading (ví dụ: hiệu ứng zoom, hiệu ứng translate,...).
- Tạo một trang web đơn giản và tích hợp hiệu ứng loading vào trang web đó.
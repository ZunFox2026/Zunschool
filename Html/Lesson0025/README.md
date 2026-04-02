# Tạo hiệu ứng loading
## Giới thiệu
Tạo hiệu ứng loading là một phần quan trọng trong thiết kế web, giúp người dùng biết rằng trang web đang tải nội dung. Hiệu ứng loading có thể là một hình ảnh quay, một thanh tiến trình, hoặc một thông báo văn bản. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng loading bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng loading, chúng ta cần sử dụng các thuộc tính CSS như `animation`, `keyframes`, và `transform`. Chúng ta cũng cần sử dụng HTML để tạo cấu trúc cho hiệu ứng loading. Có nhiều loại hiệu ứng loading khác nhau, nhưng trong bài này, chúng ta sẽ tập trung vào tạo hiệu ứng loading quay.

Ví dụ, chúng ta có thể tạo một hình tròn quay bằng cách sử dụng CSS như sau:
```html
<div class="loading"></div>
```

```css
.loading {
  width: 50px;
  height: 50px;
  border: 5px solid #ccc;
  border-top: 5px solid #666;
  border-radius: 50%;
  animation: quay 1s linear infinite;
}

@keyframes quay {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```
Đây là một ví dụ đơn giản về hiệu ứng loading quay. Chúng ta có thể tùy chỉnh màu sắc, kích thước, và tốc độ quay để phù hợp với thiết kế của trang web.

## Ví dụ
Dưới đây là một ví dụ khác về hiệu ứng loading, sử dụng thanh tiến trình:
```html
<div class="loading-bar">
  <div class="bar"></div>
</div>
```

```css
.loading-bar {
  width: 100px;
  height: 10px;
  background-color: #ccc;
  border-radius: 5px;
}

.bar {
  width: 0%;
  height: 10px;
  background-color: #666;
  animation: chay 2s linear infinite;
}

@keyframes chay {
  0% {
    width: 0%;
  }
  100% {
    width: 100%;
  }
}
```
Đây là một ví dụ về hiệu ứng loading sử dụng thanh tiến trình. Chúng ta có thể tùy chỉnh màu sắc, kích thước, và tốc độ để phù hợp với thiết kế của trang web.

## Bài tập
Bài tập cho bạn là tạo một hiệu ứng loading quay với các yêu cầu sau:
- Hình tròn quay có kích thước 100x100 pixel
- Bộ màu sử dụng là màu xanh lá cây và màu trắng
- Tốc độ quay là 2 giây
- Hiệu ứng loading quay vô hạn

Hãy sử dụng HTML và CSS để tạo hiệu ứng loading này. Bạn có thể tham khảo các ví dụ trên để thực hiện bài tập.
# Tạo hiệu ứng loading
## Giới thiệu
Trong bài này, chúng ta sẽ tìm hiểu về cách tạo hiệu ứng loading sử dụng HTML và CSS. Hiệu ứng loading là một phần quan trọng của trải nghiệm người dùng, giúp người dùng biết rằng trang web đang tải dữ liệu hoặc thực hiện một hành động nào đó. Chúng ta sẽ tìm hiểu về cách tạo hiệu ứng loading cơ bản và cách áp dụng nó vào trang web.

## Lý thuyết
Để tạo hiệu ứng loading, chúng ta có thể sử dụng các phương pháp sau:
- Sử dụng ảnh động (animation) để tạo hiệu ứng chuyển động.
- Sử dụng pseudo-element để tạo hình dạng và màu sắc cho hiệu ứng loading.
- Sử dụng CSS keyframe để định nghĩa các khung hình (frame) của hiệu ứng loading.

Dưới đây là một ví dụ cơ bản về cách tạo hiệu ứng loading sử dụng CSS:
```html
<div class="loading"></div>
```

```css
.loading {
  width: 50px;
  height: 50px;
  border: 5px solid #ccc;
  border-top: 5px solid #333;
  border-radius: 50%;
  animation: loading 1s linear infinite;
}

@keyframes loading {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```
Trong ví dụ trên, chúng ta tạo một div với lớp `loading` và định nghĩa các thuộc tính CSS để tạo hình dạng và màu sắc cho hiệu ứng loading. Chúng ta cũng sử dụng CSS keyframe để định nghĩa các khung hình của hiệu ứng loading.

## Ví dụ
Dưới đây là một ví dụ khác về cách tạo hiệu ứng loading sử dụng HTML và CSS:
```html
<div class="loading-text">Đang tải...</div>
<div class="loading-spinner"></div>
```

```css
.loading-text {
  font-size: 18px;
  color: #666;
}

.loading-spinner {
  width: 20px;
  height: 20px;
  border: 2px solid #ccc;
  border-top: 2px solid #333;
  border-radius: 50%;
  animation: loading-spinner 1s linear infinite;
}

@keyframes loading-spinner {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```
Trong ví dụ này, chúng ta tạo hai div, một div với lớp `loading-text` để hiển thị văn bản "Đang tải..." và một div với lớp `loading-spinner` để tạo hiệu ứng loading. Chúng ta sử dụng CSS keyframe để định nghĩa các khung hình của hiệu ứng loading.

## Bài tập
Bài tập cho bạn là tạo một hiệu ứng loading với hình dạng và màu sắc khác nhau. Bạn có thể sử dụng các phương pháp khác nhau để tạo hiệu ứng loading, chẳng hạn như sử dụng ảnh động, pseudo-element, hoặc CSS keyframe. Hãy thử nghiệm và tạo ra một hiệu ứng loading độc đáo và thú vị!
# Tạo hiệu ứng Loading
## Giới thiệu
Hiệu ứng loading là một phần quan trọng trong thiết kế web, giúp người dùng biết rằng trang web đang tải dữ liệu hoặc thực hiện một tác vụ nào đó. Trong bài này, chúng ta sẽ tìm hiểu về cách tạo hiệu ứng loading cơ bản sử dụng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng loading, chúng ta có thể sử dụng các kỹ thuật sau:
- Sử dụng animation trong CSS để tạo hiệu ứng chuyển động.
- Sử dụng pseudo-element như `:before` và `:after` để tạo hình dạng và hiệu ứng.
- Sử dụng thuộc tính `opacity` và `transform` để tạo hiệu ứng mờ và chuyển động.

Ví dụ, chúng ta có thể tạo một vòng tròn loading đơn giản bằng cách sử dụng HTML và CSS như sau:
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
Hiệu ứng này sẽ tạo một vòng tròn quay liên tục, cho người dùng biết rằng trang web đang tải dữ liệu.

## Ví dụ
Dưới đây là một ví dụ khác về tạo hiệu ứng loading sử dụng HTML và CSS:
```html
<div class="loading-container">
  <div class="loading-bar"></div>
</div>
```

```css
.loading-container {
  width: 100px;
  height: 100px;
  border: 1px solid #ccc;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.loading-bar {
  width: 50px;
  height: 50px;
  background-color: #333;
  animation: loading-bar 1s linear infinite;
}

@keyframes loading-bar {
  0% {
    transform: scale(0);
  }
  100% {
    transform: scale(1);
  }
}
```
Hiệu ứng này sẽ tạo một thanh loading tăng dần, cho người dùng biết rằng trang web đang tải dữ liệu.

## Bài tập
Bài tập của bạn là tạo một hiệu ứng loading sử dụng HTML và CSS. Hãy thử tạo một hiệu ứng loading hình dạng khác, như hình vuông hoặc hình tam giác. Ngoài ra, bạn cũng có thể thử thêm màu sắc và hiệu ứng chuyển động khác để làm cho hiệu ứng loading trở nên thú vị hơn.
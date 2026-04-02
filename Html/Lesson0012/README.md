# Tạo hiệu ứng Loading
## Giới thiệu
Hiệu ứng Loading là một phần quan trọng trong thiết kế web, giúp người dùng biết rằng trang web đang tải dữ liệu hoặc thực hiện một hành động nào đó. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng Loading cơ bản bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng Loading, chúng ta cần sử dụng các thuộc tính CSS như `animation`, `keyframes` và `transition`. Chúng ta cũng cần sử dụng HTML để tạo cấu trúc cho hiệu ứng Loading.

- `animation`: Thuộc tính này cho phép chúng ta tạo ra một hiệu ứng động trên trang web.
- `keyframes`: Thuộc tính này cho phép chúng ta định nghĩa các khung hình của hiệu ứng động.
- `transition`: Thuộc tính này cho phép chúng ta tạo ra một hiệu ứng chuyển tiếp giữa các trạng thái khác nhau.

Ví dụ, chúng ta có thể tạo một hiệu ứng Loading đơn giản bằng cách sử dụng CSS như sau:
```html
<div class="loading">
  <div class="loading-circle"></div>
</div>
```
```css
.loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.loading-circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 5px solid #ccc;
  border-top: 5px solid #333;
  animation: spin 1s linear infinite;
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
Chúng ta có thể tạo nhiều loại hiệu ứng Loading khác nhau bằng cách sử dụng các thuộc tính CSS khác nhau. Ví dụ, chúng ta có thể tạo một hiệu ứng Loading hình tròn với các vòng tròn đồng tâm:
```html
<div class="loading">
  <div class="loading-circle-1"></div>
  <div class="loading-circle-2"></div>
  <div class="loading-circle-3"></div>
</div>
```
```css
.loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.loading-circle-1 {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 5px solid #ccc;
  border-top: 5px solid #333;
  animation: spin 1s linear infinite;
}

.loading-circle-2 {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  border: 5px solid #ccc;
  border-top: 5px solid #333;
  animation: spin 1.5s linear infinite;
}

.loading-circle-3 {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: 5px solid #ccc;
  border-top: 5px solid #333;
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
## Bài tập
Bài tập cho bạn: Tạo một hiệu ứng Loading hình vuông với các cạnh đồng tâm. Sử dụng các thuộc tính CSS như `animation`, `keyframes` và `transition` để tạo ra hiệu ứng động. Bạn có thể tham khảo các ví dụ trên để thực hiện bài tập này.
# Tìm hiểu về Web Storage
## Giới thiệu
Web Storage là một tính năng của HTML5 cho phép lưu trữ dữ liệu trên trình duyệt của người dùng. Điều này giúp các trang web có thể lưu trữ dữ liệu cục bộ trên trình duyệt, từ đó cải thiện trải nghiệm người dùng và tăng tốc độ tải trang. Web Storage cung cấp hai loại lưu trữ: Local Storage và Session Storage. Trong bài này, chúng ta sẽ tìm hiểu về cả hai loại lưu trữ này và cách sử dụng chúng.

## Lý thuyết
Web Storage cung cấp hai loại lưu trữ:
- Local Storage: Lưu trữ dữ liệu vĩnh viễn trên trình duyệt cho đến khi người dùng xóa nó.
- Session Storage: Lưu trữ dữ liệu tạm thời trên trình duyệt và sẽ bị xóa khi người dùng đóng trình duyệt.
Cả hai loại lưu trữ đều sử dụng cặp khóa-giá trị (key-value) để lưu trữ dữ liệu. Chúng ta có thể sử dụng các phương thức như `setItem()`, `getItem()`, `removeItem()`, `clear()` để thao tác với dữ liệu trong Web Storage.
Ví dụ về CSS liên quan đến Web Storage là việc sử dụng thuộc tính `:hover` để tạo hiệu ứng khi người dùng di chuột qua một phần tử trên trang web. Ví dụ:
```css
.button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.button:hover {
  background-color: #3e8e41;
}
```
Tuy nhiên, trong bài này, chúng ta tập trung vào JavaScript và HTML.

## Ví dụ
Ví dụ sau đây minh họa cách sử dụng Local Storage và Session Storage:
```javascript
// Lưu trữ dữ liệu vào Local Storage
localStorage.setItem('ten', 'Zunny');

// Lấy dữ liệu từ Local Storage
let ten = localStorage.getItem('ten');
console.log(ten); // In ra "Zunny"

// Xóa dữ liệu từ Local Storage
localStorage.removeItem('ten');

// Lưu trữ dữ liệu vào Session Storage
sessionStorage.setItem('tuoi', '25');

// Lấy dữ liệu từ Session Storage
let tuoi = sessionStorage.getItem('tuoi');
console.log(tuoi); // In ra "25"
```
Trong ví dụ trên, chúng ta sử dụng `localStorage` và `sessionStorage` để lưu trữ và lấy dữ liệu.

## Bài tập
Bài tập này yêu cầu bạn tạo một trang web đơn giản có thể lưu trữ và hiển thị tên và tuổi của người dùng bằng cách sử dụng Local Storage và Session Storage. Yêu cầu:
- Tạo một trang web có hai ô nhập liệu (input) cho tên và tuổi.
- Tạo hai nút bấm (button) để lưu trữ dữ liệu vào Local Storage và Session Storage.
- Tạo hai nút bấm để lấy dữ liệu từ Local Storage và Session Storage và hiển thị trên trang web.
- Sử dụng CSS để tạo kiểu cho trang web, bao gồm cả việc sử dụng thuộc tính `:hover` để tạo hiệu ứng khi người dùng di chuột qua các nút bấm.
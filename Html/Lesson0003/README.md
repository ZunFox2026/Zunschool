# Tạo Form Đăng Ký
Đây là bài 3 trong khóa học Cơ bản về HTML/CSS, nơi bạn sẽ học cách tạo một form đăng ký cơ bản.

## Giới thiệu
Trong phần này, bạn sẽ học cách tạo một form đăng ký cơ bản bằng cách sử dụng HTML và CSS. Form đăng ký là một phần quan trọng của nhiều trang web, cho phép người dùng nhập thông tin của mình để đăng ký tài khoản hoặc nhận thông tin cập nhật. Bạn sẽ học cách tạo các trường nhập liệu, nút submit và cách sử dụng CSS để thiết kế form của mình.

Ví dụ về một form đăng ký cơ bản:
```html
<form>
  <label>Tên:</label>
  <input type="text" name="ten">
  <br>
  <label>Địa chỉ email:</label>
  <input type="email" name="email">
  <br>
  <label>Mật khẩu:</label>
  <input type="password" name="matkhau">
  <br>
  <input type="submit" value="Đăng ký">
</form>
```
Bạn có thể sử dụng CSS để thiết kế form của mình, chẳng hạn như thêm màu nền, font chữ và kích thước cho các trường nhập liệu.

## Lý thuyết
Để tạo một form đăng ký, bạn cần sử dụng các thẻ HTML sau:
- `<form>`: Thẻ này định nghĩa một form.
- `<label>`: Thẻ này định nghĩa một nhãn cho một trường nhập liệu.
- `<input>`: Thẻ này định nghĩa một trường nhập liệu.
- `<br>`: Thẻ này định nghĩa một dòng mới.

Bạn cũng cần sử dụng các thuộc tính sau:
- `type`: Thuộc tính này định nghĩa loại trường nhập liệu (ví dụ: text, email, password).
- `name`: Thuộc tính này định nghĩa tên của trường nhập liệu.

Ví dụ về cách sử dụng CSS để thiết kế form:
```css
form {
  background-color: #f2f2f2;
  padding: 20px;
  border: 1px solid #ccc;
}

label {
  display: block;
  margin-bottom: 10px;
}

input[type="text"], input[type="email"], input[type="password"] {
  width: 100%;
  height: 30px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
}

input[type="submit"] {
  width: 100%;
  height: 40px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
```
Đây chỉ là một ví dụ cơ bản, bạn có thể tùy chỉnh và thêm nhiều thuộc tính khác để thiết kế form của mình.

## Ví dụ
Dưới đây là một ví dụ hoàn chỉnh về một form đăng ký:
```html
<form>
  <label>Tên:</label>
  <input type="text" name="ten">
  <br>
  <label>Địa chỉ email:</label>
  <input type="email" name="email">
  <br>
  <label>Mật khẩu:</label>
  <input type="password" name="matkhau">
  <br>
  <input type="submit" value="Đăng ký">
</form>
```
Và CSS để thiết kế form:
```css
form {
  background-color: #f2f2f2;
  padding: 20px;
  border: 1px solid #ccc;
}

label {
  display: block;
  margin-bottom: 10px;
}

input[type="text"], input[type="email"], input[type="password"] {
  width: 100%;
  height: 30px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
}

input[type="submit"] {
  width: 100%;
  height: 40px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
```
Đây là một ví dụ cơ bản, bạn có thể thêm nhiều trường nhập liệu và thiết kế khác nhau để phù hợp với nhu cầu của mình.

## Bài tập
Bài tập của bạn là tạo một form đăng ký với các trường nhập liệu sau:
- Tên
- Địa chỉ email
- Mật khẩu
- Số điện thoại
- Địa chỉ

Bạn cần sử dụng HTML và CSS để tạo form và thiết kế nó. Bạn có thể thêm nhiều thuộc tính và thiết kế khác nhau để làm cho form của mình
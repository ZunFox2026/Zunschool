# Python 59: Xử Lý Chuỗi Cơ Bản

## Giới thiệu

Xử lý chuỗi là một kỹ năng cơ bản và quan trọng trong lập trình Python. Chuỗi (string) là kiểu dữ liệu dùng để lưu trữ văn bản, và Python cung cấp rất nhiều phương pháp tích hợp để thao tác với chuỗi như truy cập ký tự, nối chuỗi, tìm kiếm, thay thế, và định dạng. Trong bài học này, bạn sẽ làm quen với các thao tác xử lý chuỗi đơn giản nhưng hiệu quả, giúp bạn xử lý dữ liệu văn bản một cách dễ dàng.

## Lý thuyết

Trong Python, chuỗi được định nghĩa bằng cách đặt văn bản trong dấu nháy đơn (`'...'`) hoặc nháy kép (`"..."`). Một số thao tác cơ bản với chuỗi bao gồm:

- Truy cập ký tự: `chuoi[0]` lấy ký tự đầu tiên.
- Cắt chuỗi: `chuoi[1:4]` lấy từ ký tự thứ 1 đến thứ 3.
- Nối chuỗi: Dùng toán tử `+` để ghép hai chuỗi.
- Định dạng chuỗi: Dùng `f-string` hoặc phương thức `.format()`.
- Các phương thức phổ biến: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`.

## Ví dụ

```python
# Khai báo chuỗi
ten = "Alice"
ho = "Nguyen"

# Nối chuỗi
ho_ten = ho + " " + ten
print(ho_ten)  # Output: Nguyen Alice

# Chuyển thành chữ in hoa
print(ho_ten.upper())  # Output: NGUYEN ALICE

# Thay thế từ
cau = "Xin chào, tôi là Alice"
cau_moi = cau.replace("Alice", "Bob")
print(cau_moi)  # Output: Xin chào, tôi là Bob

# Cắt chuỗi
print(ten[0:2])  # Output: Al

# Định dạng chuỗi
tuoi = 20
thong_bao = f"Chào bạn {ten}, bạn {tuoi} tuổi."
print(thong_bao)  # Output: Chào bạn Alice, bạn 20 tuổi.
```

## Bài tập

1. Viết chương trình nhập vào họ tên người dùng, sau đó in ra tên và họ riêng biệt.
2. Nhập một chuỗi và in ra chuỗi đó viết hoa toàn bộ.
3. Thay thế tất cả ký tự khoảng trắng trong chuỗi thành dấu gạch dưới (`_`).
4. Tách một câu thành danh sách các từ bằng phương thức `.split()`.
5. Viết chương trình kiểm tra xem một từ có nằm trong câu hay không.

> Gợi ý: Sử dụng các phương thức chuỗi như `.split()`, `.replace()`, `.in`, và `f-string` để hoàn thành bài tập.
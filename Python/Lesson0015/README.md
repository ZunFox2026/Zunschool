# Bài học 15: Xử lý ngoại lệ (Exception Handling) trong Python

## Mục tiêu bài học
- Hiểu khái niệm ngoại lệ (exception) và tầm quan trọng của việc xử lý ngoại lệ trong lập trình.
- Biết cách sử dụng khối `try`, `except`, `else`, và `finally` để xử lý lỗi một cách an toàn.
- Áp dụng xử lý ngoại lệ trong các tình huống thực tế như đọc file, nhập liệu người dùng, và tính toán.
- Viết mã Python an toàn, tránh crash chương trình do lỗi không mong muốn.

## Lý thuyết chi tiết

Trong quá trình chạy chương trình, có thể xảy ra các lỗi như: chia cho 0, truy cập chỉ số vượt ngoài danh sách, mở file không tồn tại, v.v. Những lỗi này được gọi là **ngoại lệ (exceptions)**. Nếu không xử lý, chương trình sẽ dừng đột ngột.

Python cung cấp cơ chế `try-except` để bắt và xử lý ngoại lệ:

- `try`: Đặt các đoạn mã có thể gây lỗi vào đây.
- `except`: Xử lý lỗi nếu xảy ra.
- `else`: Thực thi nếu không có lỗi nào xảy ra trong `try`.
- `finally`: Luôn thực thi, dù có lỗi hay không.

### Cú pháp cơ bản:
```python
try:
    # Mã có thể gây lỗi
    pass
except LoaiException as e:
    # Xử lý lỗi
    print(e)
else:
    # Chạy nếu không có lỗi
    pass
finally:
    # Luôn chạy
    pass
```

### Một số loại ngoại lệ phổ biến:
- `ValueError`: Khi giá trị không hợp lệ (ví dụ: chuyển "abc" sang số).
- `TypeError`: Kiểu dữ liệu không phù hợp.
- `IndexError`: Truy cập chỉ số vượt ngoài danh sách.
- `FileNotFoundError`: File không tồn tại.
- `ZeroDivisionError`: Chia cho 0.

## Ví dụ minh họa

### Ví dụ 1: Xử lý lỗi nhập số
Chương trình yêu cầu người dùng nhập một số nguyên, xử lý trường hợp nhập sai.

### Ví dụ 2: Đọc file an toàn
Mở và đọc một file, xử lý trường hợp file không tồn tại.

### Ví dụ 3: Tính trung bình với kiểm tra rỗng và chia cho 0
Tính trung bình của danh sách số, xử lý danh sách rỗng.

## Bài tập thực hành
1. Viết hàm chia hai số, xử lý chia cho 0.
2. Viết chương trình đọc số từ file, xử lý file không tồn tại và lỗi dữ liệu.
3. Viết hàm tìm phần tử lớn nhất trong danh sách, xử lý danh sách rỗng.
4. Viết chương trình chuyển chuỗi thành số, xử lý lỗi định dạng.
5. Viết hàm mở file và in từng dòng, dùng `finally` để đóng file.

## Tổng kết
Xử lý ngoại lệ là kỹ năng quan trọng giúp chương trình hoạt động ổn định trong các tình huống bất ngờ. Sử dụng `try-except-else-finally` hợp lý giúp mã nguồn dễ đọc, an toàn và chuyên nghiệp hơn. Hãy luôn dự đoán các lỗi có thể xảy ra và xử lý chúng một cách thân thiện với người dùng.
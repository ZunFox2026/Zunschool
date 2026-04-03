# Bài học Python số 33: Xử lý ngoại lệ (Exception Handling)

## Mục tiêu bài học
- Hiểu được khái niệm ngoại lệ (exception) trong Python.
- Biết cách sử dụng khối `try`, `except`, `else`, và `finally` để xử lý lỗi.
- Áp dụng xử lý ngoại lệ trong các tình huống thực tế như nhập liệu người dùng, đọc file, tính toán số học.
- Viết code an toàn, tránh crash chương trình do lỗi không mong muốn.

## Lý thuyết chi tiết

Trong quá trình chạy chương trình, có thể xảy ra các lỗi không mong muốn như chia cho 0, truy cập chỉ số ngoài danh sách, đọc file không tồn tại... Những lỗi này được gọi là **ngoại lệ (exception)**. Nếu không được xử lý, chương trình sẽ dừng đột ngột.

Python cung cấp cơ chế **xử lý ngoại lệ** bằng các khối lệnh:

- `try`: Chứa đoạn code có thể gây lỗi.
- `except`: Xử lý lỗi khi xảy ra.
- `else`: Thực thi nếu không có lỗi.
- `finally`: Luôn thực thi, dù có lỗi hay không.

### Cú pháp cơ bản
```python
try:
    # Code có thể gây lỗi
    pass
except LoaiLoi:
    # Xử lý lỗi cụ thể
    pass
except:
    # Xử lý mọi lỗi còn lại
    pass
else:
    # Chạy nếu không có lỗi
    pass
finally:
    # Luôn chạy
    pass
```

### Ví dụ đơn giản
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Không thể chia cho 0!")
```

## Ví dụ minh họa

### Ví dụ 1: Xử lý nhập số từ người dùng
Chương trình yêu cầu người dùng nhập một số nguyên. Nếu nhập sai, chương trình sẽ yêu cầu nhập lại.

### Ví dụ 2: Đọc file an toàn
Chương trình đọc nội dung file, xử lý trường hợp file không tồn tại.

### Ví dụ 3: Tính trung bình danh sách số
Tính trung bình một danh sách, xử lý các trường hợp lỗi như danh sách rỗng hoặc có giá trị không phải số.

## Bài tập thực hành
1. Viết hàm `chia_hai_so(a, b)` thực hiện phép chia, xử lý lỗi chia cho 0.
2. Viết chương trình đọc file `data.txt` và in nội dung, xử lý lỗi nếu file không tồn tại.
3. Viết hàm `tinh_can_bac_hai(x)` tính căn bậc hai, xử lý lỗi khi x âm.
4. Viết chương trình nhập danh sách số từ người dùng, xử lý lỗi nhập không hợp lệ.
5. Viết hàm `doc_du_lieu_json(ten_file)` đọc file JSON, xử lý các lỗi có thể xảy ra.

## Tổng kết
Xử lý ngoại lệ là kỹ năng quan trọng giúp chương trình hoạt động ổn định và thân thiện với người dùng. Việc sử dụng `try-except` đúng cách giúp bạn bắt lỗi, thông báo rõ ràng và tiếp tục chương trình thay vì để nó sập. Luôn nhớ:
- Xử lý các lỗi cụ thể trước, rồi mới đến lỗi chung.
- Không nên bỏ trống khối `except`.
- Dùng `finally` để giải phóng tài nguyên (như đóng file).
- Ghi log lỗi để dễ dàng gỡ lỗi sau này.

Hãy luyện tập thường xuyên để viết code an toàn và chuyên nghiệp hơn!
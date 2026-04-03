# Bài học Python số 30 - Cấp độ Trung cấp

## Chủ đề: Xử lý ngoại lệ (Exception Handling) và tự định nghĩa Exception

Trong lập trình, không phải lúc nào mọi thứ cũng diễn ra như mong đợi. Các lỗi có thể xảy ra do đầu vào không hợp lệ, tài nguyên không tồn tại, kết nối mạng thất bại,... Python cung cấp cơ chế xử lý ngoại lệ (Exception Handling) để chương trình có thể xử lý lỗi một cách mềm dẻo thay vì dừng đột ngột.

Bài học này sẽ giúp bạn:
- Hiểu cách bắt và xử lý lỗi trong Python.
- Biết cách tự định nghĩa các loại ngoại lệ riêng.
- Ứng dụng vào các tình huống thực tế như đọc file, xử lý đầu vào người dùng, v.v.

---

## Mục tiêu bài học

Sau bài học này, học viên sẽ:
1. Hiểu được khái niệm và vai trò của ngoại lệ (exception) trong Python.
2. Biết sử dụng khối `try`, `except`, `else`, và `finally`.
3. Có thể tự định nghĩa lớp ngoại lệ riêng phù hợp với ngữ cảnh chương trình.
4. Áp dụng xử lý ngoại lệ vào các tình huống thực tế.

---

## Lý thuyết chi tiết

### 1. Ngoại lệ là gì?

Ngoại lệ (exception) là các sự kiện bất thường xảy ra trong quá trình thực thi chương trình, làm gián đoạn dòng chảy bình thường của mã lệnh. Ví dụ: chia cho 0, truy cập chỉ số ngoài danh sách, mở file không tồn tại,...

### 2. Cú pháp xử lý ngoại lệ

```python
try:
    # Đoạn mã có thể gây lỗi
    pass
except LoaiException as e:
    # Xử lý lỗi
    pass
else:
    # Chạy nếu không có lỗi
    pass
finally:
    # Luôn chạy, dù có lỗi hay không
    pass
```

### 3. Một số ngoại lệ phổ biến

- `ValueError`: giá trị không hợp lệ (ví dụ: `int('abc')`)
- `TypeError`: kiểu dữ liệu không phù hợp
- `FileNotFoundError`: không tìm thấy file
- `IndexError`: truy cập chỉ số ngoài danh sách
- `KeyError`: truy cập key không tồn tại trong từ điển

### 4. Tự định nghĩa ngoại lệ

Bạn có thể tạo lớp ngoại lệ riêng bằng cách kế thừa từ `Exception`:

```python
class MyError(Exception):
    pass
```

---

## Ví dụ minh họa

### Ví dụ 1: Xử lý lỗi nhập số

Chương trình yêu cầu người dùng nhập một số nguyên. Nếu nhập sai, chương trình sẽ yêu cầu nhập lại.

### Ví dụ 2: Đọc file an toàn

Mở và đọc nội dung file, xử lý trường hợp file không tồn tại.

### Ví dụ 3: Tự định nghĩa ngoại lệ cho hệ thống ngân hàng

Tạo ngoại lệ riêng cho giao dịch rút tiền khi số dư không đủ.

---

## Bài tập thực hành

1. Viết hàm chia hai số, xử lý trường hợp chia cho 0.
2. Viết chương trình đọc file và đếm số dòng, xử lý các lỗi có thể xảy ra.
3. Tạo lớp `NegativeAgeError` và kiểm tra tuổi nhập vào.
4. Xử lý lỗi khi chuyển đổi chuỗi thành danh sách số.
5. Viết hàm tìm giá trị lớn nhất trong danh sách, xử lý khi danh sách rỗng.

---

## Tổng kết

Xử lý ngoại lệ là kỹ năng quan trọng giúp chương trình ổn định và thân thiện hơn. Việc sử dụng `try-except` hợp lý giúp phát hiện và xử lý lỗi một cách mềm dẻo. Ngoài ra, việc tự định nghĩa ngoại lệ giúp mã nguồn rõ ràng, dễ bảo trì và phản ánh đúng ngữ cảnh nghiệp vụ.

Bạn nên luôn:
- Xử lý các ngoại lệ cụ thể thay vì dùng `except` chung chung.
- Không bỏ trống khối `except`.
- Sử dụng `finally` để dọn dẹp tài nguyên (đóng file, kết nối, v.v.).
- Tự định nghĩa exception khi cần mô tả lỗi nghiệp vụ.

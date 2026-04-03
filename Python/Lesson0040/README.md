# Bài học Python số 40 - Xử lý ngoại lệ nâng cao và tự tạo ngoại lệ (Cấp độ trung cấp)

Trong bài học này, chúng ta sẽ đi sâu hơn vào chủ đề **xử lý ngoại lệ** trong Python — một kỹ năng rất quan trọng khi viết các chương trình thực tế. Bạn đã biết cách dùng `try-except` cơ bản, nhưng để viết mã an toàn, chuyên nghiệp và dễ bảo trì, bạn cần hiểu cách xử lý ngoại lệ một cách có hệ thống, bao gồm việc **tạo ra các ngoại lệ tùy chỉnh**.

## Mục tiêu bài học
- Hiểu rõ cách xử lý ngoại lệ một cách hiệu quả và an toàn.
- Biết cách bắt nhiều loại ngoại lệ và xử lý riêng biệt.
- Học cách tạo và sử dụng **ngoại lệ tùy chỉnh** (custom exceptions) để phản ánh các lỗi đặc thù trong ứng dụng.
- Áp dụng kiến thức vào các tình huống thực tế như kiểm tra dữ liệu đầu vào, xử lý lỗi trong hàm.

## Lý thuyết chi tiết

### 1. Xử lý nhiều ngoại lệ
Trong thực tế, một khối `try` có thể sinh ra nhiều loại ngoại lệ khác nhau. Python cho phép bạn bắt từng loại riêng biệt để xử lý phù hợp.

```python
try:
    x = int(input("Nhập một số: "))
    result = 10 / x
except ValueError:
    print("Lỗi: Bạn phải nhập một số nguyên!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except Exception as e:
    print(f"Lỗi không xác định: {e}")
```

### 2. Khối `else` và `finally`
- `else`: chạy khi **không có ngoại lệ** xảy ra.
- `finally`: luôn chạy, dù có ngoại lệ hay không. Thường dùng để dọn dẹp tài nguyên (đóng file, kết nối DB...).

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Không tìm thấy file!")
else:
    print("Đọc file thành công:", content)
finally:
    print("Đóng chương trình...")
```

### 3. Tạo ngoại lệ tùy chỉnh
Bạn có thể tạo lớp ngoại lệ riêng bằng cách kế thừa từ `Exception` hoặc các lớp ngoại lệ có sẵn.

```python
class SoAmError(Exception):
    """Ngoại lệ khi người dùng nhập số âm"""
    pass

# Sử dụng
if x < 0:
    raise SoAmError("Số không được âm!")
```

Việc tạo ngoại lệ tùy chỉnh giúp mã nguồn rõ ràng, dễ bảo trì và có thể mở rộng.

## Ví dụ minh họa
Xem file `main.py` để chạy các ví dụ đầy đủ.

## Bài tập thực hành
Xem file `exercises.py` để làm bài tập. Sau đó tham khảo `solutions.py` nếu cần.

## Tổng kết
- Xử lý ngoại lệ là kỹ năng bắt buộc với lập trình viên Python.
- Sử dụng `try-except-else-finally` để kiểm soát luồng chương trình khi có lỗi.
- Tạo ngoại lệ tùy chỉnh giúp xử lý lỗi theo ngữ cảnh, làm cho mã rõ ràng và chuyên nghiệp hơn.
- Luôn ghi log hoặc thông báo lỗi hợp lý để dễ dàng gỡ lỗi sau này.

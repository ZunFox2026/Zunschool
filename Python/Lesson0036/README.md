# Bài học Python số 36 - Cấp độ Trung cấp

## Chủ đề: Xử lý ngoại lệ nâng cao và việc sử dụng `finally`, `else`, và `raise`

Trong bài học này, chúng ta sẽ đi sâu vào kỹ thuật xử lý ngoại lệ trong Python, bao gồm việc sử dụng các khối `try`, `except`, `else`, `finally`, và cách tự phát sinh ngoại lệ bằng `raise`. Đây là những kiến thức quan trọng giúp chương trình của bạn trở nên chuyên nghiệp, an toàn và dễ bảo trì hơn.

### 1. Mục tiêu bài học
- Hiểu rõ cách hoạt động của các khối `try`, `except`, `else`, và `finally`.
- Biết cách sử dụng `raise` để chủ động phát sinh ngoại lệ.
- Áp dụng xử lý ngoại lệ hiệu quả trong các tình huống thực tế như đọc file, nhập liệu người dùng, và kiểm tra dữ liệu.
- Viết code an toàn, dễ gỡ lỗi và bảo trì.

### 2. Lý thuyết chi tiết

#### a. Cấu trúc đầy đủ của khối try-except

Cấu trúc đầy đủ khi xử lý ngoại lệ gồm 4 khối:

```python
try:
    # Code có thể gây lỗi
    pass
except LoaiLoi:
    # Xử lý lỗi cụ thể
    pass
else:
    # Chạy nếu KHÔNG có lỗi xảy ra
    pass
finally:
    # Luôn chạy, dù có lỗi hay không
    pass
```

- `try`: Chứa đoạn code có thể gây lỗi.
- `except`: Xử lý lỗi nếu xảy ra.
- `else`: Thực thi khi **không có lỗi nào** xảy ra trong khối `try`.
- `finally`: Luôn luôn thực thi, thường dùng để dọn dẹp tài nguyên (đóng file, kết nối DB...).

#### b. Sử dụng `raise` để phát sinh ngoại lệ

Bạn có thể chủ động phát sinh lỗi bằng từ khóa `raise`:

```python
if dieu_kien:
    raise ValueError("Lỗi do người dùng cung cấp dữ liệu không hợp lệ")
```

Điều này rất hữu ích khi kiểm tra đầu vào, bảo vệ hàm khỏi dữ liệu sai.

### 3. Ví dụ minh họa

Xem các ví dụ trong file `main.py` để hiểu cách áp dụng thực tế.

### 4. Bài tập thực hành

Xem file `exercises.py` để làm bài tập. Sau đó đối chiếu với `solutions.py`.

### 5. Tổng kết

Xử lý ngoại lệ là kỹ năng thiết yếu khi lập trình Python. Việc sử dụng `else` và `finally` giúp code rõ ràng và an toàn hơn. Hãy luôn kiểm tra dữ liệu đầu vào và sử dụng `raise` khi cần để thông báo lỗi rõ ràng. Điều này giúp chương trình của bạn dễ kiểm soát và dễ bảo trì trong tương lai.

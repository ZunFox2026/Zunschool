# Bài học Python nâng cao số 64: Làm việc với Context Managers và Protocol `__enter__`, `__exit__`

## Mục tiêu bài học
- Hiểu được khái niệm và vai trò của context managers trong Python.
- Biết cách tạo và sử dụng context managers bằng cách triển khai `__enter__` và `__exit__`.
- Ứng dụng context managers để quản lý tài nguyên một cách an toàn và sạch sẽ (ví dụ: file, kết nối cơ sở dữ liệu, khóa đồng bộ).
- Sử dụng `contextlib` để tạo context managers đơn giản hơn.

## Lý thuyết chi tiết

### 1. Context Manager là gì?
Context manager là một đối tượng trong Python cho phép bạn quản lý tài nguyên một cách có cấu trúc thông qua câu lệnh `with`. Mục đích chính là đảm bảo rằng tài nguyên được khởi tạo và giải phóng đúng cách, ngay cả khi xảy ra lỗi.

Một context manager phải triển khai hai phương thức đặc biệt:
- `__enter__(self)`: được gọi khi bắt đầu khối `with`, thường trả về tài nguyên cần sử dụng.
- `__exit__(self, exc_type, exc_value, traceback)`: được gọi khi kết thúc khối `with`, dù có lỗi hay không. Phương thức này nên dọn dẹp tài nguyên và có thể xử lý ngoại lệ nếu cần.

### 2. Cú pháp `with`
```python
with context_manager as resource:
    # Sử dụng resource ở đây
# Tự động gọi __exit__, giải phóng tài nguyên
```

### 3. Ví dụ cơ bản: Mở file
Khi mở file, chúng ta nên đóng nó sau khi dùng xong. `open()` là một context manager tiêu biểu:

```python
with open('file.txt', 'w') as f:
    f.write('Hello')
# File tự động đóng dù có lỗi hay không
```

### 4. Tạo context manager tùy chỉnh
Bạn có thể tự tạo lớp có `__enter__` và `__exit__` để quản lý bất kỳ tài nguyên nào.

## Ví dụ minh họa

### Ví dụ 1: Context manager đo thời gian thực thi
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        print(f'Thời gian thực thi: {self.end - self.start:.4f} giây')

with Timer():
    time.sleep(1)
# In ra: Thời gian thực thi: 1.00 giây
```

### Ví dụ 2: Quản lý kết nối cơ sở dữ liệu giả lập
```python
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
        if exc_type is not None:
            print(f'Lỗi xảy ra: {exc_value}')
        return False  # Không chặn ngoại lệ

# Sử dụng
with DatabaseConnection(':memory:') as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users (id INTEGER, name TEXT)')
    cursor.execute('INSERT INTO users (id, name) VALUES (1, "Alice")')
    conn.commit()
```

### Ví dụ 3: Quản lý khóa (lock) trong lập trình đồng thời
```python
import threading

class ManagedLock:
    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        print('Đang chờ khóa...')
        self.lock.acquire()
        print('Đã có khóa')
        return self.lock

    def __exit__(self, *args):
        print('Đang giải phóng khóa')
        self.lock.release()

# Sử dụng trong môi trường đa luồng
lock = ManagedLock()
with lock:
    print('Đang xử lý trong khu vực an toàn...')
# Khóa tự động được giải phóng
```

## Bài tập thực hành

1. **Tạo context manager đếm số dòng trong file**
   Viết một context manager `LineCounter` nhận đường dẫn file, mở file, và đếm số dòng. Trả về số dòng khi kết thúc. Đảm bảo file được đóng đúng cách.

2. **Context manager tạm thời đổi thư mục làm việc**
   Tạo `TemporaryDirectory` để thay đổi thư mục làm việc hiện tại vào một thư mục mới, và tự động quay lại thư mục cũ khi thoát, dù có lỗi hay không. Dùng `os.getcwd()` và `os.chdir()`.

3. **Context manager ghi log hành động**
   Viết `ActionLogger` ghi lại thời gian bắt đầu, kết thúc và các thông điệp vào file log. Nếu có ngoại lệ, ghi cả lỗi vào log.

4. **Sử dụng `contextlib.contextmanager` để tạo generator-based context manager**
   Dùng decorator `@contextmanager` từ `contextlib` để viết lại `Timer` ở trên dưới dạng hàm.

5. **Context manager quản lý trạng thái (ví dụ: tạm thời tắt ghi log)**
   Tạo `SilentMode` để tạm thời đặt một biến toàn cục `LOGGING_ENABLED = False`, và khôi phục giá trị ban đầu khi thoát.

## Gợi ý
- Sử dụng `try...finally` bên trong `__exit__` nếu cần xử lý lỗi.
- Trả về `True` trong `__exit__` nếu bạn muốn **ngăn chặn** ngoại lệ lan ra ngoài.
- Dùng `contextlib` để đơn giản hóa việc tạo context manager.

## Tổng kết
Context managers là một công cụ mạnh mẽ để quản lý tài nguyên và đảm bảo tính toàn vẹn trong Python. Bằng cách sử dụng `with`, bạn có thể viết code an toàn, dễ đọc và dễ bảo trì. Việc tự tạo context manager giúp bạn mở rộng khả năng kiểm soát vòng đời của tài nguyên trong ứng dụng, đặc biệt trong các hệ thống lớn, đa luồng hoặc cần xử lý lỗi tinh vi.

Hãy luyện tập thường xuyên để thành thạo kỹ thuật này — nó là nền tảng cho nhiều thư viện và framework Python hiện đại.

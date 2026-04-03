# Bài học Python nâng cao số 69: Làm việc với Context Managers và Protocol `__enter__`, `__exit__`

## Mục tiêu bài học
- Hiểu được khái niệm và vai trò của **Context Manager** trong Python.
- Biết cách sử dụng `with` để quản lý tài nguyên một cách an toàn.
- Triển khai Context Manager bằng cách ghi đè `__enter__` và `__exit__`.
- Sử dụng module `contextlib` để tạo Context Manager linh hoạt.
- Áp dụng Context Manager vào các tình huống thực tế như xử lý file, kết nối cơ sở dữ liệu, đo thời gian thực thi, v.v.

## Lý thuyết chi tiết

### 1. Context Manager là gì?

Context Manager là một đối tượng trong Python cho phép bạn quản lý tài nguyên một cách an toàn thông qua câu lệnh `with`. Khi sử dụng `with`, Python đảm bảo rằng tài nguyên sẽ được khởi tạo (`__enter__`) và giải phóng đúng cách (`__exit__`) ngay cả khi có lỗi xảy ra.

Cú pháp cơ bản:
```python
with context_manager as variable:
    # Làm việc với tài nguyên
```

### 2. Giao thức Context Manager

Một đối tượng trở thành Context Manager nếu nó triển khai hai phương thức đặc biệt:
- `__enter__(self)`: Được gọi khi bắt đầu khối `with`. Trả về giá trị gán cho biến sau `as`.
- `__exit__(self, exc_type, exc_value, traceback)`: Được gọi khi thoát khỏi khối `with`. Dùng để dọn dẹp tài nguyên. Nếu trả về `True`, lỗi sẽ bị ngắt; nếu `False` hoặc `None`, lỗi được ném lại.

### 3. Ví dụ đơn giản

```python
class MyContext:
    def __enter__(self):
        print("Bắt đầu context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Kết thúc context")
        if exc_type is not None:
            print(f"Lỗi: {exc_value}")
        return False
```

### 4. Sử dụng contextlib

Module `contextlib` cung cấp decorator `@contextmanager` để tạo Context Manager từ hàm sinh (generator), giúp viết ngắn gọn hơn.

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Bắt đầu")
    try:
        yield "data"
    finally:
        print("Kết thúc")
```

## Ví dụ minh họa

1. **Tự tạo Context Manager để đo thời gian thực thi**.
2. **Quản lý kết nối cơ sở dữ liệu giả lập**.
3. **Tạo Context Manager để tạm thời thay đổi thư mục làm việc**.

## Bài tập thực hành

1. Viết Context Manager để đếm thời gian thực thi của một đoạn code.
2. Tạo Context Manager quản lý tệp tạm thời.
3. Viết Context Manager để bắt và ghi log lỗi vào file.
4. Tạo Context Manager để tạm thời thay đổi biến môi trường.
5. Viết Context Manager in ra thông báo bắt đầu và kết thúc, đồng thời đếm số lần nó được gọi.

## Tổng kết

Context Manager là công cụ mạnh mẽ giúp quản lý tài nguyên một cách sạch sẽ và an toàn trong Python. Việc sử dụng `with` không chỉ làm code rõ ràng hơn mà còn tránh được các lỗi rò rỉ tài nguyên. Ở cấp độ nâng cao, bạn nên biết cách tự tạo Context Manager theo nhu cầu và tận dụng `contextlib` để viết code linh hoạt và tái sử dụng tốt hơn.
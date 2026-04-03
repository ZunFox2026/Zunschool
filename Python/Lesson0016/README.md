# Bài học Python số 16: Làm việc với Decorators (Hàm trang trí)

## Mục tiêu bài học
- Hiểu khái niệm và vai trò của **decorator** trong Python.
- Biết cách viết và sử dụng decorator đơn giản và có tham số.
- Áp dụng decorator vào các tình huống thực tế như: đo thời gian thực thi, kiểm tra quyền truy cập, ghi log.
- Nâng cao khả năng tái sử dụng và tổ chức mã nguồn.

## Lý thuyết chi tiết

### 1. Decorator là gì?
Decorator là một hàm nhận vào một hàm khác và mở rộng hành vi của hàm đó mà **không thay đổi nội dung hàm gốc**. Đây là một khái niệm quan trọng trong lập trình hàm (functional programming) và rất phổ biến trong Python.

### 2. Cú pháp cơ bản
Sử dụng ký hiệu `@` để áp dụng decorator:

```python
def decorator(func):
    def wrapper():
        print("Trước khi hàm được gọi")
        func()
        print("Sau khi hàm được gọi")
    return wrapper

@decorator
def hello():
    print("Xin chào!")
```

Khi gọi `hello()`, thực tế là `wrapper()` được thực thi.

### 3. Decorator với tham số
Đôi khi ta cần truyền tham số cho decorator. Khi đó cần thêm một lớp hàm bao ngoài:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
```

### 4. Sử dụng `*args` và `**kwargs`
Để decorator hoạt động với mọi hàm, ta dùng `*args` và `**kwargs` để nhận tất cả tham số.

### 5. Một số decorator phổ biến
- `@staticmethod`, `@classmethod` trong class
- `@property` để tạo thuộc tính tính toán
- Trong framework như Flask: `@app.route('/')`

## Ví dụ minh họa

### Ví dụ 1: Đo thời gian thực thi
Tạo decorator để đo thời gian thực hiện một hàm.

### Ví dụ 2: Kiểm tra quyền truy cập
Giả lập kiểm tra quyền trước khi thực hiện hàm.

### Ví dụ 3: Ghi log hoạt động
Tự động ghi log mỗi khi một hàm được gọi.

## Bài tập thực hành
1. Viết decorator `@log_calls` để in ra tên hàm và tham số khi gọi.
2. Viết decorator `@retry` để thử lại hàm nếu gặp lỗi, tối đa 3 lần.
3. Viết decorator `@memoize` để lưu kết quả hàm (caching), tránh tính toán lại.
4. Viết decorator `@timing` cho hàm có tham số.
5. Viết decorator `@ensure_positive` kiểm tra tất cả tham số là số dương.

## Tổng kết
- Decorator giúp tách biệt logic chính và logic phụ (cross-cutting concerns).
- Dễ tái sử dụng, giúp mã nguồn sạch hơn và dễ bảo trì.
- Nắm vững decorator là bước tiến quan trọng khi học Python ở cấp độ trung cấp trở lên.
- Cần lưu ý: luôn dùng `@functools.wraps` để bảo toàn thông tin hàm gốc (sẽ học ở bài nâng cao).

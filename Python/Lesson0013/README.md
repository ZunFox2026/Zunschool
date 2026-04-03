# Bài học Python Trung cấp - Bài 13: Làm việc với Decorators

## Mục tiêu bài học
- Hiểu được khái niệm và vai trò của **decorator** trong Python.
- Biết cách tạo và sử dụng decorator đơn giản và nâng cao.
- Áp dụng decorator để thêm chức năng cho hàm như: ghi log, đo thời gian thực thi, kiểm tra đầu vào.
- Nắm vững cơ chế hoạt động của `@decorator` và cách truyền tham số vào decorator.

## Lý thuyết chi tiết

### 1. Decorator là gì?
Decorator là một hàm nhận vào một hàm khác, thêm hành vi cho hàm đó và trả về một hàm mới. Đây là một kỹ thuật mạnh mẽ để **tái sử dụng mã nguồn** và **mở rộng chức năng** mà không cần thay đổi nội dung hàm gốc.

Trong Python, hàm là **đối tượng bậc nhất** (first-class object), có nghĩa là chúng có thể được gán vào biến, truyền vào hàm khác, hoặc trả về từ một hàm — điều này tạo nền tảng cho decorator.

### 2. Cú pháp cơ bản
Sử dụng ký hiệu `@` để áp dụng decorator:

```python
@decorator_function
def my_function():
    pass
```

Tương đương với:

```python
my_function = decorator_function(my_function)
```

### 3. Cấu trúc một decorator đơn giản

```python
def my_decorator(func):
    def wrapper():
        print("Trước khi gọi hàm")
        func()
        print("Sau khi gọi hàm")
    return wrapper
```

### 4. Decorator với tham số
Để tạo decorator nhận tham số, cần thêm một lớp hàm bao ngoài:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
```

## Ví dụ minh họa

### Ví dụ 1: Decorator ghi log thời gian thực thi
Tự động ghi lại thời gian bắt đầu và kết thúc khi một hàm được gọi.

### Ví dụ 2: Decorator kiểm tra kiểu dữ liệu đầu vào
Kiểm tra xem các tham số đầu vào có đúng kiểu mong muốn không.

### Ví dụ 3: Decorator đếm số lần gọi hàm
Theo dõi và in ra số lần một hàm đã được gọi.

## Bài tập thực hành
1. Viết một decorator `@time_logger` để in thời gian thực thi của hàm.
2. Viết decorator `@ensure_positive` kiểm tra tất cả tham số số là số dương.
3. Viết decorator `@memoize` để lưu kết quả hàm, tránh tính toán lại.
4. Viết decorator `@admin_required` mô phỏng kiểm tra quyền truy cập.
5. Viết decorator `@retry` tự động thử lại hàm nếu phát sinh lỗi.

## Tổng kết
Decorator là một công cụ mạnh mẽ trong Python giúp tách biệt logic chức năng chính và các hành vi phụ như logging, bảo mật, cache, v.v. Việc sử dụng decorator giúp code **sạch hơn**, **dễ bảo trì hơn** và **tái sử dụng tốt hơn**. Học viên nên luyện tập thường xuyên để thành thạo kỹ thuật này.
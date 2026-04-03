# Bài học Python nâng cao số 92: Sử dụng Decorator với Tham số và Class-based Decorators

## Mục tiêu bài học
- Hiểu được cách tạo và sử dụng **decorator có tham số** trong Python.
- Nắm vững khái niệm **class-based decorator** và cách triển khai chúng.
- Áp dụng decorator nâng cao vào các tình huống thực tế như: ghi log có mức độ, giới hạn tốc độ gọi hàm (rate limiting), đếm số lần gọi.
- Phát triển tư duy lập trình hàm nâng cao và viết code sạch, tái sử dụng tốt.

## Lý thuyết chi tiết

### 1. Decorator với tham số

Thông thường, decorator là một hàm nhận vào một hàm khác và trả về một hàm được bọc (wrapped). Tuy nhiên, đôi khi ta muốn truyền thêm tham số vào decorator để tùy chỉnh hành vi.

Cấu trúc của một decorator có tham số:
```python
@decorator(tham_so)
def func():
    ...
```

Để làm được điều này, ta cần **ba lớp hàm lồng nhau**:
- Hàm ngoài cùng: nhận tham số cho decorator.
- Hàm giữa: nhận hàm cần bọc.
- Hàm trong cùng: thực hiện hành vi và gọi hàm gốc.

**Ví dụ**: Tạo decorator in ra thông báo trước khi gọi hàm, với thông báo tùy chỉnh.

```python
def log_with_message(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[LOG] {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### 2. Class-based Decorators

Decorator không nhất thiết phải là hàm. Ta có thể dùng **class** làm decorator bằng cách định nghĩa phương thức `__call__`.

Class-based decorator hữu ích khi cần giữ trạng thái (state), ví dụ như đếm số lần gọi, lưu cache, hoặc thiết lập cấu hình.

**Yêu cầu cơ bản**:
- Class phải có phương thức `__init__` nhận hàm cần bọc.
- Class phải có phương thức `__call__` để thực thi khi hàm được gọi.

**Ví dụ**: Đếm số lần gọi hàm.

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Hàm '{self.func.__name__}' đã được gọi {self.count} lần")
        return self.func(*args, **kwargs)
```

## Ví dụ minh họa

### Ví dụ 1: Ghi log với mức độ tùy chọn

Tạo decorator cho phép ghi log theo mức (INFO, WARNING, ERROR).

### Ví dụ 2: Giới hạn tần suất gọi hàm (Rate Limiting)

Tránh một hàm được gọi quá nhanh, hữu ích trong API hoặc xử lý tài nguyên.

### Ví dụ 3: Class decorator đếm số lần gọi và ghi log

Kết hợp đếm và ghi log bằng class-based decorator.

## Bài tập thực hành

1. Viết decorator `@repeat(n)` để gọi một hàm lặp lại `n` lần.
2. Viết class decorator `@TimeIt` để in ra thời gian thực thi mỗi lần gọi hàm.
3. Viết decorator `@only_allow_types` nhận các kiểu dữ liệu hợp lệ và kiểm tra đối số đầu vào.
4. Viết decorator `@cache_method` (cho phương thức lớp) để lưu kết quả dựa trên tham số.
5. Viết decorator `@ensure_result` kiểm tra kết quả trả về có thỏa điều kiện không.

## Tổng kết

- Decorator có tham số giúp linh hoạt hóa hành vi của decorator.
- Class-based decorator cho phép lưu trạng thái và tái sử dụng tốt trong nhiều tình huống.
- Kết hợp decorator với `*args`, `**kwargs` giúp xử lý mọi loại hàm.
- Decorator nâng cao giúp viết code sạch, tách biệt logic (cross-cutting concerns) như logging, caching, validation.

Học viên nên luyện tập thường xuyên để làm chủ kỹ thuật này — một công cụ mạnh mẽ trong lập trình Python chuyên nghiệp.

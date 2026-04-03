# Bài học 17: Làm việc với Decorators trong Python (Cấp độ Trung cấp)

Chào mừng bạn đến với bài học số 17 trong khóa học Python cấp độ trung cấp! Trong bài học này, chúng ta sẽ tìm hiểu về **decorators** — một trong những tính năng mạnh mẽ và linh hoạt nhất của Python, cho phép bạn **mở rộng chức năng của hàm hoặc lớp mà không cần thay đổi nội dung bên trong chúng**.

Decorators được sử dụng rộng rãi trong các ứng dụng thực tế như xác thực, ghi log, đo hiệu suất, kiểm tra quyền truy cập, và nhiều hơn nữa. Hiểu rõ decorators sẽ giúp bạn viết mã sạch hơn, tái sử dụng tốt hơn và chuyên nghiệp hơn.

---

## Mục tiêu bài học

Sau bài học này, bạn sẽ có thể:
- Hiểu được khái niệm và cơ chế hoạt động của decorator trong Python.
- Tạo và sử dụng các decorator đơn giản và nâng cao.
- Áp dụng decorator vào các tình huống thực tế như ghi log, đo thời gian thực thi, và xác thực.
- Viết decorator có tham số.

---

## Lý thuyết chi tiết

### 1. Hàm là đối tượng đầu cấp (First-class objects)

Trong Python, **hàm là đối tượng đầu cấp**, có nghĩa là bạn có thể:
- Gán hàm cho biến.
- Truyền hàm vào hàm khác.
- Trả về hàm từ một hàm.

```python
# Ví dụ
def chao():
    return "Xin chào!"

c = chao
print(c())  # In ra: Xin chào!
```

### 2. Hàm lồng nhau (Nested functions)

Bạn có thể định nghĩa một hàm bên trong một hàm khác.

```python
def ngoai():
    def trong():
        return "Tôi ở trong!"
    return trong()
```

### 3. Closure

Một closure là một hàm ghi nhớ giá trị từ phạm vi bao quanh nó, ngay cả khi phạm vi đó đã kết thúc.

```python
def tao_ham(x):
    def nhan(x2):
        return x * x2
    return nhan

double = tao_ham(2)
print(double(5))  # In ra: 10
```

### 4. Decorator là gì?

Một **decorator** là một hàm nhận vào một hàm khác và **trả về một hàm mới** với hành vi được mở rộng.

Cú pháp sử dụng: `@tên_decorator`

#### Cấu trúc cơ bản:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Làm gì đó trước khi gọi hàm
        result = func(*args, **kwargs)
        # Làm gì đó sau khi gọi hàm
        return result
    return wrapper

@decorator
def ham_goc():
    print("Thực thi hàm gốc")
```

### 5. Tại sao dùng decorator?

- **Tái sử dụng mã**: Viết một lần, dùng cho nhiều hàm.
- **Tách biệt lo lắng (Separation of concerns)**: Logic chính tách biệt với logic phụ như log, xác thực, hiệu suất.
- **Sạch và dễ đọc**: Gắn decorator lên hàm giúp nhìn thấy ngay các hành vi bổ sung.

---

## Ví dụ minh họa

### Ví dụ 1: Decorator ghi log

Tạo decorator để ghi lại khi một hàm được gọi.

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Đang gọi hàm: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Hàm {func.__name__} đã hoàn tất")
        return result
    return wrapper

@log_decorator
def tinh_tong(a, b):
    return a + b
```

### Ví dụ 2: Đo thời gian thực thi

Decorator giúp đo thời gian thực thi của một hàm.

```python
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} thực thi trong {end - start:.4f}s")
        return result
    return wrapper

@time_decorator
def tinh_giai_thua(n):
    if n == 0:
        return 1
    return n * tinh_giai_thua(n - 1)
```

### Ví dụ 3: Decorator có tham số (Xác thực)

Tạo decorator nhận tham số, ví dụ kiểm tra quyền truy cập.

```python
def require_role(role_required):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != role_required:
                print(f"Từ chối: Cần quyền {role_required}")
                return None
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def xoa_nguoi_dung(user_role):
    print("Xóa người dùng thành công!")
```

---

## Bài tập thực hành

1. **Tạo decorator `@uppercase`**
   Viết một decorator biến kết quả trả về của hàm thành chữ in hoa. Áp dụng cho hàm trả về chuỗi.

2. **Tạo decorator `@retry`**
   Viết decorator cho phép thử lại hàm nếu xảy ra lỗi, tối đa 3 lần.

3. **Tạo decorator `@cache` đơn giản**
   Viết decorator lưu kết quả của hàm để không tính lại nếu tham số giống. Dùng cho hàm Fibonacci.

4. **Tạo decorator `@admin_only`**
   Viết decorator chỉ cho phép người dùng có tên là "admin" thực hiện hành động.

5. **Tạo decorator `@validate_types`**
   Kiểm tra kiểu dữ liệu đầu vào của hàm. Nếu sai kiểu, in cảnh báo và bỏ qua.

---

## Tổng kết

- Decorator là một kỹ thuật mạnh để mở rộng hàm mà không thay đổi nội dung gốc.
- Cấu trúc cơ bản: nhận hàm → trả về wrapper.
- Dùng `*args, **kwargs` để làm decorator linh hoạt.
- Có thể tạo decorator có tham số.
- Ứng dụng: log, hiệu suất, xác thực, cache, validation.

Decorators là nền tảng cho nhiều tính năng nâng cao trong Python như `@property`, `@classmethod`, `@staticmethod`, và các framework như Flask/Django. Hãy luyện tập thật nhiều để thành thạo!

---

> 💡 **Mẹo học tốt**: Thử viết lại các decorator từ đầu, thêm tính năng, và áp dụng vào dự án nhỏ.

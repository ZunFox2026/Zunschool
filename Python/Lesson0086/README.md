# Bài học Python Nâng cao số 86: Lập trình phản xạ (Reflection) với `inspect` và `getattr`, `setattr`, `hasattr`

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python — khả năng của một chương trình có thể tự quan sát và thay đổi cấu trúc, hành vi của chính nó tại **thời điểm chạy (runtime)**. Đây là một kỹ năng nâng cao, cực kỳ mạnh mẽ, được sử dụng trong các framework như Django, Flask, SQLAlchemy, hay các thư viện kiểm thử và serializing.

## 1. Mục tiêu bài học

- Hiểu được khái niệm lập trình phản xạ (reflection) trong Python.
- Sử dụng được các hàm `hasattr`, `getattr`, `setattr` để truy cập và thay đổi thuộc tính đối tượng một cách linh hoạt.
- Ứng dụng module `inspect` để khám phá các thông tin về hàm, lớp, tham số, stack call.
- Biết cách áp dụng reflection trong thực tế để xây dựng code linh hoạt, động, dễ mở rộng.

## 2. Lý thuyết chi tiết

### 2.1. `hasattr`, `getattr`, `setattr`

Đây là 3 hàm built-in giúp truy cập và thay đổi thuộc tính của đối tượng một cách động.

- `hasattr(obj, name)`: Kiểm tra xem đối tượng `obj` có thuộc tính/mетод tên `name` hay không.
- `getattr(obj, name, default)`): Lấy giá trị của thuộc tính `name` từ `obj`. Nếu không tồn tại, trả về `default` (nếu có), nếu không có `default` thì báo lỗi.
- `setattr(obj, name, value)`: Gán giá trị `value` cho thuộc tính `name` của `obj`.

```python
# Ví dụ cơ bản
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(hasattr(p, 'name'))     # True
print(getattr(p, 'name'))     # Alice
setattr(p, 'age', 25)
print(p.age)                  # 25
```

### 2.2. Module `inspect`

Module `inspect` cho phép bạn "nhìn vào" các đối tượng Python để lấy thông tin chi tiết:

- `inspect.getmembers(obj)`: Trả về danh sách các cặp (tên, giá trị) của tất cả các thuộc tính và phương thức của `obj`.
- `inspect.isfunction(obj)`, `inspect.ismethod(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Lấy chữ ký (tham số) của một hàm.
- `inspect.stack()`: Lấy thông tin về các hàm đang được gọi (call stack).

```python
import inspect

def greet(name, age=20):
    pass

sig = inspect.signature(greet)
for param in sig.parameters.values():
    print(param.name, param.default)  # name <class 'inspect._empty'>, age 20
```

## 3. Ví dụ minh họa

### Ví dụ 1: Gọi phương thức động dựa trên chuỗi đầu vào

Giả sử bạn có một lớp quản lý người dùng, và muốn gọi phương thức dựa trên lệnh người dùng nhập từ terminal.

### Ví dụ 2: Tự động đăng ký các lớp xử lý trong một hệ thống

Một ứng dụng có nhiều lớp xử lý (handler) cho các loại sự kiện. Dùng `inspect` để tự động tìm và đăng ký tất cả các lớp con.

### Ví dụ 3: Ghi log hành động truy cập thuộc tính

Sử dụng `getattr` và `hasattr` để kiểm tra và truy cập thuộc tính một cách an toàn, đồng thời ghi log khi có truy cập.

## 4. Bài tập thực hành

1. Viết hàm `call_method(obj, method_name, *args)` dùng `getattr` để gọi một phương thức của đối tượng nếu tồn tại.
2. Viết hàm `find_classes_in_module(module, base_class)` dùng `inspect` để tìm tất cả các lớp trong một module kế thừa từ `base_class`.
3. Viết hàm `safe_get(obj, attr_path, default=None)` để lấy giá trị lồng nhau (ví dụ: `user.profile.settings.theme`).
4. Viết hàm `log_calls(func)` là một decorator dùng `inspect.stack()` để in ra tên hàm gọi nó.
5. Tạo một hệ thống plugin đơn giản: các lớp plugin trong một module, dùng `inspect` để tự động phát hiện và khởi tạo.

## 5. Tổng kết

Lập trình phản xạ là một công cụ mạnh mẽ giúp Python trở nên cực kỳ linh hoạt. Khi dùng đúng cách, nó giúp:

- Viết code động, mở rộng mà không cần thay đổi nhiều.
- Xây dựng framework, thư viện, hệ thống plugin.
- Gỡ lỗi và kiểm thử hiệu quả hơn.

Tuy nhiên, cần thận trọng vì:

- Code có thể khó đọc, khó debug.
- Dễ gây lỗi runtime nếu không kiểm tra kỹ.

Hãy luôn kết hợp với kiểm tra kiểu, docstring, và unit test để đảm bảo độ tin cậy.

> ✅ **Lưu ý**: Dùng reflection khi cần thiết, không lạm dụng. Ưu tiên tính minh bạch và dễ bảo trì.
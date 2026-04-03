# Bài học Python nâng cao số 49: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python và cách sử dụng module `inspect` để khám phá, phân tích và thao tác với các đối tượng trong thời gian chạy chương trình. Đây là một chủ đề nâng cao nhưng cực kỳ hữu ích khi làm việc với framework, viết thư viện, hoặc khi cần debug, kiểm thử hoặc tự động hóa hành vi của chương trình.

## Mục tiêu bài học

- Hiểu được khái niệm **phản xạ (reflection)** trong lập trình.
- Biết cách sử dụng các hàm cơ bản như `getattr`, `setattr`, `hasattr`, `callable`.
- Sử dụng thành thạo module `inspect` để:
  - Lấy thông tin về hàm, lớp, tham số.
  - Kiểm tra stack call.
  - Tự động sinh tài liệu hoặc validate đầu vào.
- Áp dụng vào các tình huống thực tế như tạo decorator thông minh, validate tham số hàm, hoặc viết framework nhỏ.

## Lý thuyết chi tiết

### 1. Phản xạ (Reflection) là gì?

Phản xạ là khả năng của một chương trình trong việc tự kiểm tra và thay đổi cấu trúc, hành vi của chính nó trong lúc chạy. Python hỗ trợ rất tốt lập trình phản xạ nhờ vào bản chất động của ngôn ngữ.

#### Các hàm phản xạ cơ bản:

- `hasattr(obj, name)`: Kiểm tra xem đối tượng có thuộc tính nào không.
- `getattr(obj, name, default)`: Lấy giá trị của thuộc tính.
- `setattr(obj, name, value)`: Thiết lập giá trị cho thuộc tính.
- `callable(obj)`: Kiểm tra xem đối tượng có thể gọi được (hàm, phương thức) không.

**Ví dụ:**

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Xin chào, tôi là {self.name}"

p = Person("Anh")

print(hasattr(p, 'name'))     # True
print(getattr(p, 'greet')())  # Xin chào, tôi là Anh
print(callable(p.greet))      # True
```

### 2. Module `inspect`

Module `inspect` cho phép ta lấy thông tin chi tiết về các đối tượng Python như hàm, lớp, module, stack frame...

Một số hàm quan trọng:

- `inspect.getmembers(obj, predicate=None)`: Lấy danh sách các thành viên của đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`, `inspect.ismodule(obj)`
- `inspect.signature(func)`: Lấy chữ ký (tham số) của hàm.
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng (nếu có).
- `inspect.stack()`: Lấy thông tin về các frame gọi hàm hiện tại.

**Ví dụ lấy tham số hàm:**

```python
import inspect

def my_function(a: int, b: str = "hello", *args, **kwargs):
    pass

sig = inspect.signature(my_function)
for name, param in sig.parameters.items():
    print(f"{name}: {param.annotation} = {param.default}")
```

## Ví dụ minh họa

### Ví dụ 1: Tạo decorator tự động kiểm tra kiểu tham số dựa trên annotation

Sử dụng `inspect.signature` để đọc kiểu dữ liệu từ annotation và kiểm tra khi gọi hàm.

### Ví dụ 2: In ra tất cả phương thức public của một lớp

Dùng `inspect.getmembers` để lọc và in ra các phương thức của một đối tượng.

### Ví dụ 3: Ghi log tên hàm và tham số khi gọi (debug helper)

Tự động in ra tên hàm, tham số gọi bằng cách dùng `inspect.stack()`.

## Bài tập thực hành

1. Viết hàm `list_public_methods(cls)` nhận vào một lớp và in ra tất cả các phương thức public (không bắt đầu bằng `_`).
2. Viết decorator `@log_calls` ghi log mỗi khi một hàm được gọi, bao gồm tên hàm và tham số.
3. Viết hàm `analyze_function(func)` in ra chi tiết về một hàm: tham số, kiểu dữ liệu, giá trị mặc định.
4. Viết hàm `find_classes_in_module(module)` trả về danh sách các lớp trong một module.
5. Viết hàm `validate_call(func, **kwargs)` kiểm tra xem `kwargs` có phù hợp với chữ ký của `func` không.

## Tổng kết

Lập trình phản xạ và module `inspect` mở ra khả năng mạnh mẽ để viết code linh hoạt, thông minh và tự động hóa. Khi hiểu rõ cách hoạt động của chúng, bạn có thể:

- Viết các decorator mạnh mẽ.
- Tạo framework hoặc thư viện tự động cấu hình.
- Debug dễ dàng hơn.
- Kiểm thử tự động.

Tuy nhiên, cần sử dụng cẩn trọng vì có thể làm code khó đọc và tiềm ẩn lỗi nếu không kiểm soát tốt. Hãy luôn nhớ: **với sức mạnh đi kèm trách nhiệm**.

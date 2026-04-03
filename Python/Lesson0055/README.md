# Bài học Python nâng cao số 55: Lập trình phản xạ (Reflection) và sử dụng `inspect`

## Mục tiêu bài học
- Hiểu được khái niệm **lập trình phản xạ (reflection)** trong Python.
- Biết cách sử dụng module `inspect` để truy xuất thông tin về các đối tượng, hàm, lớp, tham số, stack,…
- Ứng dụng `inspect` trong thực tế: ghi log, debug tự động, xây dựng framework, tạo decorator linh hoạt.
- Thành thạo các hàm phổ biến như `inspect.getmembers()`, `inspect.signature()`, `inspect.stack()`.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ (Reflection) là gì?
Lập trình phản xạ là khả năng của một chương trình có thể **tự quan sát và thay đổi cấu trúc hoặc hành vi của chính nó** trong lúc chạy. Python hỗ trợ rất tốt lập trình phản xạ nhờ vào bản chất động của ngôn ngữ.

Ví dụ:
- Kiểm tra kiểu của một đối tượng bằng `type()`.
- Lấy danh sách các thuộc tính bằng `dir()`.
- Gọi hàm hoặc truy cập thuộc tính bằng tên chuỗi với `getattr()`, `setattr()`.

### 2. Module `inspect`
Module `inspect` cung cấp nhiều công cụ mạnh mẽ để lấy thông tin chi tiết về các đối tượng Python như:
- Hàm, lớp, phương thức, module
- Tham số, giá trị mặc định, annotation
- Stack trace, frame hiện tại

#### Một số hàm quan trọng:

- `inspect.getmembers(obj)`: Trả về danh sách các cặp (tên, giá trị) của các thành viên trong `obj`.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Trả về thông tin về tham số của hàm (kiểu, mặc định, annotation).
- `inspect.stack()`: Trả về thông tin về các frame trong stack gọi hàm.
- `inspect.getsource(obj)`: Lấy mã nguồn của một đối tượng (nếu có).

### 3. Ví dụ cơ bản
```python
import inspect

def hello(name: str, age: int = 20):
    return f"Xin chào {name}, bạn {age} tuổi."

# Lấy chữ ký hàm
sig = inspect.signature(hello)
for param in sig.parameters.values():
    print(param.name, param.annotation, param.default)
```

## Ví dụ minh họa

### Ví dụ 1: Ghi log tự động tên hàm và tham số
Tạo decorator dùng `inspect` để in ra tên hàm và các tham số khi gọi.

### Ví dụ 2: Kiểm tra và hiển thị thông tin về một lớp
In ra tất cả phương thức, thuộc tính, và kiểu dữ liệu của một lớp.

### Ví dụ 3: Xây dựng decorator kiểm tra kiểu tham số
Dùng `inspect.signature()` để kiểm tra kiểu tham số theo annotation và cảnh báo nếu sai.

## Bài tập thực hành
1. Viết hàm `print_caller_info()` in ra tên hàm gọi nó và dòng lệnh.
2. Viết hàm `list_public_methods(cls)` liệt kê các phương thức công khai của một lớp.
3. Tạo decorator `@log_execution_time` ghi log thời gian thực thi, dùng `inspect.stack()` để lấy tên hàm.
4. Viết hàm `validate_annotations(func)` kiểm tra kiểu tham số đầu vào dựa trên annotation.
5. Viết hàm `get_function_source_if_possible(func)` trả về mã nguồn nếu có, nếu không thì báo lỗi.

## Tổng kết
- `inspect` là công cụ mạnh mẽ để làm meta-programming trong Python.
- Ứng dụng nhiều trong debug, testing, framework (Flask, FastAPI, pytest đều dùng `inspect`).
- Nắm vững `inspect` giúp bạn viết code linh hoạt, tự động hóa, dễ bảo trì.
- Luôn kiểm tra điều kiện trước khi dùng (ví dụ: hàm có source code không?) để tránh lỗi.

> 📌 Tip: `inspect` là nền tảng cho nhiều tính năng nâng cao như auto-document, REPL, IDE hỗ trợ.

# Bài học Python nâng cao số 70: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python và cách sử dụng module `inspect` để khám phá, phân tích và thao tác với mã nguồn trong thời gian chạy. Đây là một chủ đề nâng cao, rất hữu ích khi làm việc với framework, công cụ tự động hóa, debug hoặc xây dựng thư viện.

## Mục tiêu bài học
- Hiểu được khái niệm lập trình phản xạ (reflection) trong Python.
- Biết cách sử dụng module `inspect` để lấy thông tin về hàm, lớp, tham số, stack, và mã nguồn.
- Ứng dụng `inspect` để xây dựng các công cụ ghi log thông minh, kiểm tra lỗi, hoặc tự động hóa.
- Nâng cao khả năng debug và viết mã linh hoạt, tự nhận thức.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ (Reflection) là gì?
Lập trình phản xạ là khả năng của một chương trình trong việc tự **xem xét, phân tích và thao tác** chính bản thân nó trong lúc đang chạy. Trong Python, mọi thứ đều là đối tượng (hàm, lớp, module, v.v.) nên ta có thể truy cập và kiểm tra thuộc tính của chúng bằng các hàm như:

- `type(obj)`: Xác định kiểu của đối tượng.
- `dir(obj)`: Liệt kê các thuộc tính và phương thức của đối tượng.
- `getattr(obj, name)`, `setattr(obj, name, value)`: Lấy hoặc gán giá trị thuộc tính.
- `hasattr(obj, name)`: Kiểm tra sự tồn tại của thuộc tính.
- `callable(obj)`: Kiểm tra xem đối tượng có thể gọi được không.

Tuy nhiên, để làm việc sâu hơn — như xem **tham số hàm**, **mã nguồn**, **stack call** — ta cần đến module `inspect`.

### 2. Module `inspect`
Module `inspect` cung cấp nhiều hàm mạnh mẽ để hỗ trợ reflection:

- `inspect.getmembers(obj)`: Trả về danh sách các cặp (tên, giá trị) của tất cả thành viên trong `obj`.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Trả về thông tin về tham số của hàm (kiểu, mặc định, v.v.).
- `inspect.getsource(obj)`: Lấy mã nguồn của hàm hoặc lớp.
- `inspect.getfile(obj)`: Lấy đường dẫn file chứa đối tượng.
- `inspect.stack()`: Trả về thông tin về các frame đang chạy (call stack).

### 3. Ứng dụng thực tế của `inspect`
- Ghi log tự động tên hàm và tham số.
- Kiểm tra đầu vào hàm (type checking tự động).
- Xây dựng decorator thông minh.
- Tạo tài liệu tự động (autodoc).
- Debug nâng cao (xem ai đã gọi hàm).

## Ví dụ minh họa

Bạn có thể xem các ví dụ hoàn chỉnh trong file `main.py`.

## Bài tập thực hành

Hãy hoàn thành các bài tập trong file `exercises.py`, sau đó kiểm tra lại với `solutions.py`.

## Tổng kết

Module `inspect` và kỹ thuật lập trình phản xạ là công cụ mạnh mẽ giúp bạn viết mã linh hoạt và thông minh hơn. Khi kết hợp với decorator, meta-programming, hoặc framework, `inspect` giúp bạn giảm lặp code, tăng tính tự động và khả năng debug. Hãy sử dụng cẩn thận vì nó có thể khiến mã khó theo dõi nếu dùng quá mức. Tuy nhiên, trong các tình huống phù hợp, nó là vũ khí lợi hại của lập trình viên Python nâng cao.
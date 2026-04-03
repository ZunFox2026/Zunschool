# Bài học Python Nâng cao - Bài 53: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

## Mục tiêu bài học
- Hiểu được khái niệm **lập trình phản xạ (reflection)** trong Python.
- Biết cách sử dụng module `inspect` để truy xuất thông tin về các đối tượng tại thời điểm chạy chương trình.
- Áp dụng `inspect` để ghi log, gỡ lỗi, phân tích mã nguồn tự động và xây dựng các công cụ phát triển.
- Nâng cao khả năng viết mã linh hoạt, tự động phát hiện và xử lý các thành phần trong chương trình.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ (Reflection) là gì?

Lập trình phản xạ là khả năng của một chương trình trong việc tự quan sát, phân tích và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy. Python hỗ trợ phản xạ rất mạnh mẽ nhờ vào đặc điểm là ngôn ngữ động.

Một số hàm built-in hỗ trợ phản xạ:
- `type(obj)`: trả về kiểu của đối tượng.
- `dir(obj)`: liệt kê các thuộc tính và phương thức của đối tượng.
- `hasattr(obj, 'attr')`: kiểm tra đối tượng có thuộc tính hay không.
- `getattr(obj, 'attr')`: lấy giá trị thuộc tính.
- `setattr(obj, 'attr', value)`: gán giá trị cho thuộc tính.
- `callable(obj)`: kiểm tra đối tượng có thể gọi được (hàm, phương thức) hay không.

Tuy nhiên, để phân tích sâu hơn (như tham số hàm, dòng mã nguồn, stack call…), ta cần dùng module `inspect`.

### 2. Module `inspect`

Module `inspect` cho phép ta lấy thông tin chi tiết về các đối tượng như hàm, lớp, phương thức, module, frame (khung gọi hàm), v.v.

Một số hàm quan trọng:
- `inspect.getmembers(obj)`: trả về danh sách các thành viên (thuộc tính, phương thức) của đối tượng.
- `inspect.isfunction(obj)`, `inspect.ismethod(obj)`, `inspect.isclass(obj)`: kiểm tra loại đối tượng.
- `inspect.getsource(obj)`: lấy mã nguồn của hàm hoặc lớp (nếu có sẵn).
- `inspect.signature(obj)`: lấy thông tin về tham số của hàm (kiểu tham số, mặc định, v.v.).
- `inspect.stack()`: lấy thông tin về các khung gọi hàm (call stack).

### Ví dụ minh họa

Dưới đây là các ví dụ thực tế sử dụng `inspect` để:
- Tự động ghi log khi gọi hàm.
- Phân tích mã nguồn để tìm các hàm không được dùng.
- Xây dựng một decorator ghi lại tham số đầu vào.

## Ví dụ minh họa

### Ví dụ 1: Ghi log tự động tên hàm và tham số sử dụng `inspect`

Chúng ta sẽ tạo một decorator dùng `inspect.signature` để in ra tên hàm và các tham số được truyền vào.

### Ví dụ 2: Kiểm tra mã nguồn các hàm trong một module

Sử dụng `inspect.getsource()` để in ra mã nguồn của các hàm, hữu ích trong các công cụ phân tích mã (linter, document generator).

### Ví dụ 3: Ghi lại call stack khi có lỗi

Dùng `inspect.stack()` để truy vết các hàm đã gọi khi xảy ra lỗi, giúp debug dễ dàng hơn.

## Bài tập thực hành

1. Viết một hàm `print_class_info(cls)` nhận vào một lớp và in ra tất cả các phương thức cùng tham số của chúng.
2. Tạo một decorator `@log_calls` ghi log tên hàm, tham số, và giá trị trả về vào file `debug.log`.
3. Viết hàm `find_functions_without_docstring(module)` tìm tất cả các hàm trong một module không có docstring.
4. Viết một hàm `who_called_me()` in ra tên hàm đã gọi nó, dùng `inspect.stack()`.

## Tổng kết

Lập trình phản xạ và module `inspect` là công cụ mạnh mẽ giúp Python trở thành ngôn ngữ linh hoạt cho phát triển các công cụ tự động: debug, testing, document generation, ORM, framework,…

Việc hiểu rõ `inspect` giúp bạn:
- Tự động hóa việc kiểm tra và xử lý mã nguồn.
- Xây dựng các công cụ hỗ trợ phát triển.
- Viết mã thông minh hơn, có khả năng tự điều chỉnh.

Tuy nhiên, cần sử dụng cẩn trọng vì phản xạ có thể làm mã khó đọc, giảm hiệu năng và tiềm ẩn lỗi nếu không kiểm soát tốt.
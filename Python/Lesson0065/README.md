# Bài học Python nâng cao số 65: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python và cách sử dụng module `inspect` để khám phá, phân tích mã nguồn, hàm, lớp, tham số, và ngăn xếp gọi hàm một cách động. Đây là một kỹ năng nâng cao rất hữu dụng khi viết các thư viện, framework, công cụ debug, hoặc hệ thống plugin.

## 1. Mục tiêu bài học
- Hiểu được khái niệm **lập trình phản xạ (reflection)** trong Python.
- Biết cách sử dụng module `inspect` để:
  - Lấy thông tin về hàm, lớp, phương thức.
  - Kiểm tra tham số, kiểu dữ liệu, giá trị mặc định.
  - Phân tích ngăn xếp gọi hàm (call stack).
  - Đọc mã nguồn của hàm.
- Áp dụng vào các tình huống thực tế như ghi log tự động, kiểm tra lỗi, xây dựng framework.

## 2. Lý thuyết chi tiết

### 2.1. Lập trình phản xạ là gì?
Lập trình phản xạ (reflection) là khả năng của một chương trình có thể tự tìm hiểu và thao tác với chính cấu trúc và hành vi của nó trong lúc chạy (runtime). Trong Python, điều này được hỗ trợ mạnh mẽ nhờ vào tính chất **mọi thứ đều là object**.

Một số hàm phản xạ cơ bản:
- `type(obj)`: lấy kiểu của đối tượng.
- `dir(obj)`: liệt kê các thuộc tính và phương thức của đối tượng.
- `hasattr(obj, 'attr')`: kiểm tra tồn tại thuộc tính.
- `getattr(obj, 'attr')`: lấy giá trị thuộc tính.
- `callable(obj)`: kiểm tra đối tượng có thể gọi được không.

### 2.2. Module `inspect`
Module `inspect` cung cấp nhiều công cụ để kiểm tra các đối tượng trong Python một cách chi tiết hơn.

Một số hàm quan trọng:
- `inspect.getmembers(obj)`: trả về danh sách các cặp (tên, giá trị) của tất cả thành viên trong obj.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: kiểm tra loại đối tượng.
- `inspect.signature(func)`: trả về chữ ký của hàm (tham số, kiểu, mặc định).
- `inspect.getsource(func)`: lấy mã nguồn của hàm dưới dạng chuỗi.
- `inspect.stack()`: trả về thông tin về ngăn xếp gọi hàm.

### 2.3. Ứng dụng thực tế
- Tự động ghi log khi gọi hàm.
- Kiểm tra tham số đầu vào trong các framework.
- Xây dựng hệ thống plugin động.
- Debug và phân tích lỗi nâng cao.

## 3. Ví dụ minh họa

### Ví dụ 1: Kiểm tra chữ ký hàm và tham số
Chương trình in ra chi tiết các tham số của một hàm.

### Ví dụ 2: Lấy mã nguồn của hàm
In ra mã nguồn của một hàm để kiểm tra hoặc ghi log.

### Ví dụ 3: Ghi log tự động tên hàm và tham số gọi
Sử dụng `inspect.stack()` để biết hàm nào đang gọi, với tham số gì.

## 4. Bài tập thực hành
1. Viết hàm `in_thong_tin_ham(func)` nhận vào một hàm và in ra tên, tham số, kiểu dữ liệu (nếu có), giá trị mặc định.
2. Viết hàm `kiem_tra_loi_goi(func, *args, **kwargs)` kiểm tra xem việc gọi hàm có hợp lệ không dựa trên chữ ký.
3. Viết decorator `@theo_doi` ghi log tên hàm, tham số đầu vào và giá trị trả về.
4. Viết hàm `tim_phuong_thuc_cua_lop(cls, ten_phuong_thuc)` tìm và in thông tin về một phương thức trong lớp.

## 5. Tổng kết
Lập trình phản xạ và module `inspect` là công cụ mạnh mẽ giúp Python trở thành ngôn ngữ linh hoạt. Khi viết các hệ thống lớn, việc tự động kiểm tra, phân tích và xử lý mã nguồn là rất cần thiết. Nắm vững kỹ năng này giúp bạn thiết kế các hệ thống nâng cao như framework, công cụ debug, hoặc hệ thống plugin.

> **Lưu ý**: Dùng phản xạ một cách thận trọng – nó có thể làm mã khó đọc và khó bảo trì nếu lạm dụng.

# Bài học Python nâng cao số 97: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python – một chủ đề nâng cao giúp bạn viết những chương trình có khả năng tự kiểm tra, phân tích và thay đổi cấu trúc hoặc hành vi của chính chúng trong lúc chạy. Đây là nền tảng cho nhiều công cụ như framework web, serializer, debugger, và các thư viện kiểm thử tự động.

Chúng ta sẽ tập trung vào module `inspect` – một công cụ mạnh mẽ để khám phá các đối tượng Python một cách lập trình.

## 1. Mục tiêu bài học
- Hiểu khái niệm lập trình phản xạ (reflection) trong Python.
- Biết cách sử dụng module `inspect` để truy xuất thông tin về hàm, lớp, tham số, và stack.
- Ứng dụng `inspect` để xây dựng các hàm thông minh tự động xử lý tham số.
- Viết các decorator linh hoạt dựa trên thông tin phản xạ.

## 2. Lý thuyết chi tiết

### 2.1. Phản xạ (Reflection) là gì?
Phản xạ là khả năng của một chương trình để tự quan sát và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc thực thi. Python hỗ trợ phản xạ rất mạnh mẽ thông qua các hàm như:
- `type()`, `isinstance()`
- `hasattr()`, `getattr()`, `setattr()`, `delattr()`
- `dir()`
- `callable()`

Nhưng để đạt đến cấp độ nâng cao, chúng ta cần đến **module `inspect`**.

### 2.2. Module `inspect`
Module `inspect` cung cấp các hàm để truy xuất thông tin chi tiết về các đối tượng Python như:
- Thông tin hàm: tên, tham số, giá trị mặc định, annotation
- Stack trace: gọi hàm từ đâu, đang ở đâu
- Kiểm tra lớp, thuộc tính, phương thức

Một số hàm quan trọng:
- `inspect.getmembers(obj)`: lấy tất cả thành viên của đối tượng
- `inspect.signature(func)`: lấy chữ ký của hàm (tham số, kiểu, mặc định)
- `inspect.getsource(obj)`: lấy mã nguồn của hàm hoặc lớp
- `inspect.stack()`: lấy thông tin về stack gọi hàm

### 2.3. Ứng dụng thực tế
- Ghi log tự động tên hàm và tham số
- Xây dựng decorator thông minh
- Tạo API tự động từ các hàm
- Kiểm thử tự động (unit test)

## 3. Ví dụ minh họa

Xem trong file `main.py` để chạy các ví dụ hoàn chỉnh về:
- Trích xuất tham số hàm bằng `inspect.signature`
- Viết decorator ghi log với thông tin đầy đủ
- Kiểm tra mã nguồn và stack trace

## 4. Bài tập thực hành

Xem trong file `exercises.py`. Hãy hoàn thành các hàm theo yêu cầu:
1. Viết hàm kiểm tra tham số bắt buộc của một hàm
2. Viết decorator tự động kiểm tra kiểu tham số
3. Viết hàm in ra tên hàm gọi nó bằng stack

## 5. Tổng kết

Lập trình phản xạ và module `inspect` là công cụ mạnh mẽ giúp bạn viết code linh hoạt, thông minh và tự động. Nắm vững kỹ năng này sẽ giúp bạn phát triển các thư viện, framework, hoặc công cụ debug hiệu quả hơn. Tuy nhiên, cần sử dụng cẩn trọng vì có thể làm code khó hiểu nếu lạm dụng.

Hãy thực hành kỹ các bài tập để thành thạo!
# Bài học Python số 52 - Cấp độ Nâng cao

## Chủ đề: Thiết kế và sử dụng **Descriptor** trong Python

Trong bài học này, chúng ta sẽ tìm hiểu về **Descriptor Protocol** — một trong những tính năng nâng cao nhưng cực kỳ mạnh mẽ trong Python, cho phép bạn tùy chỉnh hành vi của thuộc tính trong lớp. Descriptors là nền tảng cho nhiều tính năng tích hợp như `property`, `classmethod`, và `staticmethod`.

### Mục tiêu bài học
- Hiểu được khái niệm Descriptor và tại sao nó hữu ích.
- Nắm vững cách triển khai một Descriptor bằng cách sử dụng các phương thức đặc biệt `__get__`, `__set__`, và `__delete__`.
- Áp dụng Descriptor để kiểm soát truy cập thuộc tính, kiểm tra dữ liệu, hoặc thực hiện ghi log.
- Giải quyết các bài toán thực tế như xác thực kiểu dữ liệu, quản lý trạng thái, hoặc xây dựng các lớp dữ liệu thông minh.

### Lý thuyết chi tiết

**Descriptor** là một đối tượng thực hiện một trong các phương thức sau:
- `__get__(self, instance, owner)`
- `__set__(self, instance, value)`
- `__delete__(self, instance)`

Khi một đối tượng như vậy được khai báo là thuộc tính của một lớp (không phải của instance), Python sẽ kích hoạt các phương thức này khi truy cập, gán hoặc xóa thuộc tính đó.

#### Khi nào nên dùng Descriptor?
- Khi bạn muốn kiểm soát việc đọc/ghi/xóa một thuộc tính.
- Khi bạn cần chia sẻ logic kiểm soát giữa nhiều thuộc tính hoặc nhiều lớp.
- Khi bạn muốn xây dựng các trường dữ liệu thông minh (ví dụ: tự động chuyển đổi kiểu, ghi log, cache, xác thực).

#### Cú pháp cơ bản:
```python
class MyDescriptor:
    def __get__(self, instance, owner):
        ...
    def __set__(self, instance, value):
        ...
    def __delete__(self, instance):
        ...

class MyClass:
    attr = MyDescriptor()  # attr là một descriptor
```

### Ví dụ minh họa

Chúng ta sẽ cùng xây dựng:
1. Một descriptor để đảm bảo thuộc tính chỉ nhận giá trị số dương.
2. Một descriptor kiểm tra kiểu dữ liệu.
3. Một descriptor ghi log mỗi khi thuộc tính được truy cập.

### Bài tập thực hành
- Viết descriptor kiểm tra email.
- Viết descriptor chỉ cho phép giá trị nằm trong danh sách lựa chọn.
- Viết descriptor tự động mã hóa/giải mã một thuộc tính.

### Tổng kết
Descriptor là một công cụ mạnh mẽ để kiểm soát hành vi của thuộc tính trong Python. Mặc dù khó tiếp cận hơn `@property`, nhưng nó linh hoạt và tái sử dụng tốt hơn, đặc biệt khi bạn cần áp dụng cùng logic cho nhiều thuộc tính. Hiểu rõ descriptor giúp bạn đọc hiểu sâu hơn về cách Python hoạt động bên trong.

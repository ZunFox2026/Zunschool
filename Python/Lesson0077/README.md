# Bài học Python Nâng cao - Bài 77: Sử dụng Descriptor để Tạo Thuộc Tính Thông Minh

Trong bài học này, chúng ta sẽ tìm hiểu về **Descriptor** – một tính năng nâng cao trong Python cho phép bạn tùy chỉnh cách truy cập, gán và xóa giá trị của thuộc tính trong lớp. Descriptor là nền tảng cho nhiều tính năng như `property`, `classmethod`, `staticmethod`, và được sử dụng rộng rãi trong các framework như Django, SQLAlchemy.

Descriptor giúp bạn viết code linh hoạt, tái sử dụng cao và kiểm soát chặt chẽ hành vi của thuộc tính.

## Mục tiêu bài học
- Hiểu được khái niệm và cơ chế hoạt động của Descriptor.
- Biết cách tạo và sử dụng Descriptor để kiểm soát truy cập thuộc tính.
- Ứng dụng Descriptor trong các tình huống thực tế như xác thực dữ liệu, ghi log, caching.
- Tự tin sử dụng Descriptor trong các dự án nâng cao.

## Lý thuyết chi tiết

### 1. Descriptor là gì?

Một **Descriptor** là một đối tượng (thường là một lớp) triển khai một (hoặc nhiều) trong ba phương thức đặc biệt sau:
- `__get__(self, instance, owner)`
- `__set__(self, instance, value)`
- `__delete__(self, instance)`

Khi một đối tượng descriptor được gán làm thuộc tính của một lớp, Python sẽ tự động gọi các phương thức này khi truy cập, gán hoặc xóa thuộc tính đó.

> 🔹 Nếu chỉ có `__get__` → non-data descriptor (ví dụ: hàm, method)
> 🔹 Nếu có `__set__` hoặc `__delete__` → data descriptor (ưu tiên cao hơn `__dict__`)

### 2. Cú pháp cơ bản

```python
class MyDescriptor:
    def __get__(self, instance, owner):
        # Trả về giá trị khi truy cập thuộc tính
        pass

    def __set__(self, instance, value):
        # Xử lý khi gán giá trị
        pass

    def __delete__(self, instance):
        # Xử lý khi xóa
        pass
```

### 3. Ví dụ đơn giản

Một descriptor đơn giản để in log mỗi khi truy cập hoặc gán giá trị:

```python
class LoggedAttribute:
    def __get__(self, instance, owner):
        print("Đọc thuộc tính")
        return instance._value

    def __set__(self, instance, value):
        print(f"Gán giá trị: {value}")
        instance._value = value
```

## Ví dụ minh họa

### Ví dụ 1: Kiểm tra giá trị hợp lệ với Descriptor

Tạo một lớp descriptor để đảm bảo một thuộc tính luôn là số dương.

### Ví dụ 2: Thuộc tính có giá trị được tính toán và cache

Sử dụng descriptor để lưu trữ kết quả tính toán nặng và chỉ tính lại khi cần.

### Ví dụ 3: Ghi log truy cập thuộc tính

Tạo descriptor để theo dõi mọi lần truy cập/gán vào thuộc tính.

## Bài tập thực hành

1. Tạo descriptor cho thuộc tính email, đảm bảo định dạng hợp lệ.
2. Viết descriptor để giới hạn số lần truy cập một thuộc tính.
3. Tạo descriptor cho thuộc tính chỉ đọc (read-only).
4. Viết descriptor theo dõi thời gian truy cập thuộc tính.
5. Tạo descriptor hỗ trợ kiểu dữ liệu cố định (type enforcement).

## Tổng kết

- Descriptor là một công cụ mạnh để kiểm soát hành vi của thuộc tính.
- Có thể dùng để xác thực, logging, caching, kiểm soát quyền truy cập.
- Hiểu rõ descriptor giúp bạn đọc hiểu code của các framework lớn.
- Cần lưu ý thứ tự ưu tiên: data descriptor > instance.__dict__ > non-data descriptor.

Descriptor là một phần quan trọng trong hệ thống dữ liệu thuộc tính của Python. Khi sử dụng đúng cách, chúng giúp code sạch hơn, an toàn hơn và linh hoạt hơn.

---
> 📌 **Gợi ý học tập**:
> - Xem lại cơ chế `__getattribute__` để hiểu sâu hơn về luồng truy cập thuộc tính.
> - Thử debug một class có descriptor để xem thứ tự gọi các phương thức.

# Bài học Python Nâng cao - Bài 41: Lập trình phản xạ (Reflection) với `inspect` và `getattr`, `setattr`, `hasattr`

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python — một kỹ năng nâng cao giúp chương trình có khả năng "tự quan sát" và thao tác với chính cấu trúc của nó như các lớp, phương thức, thuộc tính, tham số hàm, v.v.

Python hỗ trợ rất mạnh tính năng này thông qua các hàm built-in như `getattr`, `setattr`, `hasattr` và module `inspect`. Đây là nền tảng cho nhiều framework nổi tiếng như Django, Flask, Pydantic, v.v.

## Mục tiêu bài học

- Hiểu được khái niệm lập trình phản xạ (reflection) trong Python.
- Sử dụng linh hoạt các hàm `getattr`, `setattr`, `hasattr` để truy cập và thay đổi thuộc tính/ phương thức của đối tượng.
- Khai thác module `inspect` để lấy thông tin chi tiết về hàm, lớp, stack, tham số, v.v.
- Ứng dụng reflection để xây dựng các chương trình linh hoạt, tự động hóa, hoặc kiểm thử.

## Lý thuyết chi tiết

### 1. `getattr`, `setattr`, `hasattr`

Đây là ba hàm built-in cho phép truy cập, thiết lập và kiểm tra sự tồn tại của thuộc tính trong một đối tượng dựa trên tên (dưới dạng chuỗi).

```python
getattr(obj, 'attribute_name', default)  # Lấy giá trị thuộc tính
setattr(obj, 'attribute_name', value)      # Thiết lập giá trị
hasattr(obj, 'attribute_name')             # Kiểm tra tồn tại
```

### 2. Module `inspect`

Module `inspect` cho phép kiểm tra chi tiết cấu trúc chương trình như:
- Lấy danh sách các thành viên của một đối tượng: `inspect.getmembers(obj)`
- Lấy thông tin về hàm: tên, tham số, giá trị mặc định: `inspect.signature(func)`
- Lấy stack gọi hàm: `inspect.stack()`
- Kiểm tra loại đối tượng: `inspect.isfunction()`, `inspect.isclass()`, v.v.

## Ví dụ minh họa

1. **Tự động gọi phương thức qua tên chuỗi**
2. **Tạo báo cáo chi tiết về một lớp bằng `inspect`**
3. **Xây dựng hệ thống ghi log tự động tên hàm và tham số**

## Bài tập thực hành

1. Viết hàm kiểm tra và gọi phương thức an toàn trên đối tượng.
2. Liệt kê tất cả phương thức công khai của một lớp.
3. Tạo hàm in thông tin chi tiết về tham số của một hàm bất kỳ.
4. Xây dựng một decorator ghi log tự động tên hàm và tham số đầu vào.

## Tổng kết

Lập trình phản xạ giúp Python trở nên cực kỳ linh hoạt. Việc hiểu và sử dụng `inspect` và các hàm `getattr`, `setattr`, `hasattr` không chỉ nâng cao khả năng lập trình mà còn giúp bạn đọc hiểu mã nguồn của các framework lớn. Tuy nhiên, cần sử dụng cẩn trọng để tránh làm mã nguồn trở nên khó hiểu hoặc dễ lỗi.

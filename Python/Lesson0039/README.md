# Python 39: Lập Trình Hướng Đối Tượng Cơ Bản

## Giới thiệu

Lập trình hướng đối tượng (Object-Oriented Programming - OOP) là một phương pháp lập trình phổ biến trong Python, giúp tổ chức và quản lý mã nguồn một cách hiệu quả hơn. Thay vì viết các hàm rời rạc, OOP cho phép nhóm dữ liệu và hành vi liên quan vào các đối tượng. Bài học này sẽ giới thiệu những khái niệm cơ bản như lớp (class), đối tượng (object), thuộc tính và phương thức, giúp bạn bắt đầu với OOP trong Python.

## Lý thuyết

Trong OOP, **lớp (class)** là bản mẫu để tạo ra các **đối tượng (object)**. Mỗi đối tượng có thể chứa **thuộc tính** (dữ liệu) và **phương thức** (hàm hành động).  
Các khái niệm chính:
- **Class**: Khuôn mẫu định nghĩa cấu trúc và hành vi.
- **Object**: Thực thể được tạo từ lớp.
- **`__init__`**: Phương thức khởi tạo, dùng để thiết lập các thuộc tính ban đầu.
- **self**: Tham chiếu đến đối tượng hiện tại, luôn là tham số đầu tiên trong các phương thức.

## Ví dụ

Dưới đây là ví dụ về một lớp `Nguoi` đại diện cho một người:

```python
class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def gioi_thieu(self):
        print(f"Xin chào, tôi là {self.ten}, {self.tuoi} tuổi.")

# Tạo đối tượng từ lớp
nguoi1 = Nguoi("An", 20)
nguoi1.gioi_thieu()  # Kết quả: Xin chào, tôi là An, 20 tuổi.
```

## Bài tập

1. Tạo một lớp `HinhChuNhat` với các thuộc tính `chieu_dai` và `chieu_rong`.
2. Viết phương thức `tinh_dien_tich()` để tính diện tích hình chữ nhật.
3. Viết phương thức `tinh_chu_vi()` để tính chu vi.
4. Tạo một đối tượng hình chữ nhật với chiều dài 5 và chiều rộng 3, rồi in ra diện tích và chu vi.

> Gợi ý: Sử dụng `__init__` để khởi tạo các thuộc tính. Diện tích = dài × rộng, chu vi = 2 × (dài + rộng).
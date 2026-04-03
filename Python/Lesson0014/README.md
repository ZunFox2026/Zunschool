# Python 14: Lập Trình Hướng Đối Tượng Cơ Bản

## Giới thiệu

Lập trình hướng đối tượng (OOP - Object-Oriented Programming) là một trong những phương pháp lập trình phổ biến, giúp tổ chức và cấu trúc code một cách rõ ràng, dễ bảo trì và tái sử dụng. Trong bài học này, bạn sẽ được làm quen với các khái niệm cơ bản như lớp (class), đối tượng (object), thuộc tính (attribute) và phương thức (method) trong Python.

## Lý thuyết

Trong lập trình hướng đối tượng, **lớp (class)** là bản thiết kế để tạo ra các **đối tượng (object)**. Mỗi đối tượng có thể chứa **thuộc tính** (dữ liệu) và **phương thức** (hàm). Một số khái niệm cốt lõi:

- **Class**: Khuôn mẫu để tạo đối tượng.
- **Object**: Thể hiện cụ thể của một class.
- **`__init__`**: Phương thức khởi tạo, được gọi khi tạo đối tượng mới.
- **`self`**: Tham chiếu đến chính đối tượng hiện tại, dùng để truy cập các thuộc tính và phương thức bên trong class.

## Ví dụ

Dưới đây là một ví dụ đơn giản về class `Nguoi`:

```python
class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def gioi_thieu(self):
        print(f"Xin chào, tôi là {self.ten}, {self.tuoi} tuổi.")

# Tạo đối tượng
nguoi1 = Nguoi("An", 20)
nguoi1.gioi_thieu()  # Kết quả: Xin chào, tôi là An, 20 tuổi.
```

Trong ví dụ trên:
- `Nguoi` là một class.
- `nguoi1` là một đối tượng của class `Nguoi`.
- `gioi_thieu()` là một phương thức in thông tin của đối tượng.

## Bài tập

1. Tạo một class `HinhChuNhat` với các thuộc tính `chieu_dai` và `chieu_rong`, cùng hai phương thức:
   - `tinh_dien_tich()` để tính diện tích.
   - `tinh_chu_vi()` để tính chu vi.
2. Tạo một đối tượng hình chữ nhật có chiều dài 10, chiều rộng 5, rồi in ra diện tích và chu vi của nó.

> 💡 Gợi ý: Sử dụng `__init__` để khởi tạo các thuộc tính và viết các phương thức tính toán như yêu cầu.
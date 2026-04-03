# Python 15 cấp Cơ bản – Bài 15: Hàm trong Python

## Giới thiệu

Trong lập trình Python, **hàm** (function) là một khối lệnh thực hiện một nhiệm vụ cụ thể và có thể được tái sử dụng nhiều lần. Việc sử dụng hàm giúp chương trình trở nên rõ ràng, dễ quản lý và tránh lặp lại mã. Bài học này sẽ giới thiệu cách định nghĩa, gọi và sử dụng hàm trong Python – một kiến thức cơ bản nhưng cực kỳ quan trọng trong hành trình học lập trình.

## Lý thuyết

Trong Python, hàm được định nghĩa bằng từ khóa `def`, theo sau là tên hàm, dấu ngoặc đơn `()` và dấu hai chấm `:`. Các câu lệnh bên trong hàm phải được thụt lề đúng cách.

Cú pháp:
```python
def ten_ham(tham_so):
    # Các câu lệnh
    return gia_tri
```

- `ten_ham`: Tên do người dùng đặt, nên mang tính mô tả.
- `tham_so`: Dữ liệu đầu vào (không bắt buộc).
- `return`: Trả về giá trị (nếu có). Nếu không có `return`, hàm trả về `None`.

Hàm chỉ chạy khi được **gọi** (invoke). Bạn có thể gọi hàm bằng cách viết tên hàm kèm theo dấu ngoặc.

## Ví dụ

Dưới đây là một hàm đơn giản in lời chào:

```python
def xin_chao(ten):
    print(f"Xin chào, {ten}!")

# Gọi hàm
xin_chao("An")
# Kết quả: Xin chào, An!
```

Hàm tính tổng hai số:

```python
def tinh_tong(a, b):
    return a + b

ket_qua = tinh_tong(5, 3)
print("Tổng là:", ket_qua)  # Kết quả: Tổng là: 8
```

## Bài tập

1. Viết hàm `tinh_binh_phuong(x)` nhận một số và trả về bình phương của nó. Gọi hàm với giá trị 4.
2. Viết hàm `in_loi_chuc(ten, tuoi)` in ra lời chúc sinh nhật như: *"Chúc mừng sinh nhật tên! Chúc bạn tuổi tuoi vui vẻ!"*.
3. Viết hàm `kiem_tra_chan_le(n)` kiểm tra và in ra số `n` là chẵn hay lẻ.

> Gợi ý: Sử dụng toán tử `%` để kiểm tra chia hết cho 2.
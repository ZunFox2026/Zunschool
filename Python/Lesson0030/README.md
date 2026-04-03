# Bài 30: Python Cơ bản

## Giới thiệu

Python là một ngôn ngữ lập trình phổ biến nhờ cú pháp đơn giản, dễ đọc và khả năng ứng dụng rộng rãi trong nhiều lĩnh vực như phát triển web, khoa học dữ liệu, trí tuệ nhân tạo và tự động hóa. Bài học này sẽ giới thiệu những khái niệm cơ bản nhất trong Python, giúp người mới bắt đầu làm quen với cách viết và chạy chương trình đơn giản.

## Lý thuyết

Trong Python, bạn không cần khai báo kiểu dữ liệu khi tạo biến – ngôn ngữ tự động suy ra kiểu dựa trên giá trị được gán. Các kiểu dữ liệu cơ bản bao gồm:
- `int`: số nguyên (ví dụ: `5`, `-3`)
- `float`: số thực (ví dụ: `3.14`, `-0.5`)
- `str`: chuỗi ký tự (ví dụ: `"Hello"`)
- `bool`: giá trị logic `True` hoặc `False`

Câu lệnh điều kiện `if-else`, vòng lặp `for` và `while`, cùng với việc định nghĩa hàm bằng từ khóa `def` là những cấu trúc điều khiển quan trọng trong Python.

## Ví dụ

Dưới đây là một chương trình Python đơn giản in ra thông báo và thực hiện phép tính:

```python
# In chào mừng
print("Chào mừng đến với Python cơ bản!")

# Tính tổng hai số
a = 10
b = 5
tong = a + b
print(f"Tổng của {a} và {b} là: {tong}")

# Sử dụng câu lệnh điều kiện
if tong > 10:
    print("Tổng lớn hơn 10")
else:
    print("Tổng nhỏ hơn hoặc bằng 10")
```

Kết quả chạy chương trình:
```
Chào mừng đến với Python cơ bản!
Tổng của 10 và 5 là: 15
Tổng lớn hơn 10
```

## Bài tập

1. Viết chương trình nhập vào hai số từ bàn phím và in ra tích của chúng.
2. Viết hàm `kiem_tra_chan_le(n)` nhận một số nguyên `n` và in ra `"Chẵn"` nếu `n` chia hết cho 2, ngược lại in ra `"Lẻ"`.
3. Sử dụng vòng lặp `for` để in các số từ 1 đến 5.

> Gợi ý: Dùng `input()` để nhận dữ liệu người dùng, nhớ chuyển đổi sang kiểu số bằng `int()`.
# Bài 52: Tổng Hợp Kiến Thức Python Cơ Bản

## Giới thiệu

Bài học này tổng hợp lại các kiến thức cơ bản về ngôn ngữ lập trình Python, phù hợp cho người mới bắt đầu. Python là ngôn ngữ dễ học, cú pháp rõ ràng và mạnh mẽ, được sử dụng rộng rãi trong nhiều lĩnh vực như lập trình web, phân tích dữ liệu, trí tuệ nhân tạo,... Hiểu vững kiến thức cơ bản sẽ là nền tảng giúp bạn phát triển kỹ năng lập trình hiệu quả hơn.

## Lý thuyết

Python cung cấp nhiều tính năng cơ bản nhưng quan trọng như:

- **Biến và kiểu dữ liệu**: Số nguyên (`int`), số thực (`float`), chuỗi (`str`), boolean (`bool`).
- **Cấu trúc điều khiển**: `if`, `elif`, `else` để rẽ nhánh; `for` và `while` để lặp.
- **Hàm**: Dùng `def` để định nghĩa hàm, giúp tái sử dụng mã.
- **Danh sách (list)**: Cấu trúc lưu trữ nhiều phần tử, có thể thay đổi.
- **Xử lý chuỗi**: Các phương thức như `split()`, `join()`, `upper()`, `lower()`.

## Ví dụ

Dưới đây là ví dụ tổng hợp sử dụng các kiến thức cơ bản:

```python
# Định nghĩa hàm kiểm tra số chẵn/lẻ
def kiem_tra_chan_le(n):
    if n % 2 == 0:
        return "Số chẵn"
    else:
        return "Số lẻ"

# Danh sách các số
so = [1, 2, 3, 4, 5]

# In kết quả kiểm tra từng số
for num in so:
    ket_qua = kiem_tra_chan_le(num)
    print(f"Số {num} là {ket_qua}")

# Xử lý chuỗi
ten = "python co ban"
print(ten.upper())  # In hoa toàn bộ
```

**Kết quả:**
```
Số 1 là Số lẻ
Số 2 là Số chẵn
Số 3 là Số lẻ
Số 4 là Số chẵn
Số 5 là Số lẻ
PYTHON CO BAN
```

## Bài tập

1. Viết chương trình nhập vào một danh sách số và in ra số lớn nhất, nhỏ nhất.
2. Tạo hàm tính tổng các số từ 1 đến n (với n là tham số).
3. Nhập một chuỗi và đếm số từ trong chuỗi đó (phân cách bởi khoảng trắng).
4. Sử dụng vòng lặp `while` để in các số từ 10 về 1.

> Gợi ý: Sử dụng `input()` để nhận dữ liệu, `max()`, `min()`, `len()`, và các cấu trúc điều khiển đã học.
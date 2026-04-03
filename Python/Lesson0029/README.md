# Python 29: Xử Lý Danh Sách và Vòng Lặp

## Giới thiệu

Trong lập trình Python, danh sách (list) và vòng lặp là hai khái niệm cơ bản nhưng cực kỳ quan trọng. Danh sách giúp lưu trữ nhiều giá trị trong một biến duy nhất, còn vòng lặp cho phép thực hiện lặp lại một đoạn mã nhiều lần. Bài học này sẽ giúp bạn làm chủ cách sử dụng danh sách kết hợp với vòng lặp để xử lý dữ liệu một cách hiệu quả.

## Lý thuyết

Danh sách trong Python được khai báo bằng cặp dấu ngoặc vuông `[]`, có thể chứa nhiều kiểu dữ liệu khác nhau. Vòng lặp `for` thường được dùng để duyệt qua từng phần tử trong danh sách.

Cú pháp cơ bản:
```python
for phần_tử in danh_sách:
    # Thực hiện công việc với phần_tử
```

Bạn cũng có thể sử dụng `while` để lặp theo chỉ số, hoặc các phương thức như `append()`, `remove()`, `len()` để thao tác với danh sách.

## Ví dụ

Dưới đây là ví dụ sử dụng vòng lặp `for` để in từng phần tử trong danh sách và tính tổng các số:

```python
# Danh sách điểm số
diem_so = [8, 9, 7, 10, 6]

# In từng điểm số
print("Các điểm số:")
for diem in diem_so:
    print(diem)

# Tính tổng điểm
tong = 0
for diem in diem_so:
    tong += diem

print("Tổng điểm:", tong)
```

Kết quả:
```
Các điểm số:
8
9
7
10
6
Tổng điểm: 40
```

## Bài tập

1. Tạo một danh sách chứa tên của 5 người bạn, rồi in ra từng tên sử dụng vòng lặp `for`.
2. Viết chương trình tính trung bình cộng của các số trong danh sách: `[10, 20, 30, 40]`.
3. Thêm phần tử `15` vào cuối danh sách `[5, 10, 20]` rồi in lại danh sách sau khi thêm.

> Gợi ý: Dùng `append()` để thêm phần tử, `len()` để đếm số lượng phần tử.
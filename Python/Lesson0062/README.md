# Bài Python 62: Xử Lý Danh Sách và Vòng Lặp Cơ Bản

## Giới thiệu

Trong lập trình Python, danh sách (list) và vòng lặp là hai khái niệm cơ bản nhưng cực kỳ quan trọng. Danh sách giúp lưu trữ nhiều giá trị trong một biến duy nhất, còn vòng lặp cho phép thực hiện lặp lại một đoạn mã với các phần tử trong danh sách. Bài học này sẽ giúp bạn nắm vững cách xử lý danh sách và sử dụng vòng lặp `for` để duyệt qua các phần tử — nền tảng thiết yếu để phát triển các chương trình Python hiệu quả.

## Lý thuyết

- **Danh sách (List)**: Là cấu trúc dữ liệu lưu trữ tập hợp các phần tử có thể thay đổi (mutable), được khai báo bằng dấu ngoặc vuông `[]`. Ví dụ: `numbers = [1, 2, 3]`.
- **Vòng lặp `for`**: Dùng để duyệt qua từng phần tử trong danh sách. Cú pháp:  
  ```python
  for phần_tử in danh_sách:
      # thực hiện lệnh
  ```
- Bạn cũng có thể truy cập chỉ số phần tử bằng hàm `range()` kết hợp `len()` hoặc dùng `enumerate()`.

## Ví dụ

Dưới đây là ví dụ minh họa cách sử dụng vòng lặp để in và xử lý các phần tử trong danh sách:

```python
# Danh sách điểm số
diem_so = [8, 5, 9, 7, 10]

# In từng điểm số
print("Các điểm số:")
for diem in diem_so:
    print(diem)

# Tính tổng điểm
tong = 0
for diem in diem_so:
    tong += diem
print(f"Tổng điểm: {tong}")

# In điểm kèm thứ tự
print("Điểm theo thứ tự:")
for i, diem in enumerate(diem_so, start=1):
    print(f"Người chơi {i}: {diem} điểm")
```

## Bài tập

1. Tạo một danh sách chứa tên của 5 người bạn, sau đó in ra màn hình bằng vòng lặp `for`.
2. Viết chương trình tính trung bình cộng của các số trong danh sách: `[4, 8, 6, 10, 3]`.
3. Duyệt danh sách và in ra các số chẵn từ danh sách: `[1, 4, 7, 8, 10, 13]`.
4. *(Nâng cao)*: Tạo danh sách chuỗi và in ra các phần tử có độ dài lớn hơn 5 ký tự.
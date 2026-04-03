# Python 37: Làm Quen Với Biến Và Kiểu Dữ Liệu

## Giới thiệu

Trong lập trình Python, **biến** và **kiểu dữ liệu** là hai khái niệm cơ bản và quan trọng nhất mà mọi người học lập trình cần nắm vững. Biến giúp lưu trữ dữ liệu, còn kiểu dữ liệu xác định loại giá trị mà biến có thể chứa, như số, văn bản, hay giá trị đúng/sai. Bài học này sẽ giúp bạn làm quen với cách khai báo biến và các kiểu dữ liệu phổ biến trong Python như `int`, `float`, `str`, và `bool`.

## Lý thuyết

Trong Python, bạn không cần khai báo kiểu dữ liệu khi tạo biến — Python tự động suy ra kiểu dữ liệu dựa trên giá trị được gán. Cú pháp khai báo biến rất đơn giản:

```python
tên_biến = giá_trị
```

Một số kiểu dữ liệu cơ bản:
- `int`: số nguyên, ví dụ: `5`, `-3`
- `float`: số thực, ví dụ: `3.14`, `-0.5`
- `str`: chuỗi ký tự, ví dụ: `"Xin chào"`, `'Python'`
- `bool`: giá trị logic, chỉ nhận `True` hoặc `False`

Tên biến phải bắt đầu bằng chữ cái hoặc dấu gạch dưới, không chứa dấu cách, và phân biệt chữ hoa/chữ thường.

## Ví dụ

```python
# Khai báo và sử dụng biến
tuoi = 20
chieu_cao = 1.75
ten = "An"
la_sinh_vien = True

# In thông tin ra màn hình
print("Tên:", ten)
print("Tuổi:", tuoi)
print("Chiều cao:", chieu_cao, "m")
print("Là sinh viên:", la_sinh_vien)
```

Kết quả:
```
Tên: An
Tuổi: 20
Chiều cao: 1.75 m
Là sinh viên: True
```

## Bài tập

1. Tạo một biến `ho_ten` và gán tên của bạn vào đó, sau đó in ra màn hình.
2. Tạo hai biến `a` và `b` với giá trị số bất kỳ, tính tổng và in kết quả.
3. Tạo biến `dung` có giá trị `True` và biến `sai` có giá trị `False`, in cả hai ra màn hình.

> Gợi ý: Sử dụng hàm `print()` để hiển thị kết quả.
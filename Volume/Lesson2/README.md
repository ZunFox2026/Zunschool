# Bài 2: Cấu trúc rẽ nhánh – if, elif, else

## 🎯 Mục tiêu
- Hiểu và sử dụng câu lệnh điều kiện `if`, `elif`, `else`.
- So sánh các giá trị với toán tử quan hệ (`==`, `!=`, `<`, `>`, `<=`, `>=`).
- Kết hợp nhiều điều kiện với `and`, `or`, `not`.
- Viết chương trình có rẽ nhánh theo logic.

## 📖 Lý thuyết

### 1. Câu lệnh if cơ bản
```python
if điều_kiện:
    # khối lệnh thực hiện nếu điều_kiện đúng
2. if – else

```python
if điều_kiện:
    # đúng
else:
    # sai
```

3. if – elif – else

```python
if điều_kiện_1:
    ...
elif điều_kiện_2:
    ...
else:
    ...
```

4. Toán tử so sánh

Toán tử Ý nghĩa
== bằng
!= khác
< nhỏ hơn
> lớn hơn
<= nhỏ hơn hoặc bằng
>= lớn hơn hoặc bằng

5. Toán tử logic

· and: cả hai đều đúng
· or: ít nhất một đúng
· not: phủ định

🧪 Ví dụ mẫu

Xem file Lesson2.py.

📝 Bài tập

1. Nhập một số, kiểm tra số đó là chẵn hay lẻ.
2. Nhập điểm, in ra xếp loại (A: >=8.5, B: 7-8.4, C: 5.5-6.9, D: <5.5).
3. Nhập năm, kiểm tra năm nhuận (chia hết cho 4, không chia hết cho 100, hoặc chia hết cho 400).
4. Nhập 3 số, tìm số lớn nhất.
5. Viết máy tính đơn giản (+, -, *, /) dùng if-elif.

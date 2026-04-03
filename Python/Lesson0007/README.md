# Bài 7: Luyện Tập Cơ Bản Về Cấu Trúc Điều Khiển Và Vòng Lặp Trong Python

## Giới thiệu

Bài 7 giúp người học củng cố kiến thức cơ bản về các cấu trúc điều khiển và vòng lặp trong Python – nền tảng quan trọng để viết chương trình có logic rẽ nhánh và lặp lại hành động. Sau bài học này, bạn sẽ hiểu và vận dụng được câu lệnh điều kiện `if`, `elif`, `else` cùng các vòng lặp `for` và `while` để giải quyết các bài toán đơn giản.

## Lý thuyết

Python hỗ trợ ba cấu trúc điều khiển chính:
- **Câu lệnh điều kiện**: Dùng để thực hiện các khối lệnh dựa trên điều kiện đúng/sai.
  - Cú pháp: `if`, `elif`, `else`
- **Vòng lặp for**: Lặp qua một dãy (list, string, range,...)
  - Cú pháp: `for i in range(n):`
- **Vòng lặp while**: Lặp khi điều kiện còn đúng
  - Cú pháp: `while điều_kiện:`

Các toán tử so sánh như `==`, `!=`, `<`, `>` và toán tử logic `and`, `or`, `not` thường được dùng trong điều kiện.

## Ví dụ

Dưới đây là ví dụ sử dụng cả điều kiện và vòng lặp:

```python
# In các số từ 1 đến 10, nếu chia hết cho 3 thì in thông báo
for i in range(1, 11):
    if i % 3 == 0:
        print(f"{i} chia hết cho 3")
    else:
        print(i)
```

**Kết quả:**
```
1
2
3 chia hết cho 3
4
5
6 chia hết cho 3
...
```

## Bài tập

1. Viết chương trình kiểm tra một số nhập từ bàn phím là chẵn hay lẻ.
2. Dùng vòng lặp `for` in ra các số lẻ từ 1 đến 20.
3. Dùng vòng lặp `while` để tính tổng các số từ 1 đến n (người dùng nhập n).
4. Viết chương trình in "Hello, Python!" 5 lần bằng cả `for` và `while`.

> Gợi ý: Sử dụng `input()` để nhận dữ liệu, `int()` để chuyển đổi kiểu số, và kiểm tra điều kiện bằng `if-else`.
# Bài 8: Python Cơ bản  

## Giới thiệu  

Bài 8 thuộc khóa học “Python Cơ bản” dành cho người mới bắt đầu. Mục tiêu của bài này là giúp sinh viên nắm vững cú pháp cơ bản của Python, biết cách khai báo biến, sử dụng các kiểu dữ liệu nguyên thủy (số, chuỗi, boolean), thực hiện các phép toán và điều khiển luồng chương trình bằng cấu trúc `if…else` và vòng lặp `for`, `while`. Khi hoàn thành bài này, học viên sẽ có thể viết các chương trình đơn giản để giải quyết các bài toán thực tế như tính tổng dãy số, kiểm tra số nguyên tố, hoặc xử lý chuỗi ký tự.  

## Lý thuyết  

1. **Cú pháp và indent**  
   - Python dùng khoảng trắng (thường là 4 space) để xác định khối mã. Không dùng dấu ngoặc nhọn `{}` như C/Java.  
   - Mỗi lệnh kết thúc bằng dấu xuống dòng; không cần dấu chấm phẩy (`;`) trừ khi muốn đặt nhiều lệnh trên cùng một dòng.  

2. **Biến và kiểu dữ liệu**  
   - Khai báo biến không cần chỉ định kiểu: `x = 10`, `name = "An"`.  
   - Các kiểu nguyên thủy phổ biến: `int`, `float`, `str`, `bool`.  
   - Ép kiểu: `int("5")`, `float(3)`, `str(2025)`.  

3. **Toán tử**  
   - Toán số học: `+ - * / // % **`.  
   - Toán so sánh: `== != > < >= <=`.  
   - Toán logic: `and or not`.  

4. **Cấu trúc điều khiển**  
   - `if … elif … else:` – thực hiện nhánh dựa trên điều kiện boolean.  
   - Vòng lặp `for` với `range(start, stop, step)` hoặc lặp qua iterable (list, string).  
   - Vòng lặp `while` – lặp finché điều kiện còn đúng.  
   - Các từ khóa `break`, `continue`, `pass` để điều khiển luồng trong vòng lặp.  

5. **Hàm (function)**  
   - Định hàm bằng `def ten_ham([tham_số]):`.  
   - Trả về giá trị bằng `return`. Hàm không có `return` sẽ trả về `None`.  

## Ví dụ  

```python
# Ví dụ 1: Tính tổng các số từ 1 đến n
def tong_den_n(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i
    return tong

print(tong_den_n(10))   # Kết quả: 55

# Ví dụ 2: Kiểm tra số nguyên tố
def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for num in range(1, 21):
    if la_so_nguyen_to(num):
        print(num, end=" ")   # 2 3 5 7 11 13 17 19
```

## Bài tập  

1. **Tính giai thừa** – Viết hàm `giai_thua(n)` trả về `n!` (giai thừa của n). Yêu cầu xử lý trường hợp `n = 0` trả về `1`.  
2. **Đảo ngược chuỗi** – Nhập một chuỗi từ bàn phím, in ra chuỗi đã đảo ngược mà không dùng slicing `[::-1]`.  
3. **Số Fibonacci** – In ra 20 số đầu tiên của dãy Fibonacci (0, 1, 1, 2, 3, 5, …).  
4. ** Đếm ký tự** – Cho một chuỗi, đếm số lượng chữ hoa,,
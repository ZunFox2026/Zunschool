# README – Bài 3 (Cấp Cơ bản)  
**Chủ đề:** Sử dụng vòng lặp `for`, hàm và xử lý danh sách trong Python  

---  

## Giới thiệu  

Bài tập này nhằm giúp bạn làm quen với cách duyệt qua các phần tử của một danh sách (list), áp dụng logic điều kiện bên trong vòng lặp và đóng gói mã thành hàm để tái sử dụng. Khi hoàn thành bài, bạn sẽ biết:

* Tạo và truy cập danh sách trong Python.  
* Dùng vòng lặp `for` để lặp qua từng phần tử.  
* Kết hợp câu lệnh `if` để lọc hoặc biến đổi dữ liệu.  
* Định nghĩa hàm (`def`) và trả về kết quả bằng `return`.  
* Gọi hàm và in kết quả ra màn hình.  

Các kỹ năng này là nền tảng cho hầu hết các bài toán xử lý dữ liệu trong Python, từ phân tích số liệu đơn giản đến các ứng dụng web và khoa học dữ liệu.  

---  

## Lý thuyết  

### 1. Danh sách (list)  
Danh sách là một cấu trúc dữ liệu có thứ tự, cho phép lưu trữ nhiều giá trị khác nhau trong một biến. Cú pháp khai báo:  

```python
danh_sach = [1, 2, 3, 'a', 'b']
```

Các phần tử được truy cập bằng chỉ số bắt đầu từ `0`: `danh_sach[0]` → `1`.  

### 2. Vòng lặp `for`  
Vòng lặp `for` duyệt qua từng phần tử của một iterable (list, tuple, range, …). Cú pháp cơ bản:  

```python
for bien in iterable:
    # thân vòng lặp
```

### 3. Câu lệnh điều kiện `if`  
Cho phép thực hiện một khối mã chỉ khi điều kiện nhất định đúng.  

```python
if bien % 2 == 0:   # kiểm tra số chẵn
    print(bien, "là số chẵn")
```

### 4. Hàm (`def`)  
Hàm giúp đóng gói một đoạn mã có thể tái sử dụng. Cú pháp:  

```python
def ten_ham(tham_số_1, tham_số_2):
    # thân hàm
    return giá_trị_trả_về
```

Khi gọi hàm, chúng ta truyền các đối số và nhận kết quả từ `return`.  

---  

## Ví dụ  

**Yêu cầu:** Viết hàm `tong_so_chan(ds)` trả về tổng tất cả các số chẵn trong danh sách `ds`.  

```python
def tong_so_chan(ds):
    """
    Tính tổng các số chẵn trong danh sách ds.
    Tham số:
        ds (list): danh sách chứa các số nguyên.
    Trả về:
        int: tổng của các số chẵn.
    """
    tong = 0                     # khởi tạo biến tích lũy
    for so in ds:                # duyệt từng phần tử
        if isinstance(so, int) and so % 2 == 0:  # kiểm tra là int và chẵn
            tong += so           # cộng vào tổng
    return tong

# Minh họa sử dụng
mau = [1, 4, 7, 10, 13, 16, 'hello', 22]
print("Tổng số chẵn:", tong_so_chan(mau))   # Output: 52
```

**Giải thích:**
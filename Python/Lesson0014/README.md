# README – Bài 14: Lập trình hàm (Cấp cơ bản)

## Giới thiệu
Trong quá trình học Python, hàm là một trong những khái niệm nền tảng giúp chúng ta **tái sử dụng mã**, **giảm lặp lại** và **làm cho chương trình dễ đọc, bảo trì hơn**. Bài 14 tập trung vào cách khai báo, gọi hàm, truyền tham số và trả về kết quả. Sau khi hoàn thành bài này, bạn sẽ biết:

- Cách định nghĩa hàm bằng từ khóa `def`.
- Sự khác biệt giữa tham số chính thức và tham số thực.
- Nguyên tắc phạm vi biến (local vs global).
- Cách trả về nhiều giá trị bằng tuple.
- Một số mẹo tốt nhất khi viết hàm (tên hàm mô tả, docstring, không side‑effect không cần thiết).

## Lý thuyết
### 1. Khai báo hàm
```python
def tên_hàm(tham_số_1, tham_số_2=None):
    """Mô tả ngắn gọn về việc hàm làm gì."""
    # thân hàm
    return giá_trị
```
- `def` bắt đầu khai báo.
- Tên hàm nên viết hoa đầu từ (snake_case) và mô tả hành động.
- Tham số có thể có giá trị mặc định (`None`, `0`, `[]` …).  
- Docstring (chuỗi triple quotes) đặt ngay sau dòng `def` để tạo tài liệu tự động.

### 2. Truyền tham số
- **Theo vị trí**: `tính_tổng(3, 5)`  
- **Theo tên**: `tính_tổng(b=5, a=3)` – giúp代码更易读。  
- **Tham số mặc định**: nếu không cung cấp, Python sẽ dùng giá trị đã khai báo.

### 3. Phạm vi biến
- Biến được định nghĩa **bên trong hàm** là *local* – chỉ可见 trong hàm đó.  
- Biến **toàn cục** (được khai báo ngoài hàm) có thể đọc bên trong, nhưng nếu muốn thay đổi phải dùng từ khóa `global`.

### 4. Trả về nhiều giá trị
Python cho phép trả về một tuple mà không cần dấu ngoặc đơn:
```python
def min_max(values):
    return min(values), max(values)   # trả về (min, max)
```
Khi gọi: `a, b = min_max([4, 7, 2])`.

## Ví dụ
Dưới đây là một hàm tính **giải thừa** của một số nguyên không âm, kèm xử lý lỗi đơn giản:

```python
def giai_thua(n: int) -> int:
    """
    Tính n! (giai thừa) bằng phương pháp lặp.
    Nếu n < 0 sẽ raises ValueError.
    """
    if n < 0:
        raise ValueError("n phải là số nguyên không âm")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Sử dụng hàm
if __name__ == "__main__":
ause
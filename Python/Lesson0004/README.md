# README – Bài 4: Python Cơ bản  

---

## Giới thiệu  

Bài 4 thuộc khóa học **Python Cơ bản** và là bước quan trọng giúp người học nắm vững các khái niệm nền tảng: biến, kiểu dữ liệu, toán tử, cấu trúc điều khiển và hàm. Sau khi hoàn thành bài này, bạn sẽ có thể:

- Khai báo và sử dụng các biến với các kiểu dữ liệu cơ bản (`int`, `float`, `str`, `bool`).  
- Áp dụng các toán tử số học, so sánh và logic để xây dựng biểu thức.  
- Viết các câu lệnh điều kiện (`if‑elif‑else`) và vòng lặp (`while`, `for`).  
- Định nghĩa hàm, truyền tham số và trả về kết quả.  

Bài viết được viết dưới dạng **Markdown** để dễ dàng lưu trữ trên GitHub, GitLab hoặc bất kỳ hệ thống quản lý tài liệu nào. Bạn có thể sao chép toàn bộ nội dung này vào một file tên `README.md` và mở bằng trình soạn thảo hỗ trợ Markdown (VS Code, Typora, …) để xem kết quả định dạng.

---

## Lý thuyết  

### 1. Biến và kiểu dữ liệu  
```python
# Khai báo biến
tuoi = 20                 # int
chieu_cao = 1.68          # float
ten = "Nguyễn Văn A"      # str
la_sinh_vien = True       # bool
```
- **Int** – số nguyên.  
- **Float** – số thực (dấu phẩy động).  
- **Str** – chuỗi ký tự, có thể dùng dấu `'` hoặc `"`.  
- **Bool** – giá trị logic `True` hoặc `False`.  

### 2. Toán tử  
| Nhóm | Ví dụ | Mô tả |
|------|-------|-------|
| Số học | `+ - * / // % **` | Cộng, trừ, nhân, chia, chia lấy phần nguyên, chia lấy dư, lũy thừa |
| So sánh | `== != > < >= <=` | Kiểm tra bằng, không bằng, lớn hơn, … |
| Logic | `and or not` | Kết hợp hoặc đảo ngược điều kiện |

### 3. Cấu trúc điều khiển  
- **If‑elif‑else**  
```python
if tuoi >= 18:
    print("Đã thành niên")
elif tuoi >= 13:
    print("Thiếu niên")
else:
    print("Trẻ em")
```
- **Vòng lặp while**  
```python
dem = 0
while dem < 5:
    print(dem)
    dem += 1
```
- **Vòng lặp for** (duyệt qua dãy hoặc iterable)  
```python
for i in range(1, 6):   # 1,2,3,4,5
    print(i)
```

### 4. Hàm  
```python
def binh_phuong(x):
    """Trả về bình phương của x"""
    return x * x

ket_qua = binh_phuong(4)   # ket_qua = 16
print(ket_qua)
```
- Định nghĩa bằng từ khóa `def`.  
- Docstring (chuỗi Triple quotes) mô tả chức năng hàm.  
- `return` gửi kết quả về phía gọi hàm; nếu không có `return`, hàm trả về `None`.  

---

## Ví dụ  

### Ví dụ 1: Tính chỉ số BMI  
```python
def tinh_bmi(can_nang, chieu_cao):
    """Tính chỉ số BMI từ cân nặng (kg) và chiều cao (m)"""
    return can_nang / (chieu_cao ** 2)

# Nhập dữ liệu từ người dùng
can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))

bmi = tinh_bmi(can_nang, chieu_cao)
print(f"Chỉ số BMI của bạn là: {bmi:.2f}
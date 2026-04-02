# README: Bài 5 – Python Cơ bản  

## Giới thiệu  
Bài học này là phần thứ năm của chuỗi “Python Cơ bản” dành cho người mới bắt đầu. Mục tiêu của bài là giúp các bạn nắm vững **cú pháp điều khiển luồng** (câu lệnh `if`, `elif`, `else` và các vòng lặp `for`, `while`) cũng như cách làm việc với **danh sách (list)** và **từ điển (dict)** – hai cấu trúc dữ liệu cơ bản nhất trong Python. Sau khi hoàn thành bài, bạn sẽ có thể viết các chương trình đơn giản để xử lý dữ liệu, thực hiện quyết định và lặp lại hành động một cách linh hoạt.

## Lý thuyết  

### 1. Câu lệnh điều kiện  
- `if`, `elif`, `else` cho phép chương trình thực hiện các khối mã khác nhau tùy thuộc vào giá trị boolean của biểu thức.  
- Cú pháp:  

```python
if điều_kiện_1:
    # khối mã khi điều_kiện_1 là True
elif điều_kiện_2:
    # khối mã khi điều_kiện_1 là False và điều_kiện_2 là True
else:
    # khối mã khi tất cả các điều trên đều False
```

- Lưu ý về **thụt lề** (indent): Python sử dụng khoảng trắng (thường là 4 spaces) để xác định khối mã.

### 2. Vòng lặp  
- **`for`**: lặp qua từng phần tử của một iterable (list, tuple, string, range…).  
- **`while`**: lặp finché điều kiện còn đúng.  

```python
# for
for i in range(5):          # 0,1,2,3,4
    print(i)

# while
count = 0
while count < 5:
    print(count)
    count += 1
```

- Từ khóa `break` và `continue` cho phép thoát sớm hoặc bỏ qua lần lặp hiện tại.

### 3. Danh sách (list)  
- Định danh bằng dấu `[ ]`, phần tử có thể thay đổi (mutable).  
- Các thao tác phổ biến: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `len()`, slicing (`list[start:stop:step]`).

### 4. Từ điển (dict)  
- Định dạng `{key: value}`; key phải là immutable (string, number, tuple).  
- Truy cập, thêm, sửa, xóa qua `dict[key]`. Các phương thức: `keys()`, `values()`, `items()`, `get()`, `pop()`.

## Ví dụ  

```python
# Ví dụ 1: Kiểm tra số chẵn/lẻ
def chan_le(n):
    if n % 2 == 0:
        return "Chẵn"
    else:
        return "Lẻ"

print(chan_le(7))   # Lẻ
print(chan_le(10))  # Chẵn


# Ví dụ 2: Tính tổng các số lẻ trong một list bằng for
numbers = [1, 4, 5, 8, 11, 14]
tong_le = 0
for x in numbers:
    if x % 2 != 0:      # nếu là số lẻ
        tong_le += x
print("Tổng số lẻ:", tong_le)   # 17


# Ví dụ 3: Đếm tần suất xuất hiện của từ trong một câu bằng dict
def dem_tu(cau):
    tu_list = cau.lower().split()
    freq = {}
    for tu in tu_list:
        freq[tu] = freq.get(tu, 0) + 1
    return freq

cau = "Python là ngôn ngữ lập trình Python rất mạnh"
print(dem_tu(cau))
# {'python': 2, 'là': 1, 'ngôn': 1, 'ngữ': 1, 'lập': 1, 'trình': 1, 'rất': 1, 'mạnh': 1}
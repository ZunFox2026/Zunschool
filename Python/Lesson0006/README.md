# Bài học 6: Tuple, Set và Dictionary trong Python

Chào mừng bạn đến với bài học số 6 trong khóa học Python cơ bản! Trong bài học này, chúng ta sẽ tìm hiểu về ba kiểu dữ liệu quan trọng trong Python: **Tuple**, **Set**, và **Dictionary**. Đây là những cấu trúc dữ liệu linh hoạt và được sử dụng rất phổ biến trong lập trình Python.

## Mục tiêu bài học

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Hiểu được đặc điểm và cách sử dụng của Tuple, Set và Dictionary.
- Khai báo, truy cập và thao tác với các phần tử trong Tuple, Set và Dictionary.
- Phân biệt được sự khác nhau giữa các kiểu dữ liệu này.
- Áp dụng các kiểu dữ liệu này vào các tình huống thực tế như lưu thông tin học sinh, xử lý danh sách từ, đếm tần suất xuất hiện, v.v.

## Nội dung lý thuyết

### 1. Tuple (Bộ)

- **Tuple** là một chuỗi các phần tử có thứ tự, **không thể thay đổi (immutable)** sau khi tạo.
- Dùng để lưu trữ các bộ dữ liệu cố định, ví dụ: tọa độ điểm, thông tin ngày tháng năm, thông tin cá nhân cơ bản.
- Khai báo bằng dấu ngoặc tròn `()`.

**Ví dụ:**
```python
coord = (10, 20)
student = ("Nguyễn Văn A", 18, "Lớp 12A")
```

### 2. Set (Tập hợp)

- **Set** là một tập hợp **không có thứ tự**, **không chứa phần tử trùng lặp**.
- Rất hữu ích để loại bỏ phần tử trùng, kiểm tra thành viên nhanh, hoặc thực hiện các phép toán tập hợp (hợp, giao, hiệu).
- Khai báo bằng dấu ngoặc nhọn `{}` hoặc dùng hàm `set()`.

**Ví dụ:**
```python
unique_numbers = {1, 2, 3, 4}
subjects = set(["Toán", "Lý", "Hóa", "Toán"])  # tự động loại bỏ trùng
```

### 3. Dictionary (Từ điển)

- **Dictionary** là cấu trúc dữ liệu lưu trữ theo cặp **khóa (key)** và **giá trị (value)**.
- Khóa phải là **duy nhất** và **không thay đổi được** (thường dùng string, số, tuple).
- Dùng để ánh xạ thông tin, ví dụ: từ điển Anh-Việt, thông tin học sinh theo mã số, đếm tần suất.
- Khai báo bằng dấu ngoặc nhọn `{}` với cấu trúc `key: value`.

**Ví dụ:**
```python
dict_student = {"tên": "Lan", "tuổi": 17, "lớp": "11B"}
word_count = {"xin": 2, "chào": 3}
```

## Ví dụ minh họa

Xem file `main.py` để chạy các ví dụ thực tế.

## Bài tập thực hành

Xem file `exercises.py` để làm bài tập.

## Lời giải

Lời giải cho bài tập có trong file `solutions.py`.

## Cách sử dụng

1. Chạy ví dụ minh họa:
   ```bash
   python main.py
   ```

2. Làm bài tập trong `exercises.py`.

3. Kiểm tra lời giải (nếu cần):
   ```bash
   python solutions.py
   ```

Chúc bạn học tốt và thành thạo các kiểu dữ liệu Tuple, Set và Dictionary!
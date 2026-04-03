# Bài học 7: Xử lý chuỗi và file trong Python

Chào mừng bạn đến với Bài học 7 trong khóa học Python cơ bản! Trong bài học này, chúng ta sẽ tìm hiểu cách làm việc với **chuỗi (string)** và **tệp tin (file)** — hai khái niệm cực kỳ quan trọng khi lập trình Python.

Bạn sẽ học cách xử lý dữ liệu văn bản, đọc/ghi file, và áp dụng vào các tình huống thực tế như lưu nhật ký, xử lý dữ liệu người dùng hay làm sạch dữ liệu.

---

## Mục tiêu bài học

Sau bài học này, bạn sẽ có thể:

- Hiểu và sử dụng các phương thức xử lý chuỗi phổ biến.
- Đọc và ghi file văn bản bằng Python.
- Xử lý lỗi khi làm việc với file.
- Áp dụng kiến thức vào các bài toán thực tế như đếm từ, lưu nhật ký, xử lý dữ liệu đơn giản.

---

## Lý thuyết chi tiết

### 1. Xử lý chuỗi (String)

Chuỗi là một dãy ký tự, được đặt trong dấu nháy đơn hoặc kép.

#### Một số phương thức chuỗi phổ biến:

- `len(s)` – trả về độ dài chuỗi.
- `s.upper()` – chuyển thành chữ in hoa.
- `s.lower()` – chuyển thành chữ thường.
- `s.strip()` – loại bỏ khoảng trắng đầu và cuối.
- `s.split(sep)` – tách chuỗi thành danh sách theo ký tự phân cách.
- `s.replace(old, new)` – thay thế chuỗi con.
- `s.find(sub)` – tìm vị trí chuỗi con (trả về -1 nếu không thấy).
- `''.join(list)` – nối các phần tử danh sách thành chuỗi.

**Ví dụ:**

```python
s = "  Xin chào Python!  "
s = s.strip().upper()  # Kết quả: "XIN CHÀO PYTHON!"
words = s.split()  # Kết quả: ['XIN', 'CHÀO', 'PYTHON!']
```

### 2. Làm việc với file

Python cung cấp lệnh `open()` để làm việc với file.

#### Các chế độ mở file phổ biến:

- `'r'`: đọc (mặc định)
- `'w'`: ghi (ghi đè)
- `'a'`: ghi tiếp (append)
- `'r+'`: đọc và ghi

**Cú pháp cơ bản:**

```python
with open('ten_file.txt', 'chế_độ') as f:
    nội_dung = f.read()  # hoặc f.write(), f.readlines(), ...
```

Dùng `with` giúp tự động đóng file sau khi sử dụng, tránh lỗi.

#### Các phương thức file:

- `f.read()`: đọc toàn bộ nội dung.
- `f.readline()`: đọc một dòng.
- `f.readlines()`: đọc tất cả dòng, trả về danh sách.
- `f.write(string)`: ghi chuỗi vào file.

---

## Ví dụ minh họa

### Ví dụ 1: Đếm số từ trong một file

Giả sử bạn có file `data.txt` chứa một đoạn văn, và bạn muốn đếm xem có bao nhiêu từ.

### Ví dụ 2: Ghi nhật ký (log)

Tạo một chương trình ghi lại thời gian người dùng chạy chương trình vào file `log.txt`.

### Ví dụ 3: Làm sạch dữ liệu

Đọc file chứa danh sách tên có khoảng trắng thừa, chuẩn hóa và ghi lại.

---

## Bài tập thực hành

1. Viết chương trình đếm số dòng trong một file văn bản.
2. Viết hàm tìm và thay thế từ trong một file.
3. Đọc file chứa danh sách email, lọc các email hợp lệ và lưu vào file mới.
4. Tạo file `profile.txt` và ghi thông tin cá nhân người dùng.
5. Viết chương trình nối hai file văn bản thành một file mới.

---

## Tổng kết

- Xử lý chuỗi là kỹ năng thiết yếu khi làm việc với dữ liệu văn bản.
- Python cung cấp nhiều phương thức tiện lợi để thao tác chuỗi.
- Làm việc với file cần cẩn thận: luôn dùng `with`, kiểm tra lỗi, chọn đúng chế độ mở.
- Kết hợp chuỗi và file giúp giải quyết nhiều bài toán thực tế như xử lý dữ liệu, lưu cấu hình, ghi log, v.v.

Hãy thực hành nhiều để thành thạo! Chúc bạn học tốt!
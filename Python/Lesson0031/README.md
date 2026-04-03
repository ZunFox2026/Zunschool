# Bài học Python số 31 - Cấp độ Trung cấp

## Chủ đề: Làm việc với File JSON trong Python

JSON (JavaScript Object Notation) là một định dạng dữ liệu nhẹ, dễ đọc và viết, được sử dụng phổ biến để trao đổi dữ liệu giữa các hệ thống (ví dụ: API, cấu hình, lưu trữ dữ liệu). Trong bài học này, bạn sẽ học cách đọc, ghi và xử lý dữ liệu JSON trong Python bằng module `json`.

### Mục tiêu bài học
- Hiểu được JSON là gì và ứng dụng của nó.
- Biết cách đọc và ghi file JSON bằng Python.
- Biết chuyển đổi giữa đối tượng Python và dữ liệu JSON.
- Áp dụng JSON để lưu trữ và truy xuất dữ liệu thực tế.

### Yêu cầu hệ thống
- Python 3.6 trở lên
- Không cần cài thêm thư viện

### Hướng dẫn sử dụng
1. Chạy file `main.py` để xem các ví dụ minh họa.
2. Làm các bài tập trong file `exercises.py`.
3. Kiểm tra lời giải (nếu cần) trong file `solutions.py`.

### Cấu trúc thư mục
```
lesson31/
│
├── main.py         # Các ví dụ minh họa
├── exercises.py    # Bài tập thực hành
├── solutions.py    # Lời giải bài tập
└── README.md       # Tài liệu hướng dẫn
```

---

## Nội dung chi tiết

### 1. Module `json` trong Python

Python cung cấp module `json` để làm việc với dữ liệu JSON. Các hàm chính:

- `json.dumps(obj)`: Chuyển đối tượng Python thành chuỗi JSON.
- `json.loads(json_string)`: Chuyển chuỗi JSON thành đối tượng Python.
- `json.dump(obj, file)`: Ghi đối tượng Python vào file dưới dạng JSON.
- `json.load(file)`: Đọc dữ liệu JSON từ file và trả về đối tượng Python.

### 2. Kiểu dữ liệu tương ứng

| Python        | JSON          |
|---------------|---------------|
| dict          | object        |
| list, tuple   | array         |
| str           | string        |
| int, float    | number        |
| True          | true          |
| False         | false         |
| None          | null          |

### 3. Ví dụ minh họa

Xem file `main.py` để thấy cách sử dụng trong thực tế.

### 4. Bài tập

Hãy hoàn thành các bài tập trong `exercises.py` để củng cố kiến thức.

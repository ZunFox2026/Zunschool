# Bài 23: Cấp Cơ Bản – Làm Việc Với File trong Python

## Giới thiệu

Trong lập trình Python, việc đọc và ghi dữ liệu vào file là một kỹ năng cơ bản và thiết yếu. Bài học này sẽ giúp bạn hiểu cách làm việc với các file văn bản (text file) trong Python, từ việc mở, đọc, ghi đến đóng file một cách an toàn. Đây là nền tảng quan trọng để xử lý dữ liệu từ bên ngoài chương trình, như đọc cấu hình, lưu nhật ký hoặc làm việc với dữ liệu người dùng.

## Lý thuyết

Python cung cấp hàm `open()` để làm việc với file. Cú pháp cơ bản:

```python
file = open(tên_file, chế_độ)
```

Các chế độ phổ biến:
- `'r'`: Đọc file (mặc định)
- `'w'`: Ghi file (ghi đè nếu file đã tồn tại)
- `'a'`: Ghi thêm vào cuối file
- `'r+'`: Đọc và ghi

Sau khi sử dụng file, nên đóng bằng `file.close()` để giải phóng tài nguyên. Tuy nhiên, tốt nhất nên dùng khối `with` để tự động đóng file.

## Ví dụ

Dưới đây là ví dụ về cách ghi và đọc dữ liệu từ file:

```python
# Ghi dữ liệu vào file
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Xin chào từ Python!\n")
    f.write("Đây là dòng thứ hai.")

# Đọc dữ liệu từ file
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

Kết quả in ra:
```
Xin chào từ Python!
Đây là dòng thứ hai.
```

## Bài tập

1. Tạo một chương trình ghi tên và tuổi của bạn vào file `thongtin.txt`.
2. Viết tiếp một dòng mới vào file đó với thông tin sở thích của bạn (dùng chế độ `'a'`).
3. Đọc và in toàn bộ nội dung file ra màn hình.
4. (Nâng cao) Đọc từng dòng trong file và in ra với số thứ tự dòng.

> Gợi ý: Dùng `readline()` hoặc vòng lặp `for` để duyệt từng dòng.
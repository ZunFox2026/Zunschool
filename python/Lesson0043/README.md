# Làm việc với File CSV
## Giới thiệu
File CSV (Comma Separated Values) là một loại file văn bản thường được sử dụng để lưu trữ dữ liệu dưới dạng bảng. Mỗi hàng trong file CSV đại diện cho một bản ghi, và các trường trong bản ghi được ngăn cách bởi dấu phẩy. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với file CSV bằng ngôn ngữ lập trình Python.

## Lý thuyết
Để làm việc với file CSV, Python cung cấp một mô-đun có tên là `csv`. Mô-đun này cho phép bạn đọc và ghi file CSV một cách dễ dàng. Có hai cách chính để làm việc với file CSV: đọc và ghi. 
- Đọc file CSV: Sử dụng hàm `reader()` từ mô-đun `csv` để đọc file CSV. Hàm này trả về một đối tượng reader, cho phép bạn đọc từng hàng trong file CSV.
- Ghi file CSV: Sử dụng hàm `writer()` từ mô-đun `csv` để ghi file CSV. Hàm này trả về một đối tượng writer, cho phép bạn ghi từng hàng vào file CSV.

## Ví dụ
Dưới đây là một ví dụ về cách đọc và ghi file CSV bằng Python:
```python
import csv

# Đọc file CSV
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Ghi file CSV
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tên', 'Tuổi', 'Địa chỉ'])
    writer.writerow(['Nguyễn Văn A', 25, 'Hà Nội'])
    writer.writerow(['Trần Thị B', 30, 'TP.HCM'])
```
Trong ví dụ trên, chúng ta đọc file CSV có tên `example.csv` và in ra từng hàng. Sau đó, chúng ta ghi một số dữ liệu vào file CSV có cùng tên.

## Bài tập
Bài tập cho bạn:
- Tạo một file CSV có tên `sinh_vien.csv` với các trường `MSSV`, `Tên`, `Tuổi`, `Địa chỉ`.
- Đọc file CSV và in ra danh sách sinh viên.
- Thêm một số bản ghi mới vào file CSV.
- Đọc lại file CSV và in ra danh sách sinh viên đã được cập nhật.
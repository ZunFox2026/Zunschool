# Làm việc với file CSV
## Giới thiệu
File CSV (Comma Separated Values) là một loại file văn bản được sử dụng để lưu trữ dữ liệu bảng. Mỗi hàng trong file CSV đại diện cho một bản ghi, và các trường trong bản ghi được ngăn cách bởi dấu phẩy. File CSV được sử dụng rộng rãi trong nhiều lĩnh vực, bao gồm kinh doanh, tài chính, và khoa học dữ liệu. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với file CSV bằng ngôn ngữ lập trình Python.

## Lý thuyết
Để làm việc với file CSV trong Python, chúng ta có thể sử dụng module `csv`. Module này cung cấp các hàm và lớp để đọc và viết file CSV. Có hai cách chính để làm việc với file CSV: đọc và viết.

*   Đọc file CSV: Chúng ta có thể sử dụng hàm `reader()` từ module `csv` để đọc file CSV. Hàm này trả về một đối tượng reader, cho phép chúng ta đọc từng hàng trong file CSV.
*   Viết file CSV: Chúng ta có thể sử dụng hàm `writer()` từ module `csv` để viết file CSV. Hàm này trả về một đối tượng writer, cho phép chúng ta viết từng hàng vào file CSV.

## Ví dụ
Dưới đây là một số ví dụ về cách làm việc với file CSV:

*   Đọc file CSV:

    ```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

    Ví dụ trên sẽ đọc file `data.csv` và in ra từng hàng trong file.

*   Viết file CSV:

    ```python
import csv

data = [['Tên', 'Tuổi'], ['John', 25], ['Alice', 30]]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

    Ví dụ trên sẽ viết dữ liệu vào file `data.csv`.

## Bài tập
Bài tập dưới đây sẽ giúp bạn thực hành làm việc với file CSV:

*   Tạo một file CSV có tên `sinh_vien.csv` với các trường `MSSV`, `Tên`, `Tuổi`.
*   Đọc file `sinh_vien.csv` và in ra từng hàng trong file.
*   Thêm một bản ghi mới vào file `sinh_vien.csv`.
*   Đọc file `sinh_vien.csv` và tìm bản ghi có `MSSV` là `12345`.
*   Xóa bản ghi có `MSSV` là `12345` trong file `sinh_vien.csv`.

Bài tập này sẽ giúp bạn nắm vững cách làm việc với file CSV trong Python. Hãy thử thực hành và tìm hiểu thêm về module `csv` để có thể làm việc hiệu quả với file CSV.
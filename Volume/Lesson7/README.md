# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với tệp tin trong Python.

## Lý thuyết
Để làm việc với tệp tin trong Python, bạn cần sử dụng hàm `open()` để mở tệp tin. Hàm `open()` trả về một đối tượng tệp tin, cho phép bạn đọc và viết dữ liệu vào tệp tin. Có nhiều chế độ mở tệp tin khác nhau, bao gồm:
- `r`: Mở tệp tin để đọc (read)
- `w`: Mở tệp tin để viết (write)
- `a`: Mở tệp tin để thêm (append)
- `r+`: Mở tệp tin để đọc và viết
- `w+`: Mở tệp tin để đọc và viết, xóa nội dung cũ

Khi mở tệp tin, bạn cần chỉ định đường dẫn đến tệp tin và chế độ mở. Ví dụ:
```python
f = open('ten_tep.txt', 'r')
```
Sau khi mở tệp tin, bạn có thể đọc hoặc viết dữ liệu vào tệp tin bằng cách sử dụng các phương thức như `read()`, `write()`, `close()`. Ví dụ:
```python
f = open('ten_tep.txt', 'w')
f.write('Xin chào, thế giới!')
f.close()
```
## Ví dụ
Dưới đây là một ví dụ về cách đọc và viết dữ liệu vào tệp tin:
```python
# Mở tệp tin để viết
f = open('ten_tep.txt', 'w')
f.write('Xin chào, thế giới!')
f.close()

# Mở tệp tin để đọc
f = open('ten_tep.txt', 'r')
noi_dung = f.read()
print(noi_dung)
f.close()
```
Kết quả sẽ là:
```
Xin chào, thế giới!
```
## Bài tập
Bài tập 1: Viết một chương trình để đọc nội dung của tệp tin `ten_tep.txt` và in ra màn hình.
Bài tập 2: Viết một chương trình để viết nội dung của biến `noi_dung` vào tệp tin `ten_tep.txt`.
Bài tập 3: Viết một chương trình để thêm nội dung của biến `them_noi_dung` vào cuối tệp tin `ten_tep.txt`.

Hy vọng những thông tin trên sẽ giúp bạn hiểu rõ hơn về cách làm việc với tệp tin trong Python. Hãy thử thực hành các bài tập trên để nắm vững kiến thức!
# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một trong những kỹ năng quan trọng khi lập trình. Trong Python, việc đọc và ghi tệp tin được thực hiện thông qua các hàm và phương thức đặc biệt. Bài viết này sẽ giới thiệu về cách làm việc với tệp tin trong Python, bao gồm cả lý thuyết và ví dụ minh họa.

## Lý thuyết
Để làm việc với tệp tin trong Python, bạn cần sử dụng hàm `open()` để mở tệp tin. Hàm này trả về một đối tượng tệp tin, cho phép bạn đọc và ghi dữ liệu vào tệp tin. Có hai chế độ mở tệp tin chính: `r` (đọc) và `w` (ghi). Ngoài ra, bạn cũng có thể sử dụng các chế độ khác như `a` (thêm vào cuối tệp tin), `x` (tạo tệp tin mới) và `b` (đọc/ghi tệp tin nhị phân).

Khi mở tệp tin, bạn cần chỉ định đường dẫn và tên tệp tin. Nếu tệp tin không tồn tại, Python sẽ tự động tạo tệp tin mới nếu bạn sử dụng chế độ `w` hoặc `x`. Nếu tệp tin đã tồn tại, Python sẽ ghi đè lên tệp tin nếu bạn sử dụng chế độ `w`.

Để đọc dữ liệu từ tệp tin, bạn có thể sử dụng phương thức `read()`. Phương thức này trả về một chuỗi chứa dữ liệu trong tệp tin. Để ghi dữ liệu vào tệp tin, bạn có thể sử dụng phương thức `write()`.

## Ví dụ
Ví dụ sau minh họa cách mở, đọc và ghi tệp tin trong Python:
```python
# Mở tệp tin và ghi dữ liệu
f = open("test.txt", "w")
f.write("Xin chào, thế giới!")
f.close()

# Mở tệp tin và đọc dữ liệu
f = open("test.txt", "r")
print(f.read())
f.close()
```
Kết quả của ví dụ trên sẽ là:
```
Xin chào, thế giới!
```
## Bài tập
Bài tập dưới đây yêu cầu bạn thực hiện các thao tác sau:

* Tạo một tệp tin mới tên là `hello.txt` và ghi vào đó chuỗi "Xin chào, thế giới!".
* Đọc dữ liệu từ tệp tin `hello.txt` và in ra màn hình.
* Thêm vào cuối tệp tin `hello.txt` chuỗi "Đây là một dòng mới.".
* Đọc lại dữ liệu từ tệp tin `hello.txt` và in ra màn hình.

Hãy tự thực hiện bài tập trên và chạy chương trình để xem kết quả!
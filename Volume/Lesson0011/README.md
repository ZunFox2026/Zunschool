# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một phần quan trọng trong lập trình. Trong bài học này, chúng ta sẽ tìm hiểu cách đọc, ghi và xử lý tệp tin trong Python. Đây là một kỹ năng cơ bản nhưng rất quan trọng, vì nó cho phép chúng ta lưu trữ và đọc dữ liệu từ tệp tin, giúp cho chương trình của chúng ta trở nên linh hoạt và hữu dụng hơn.

## Lý thuyết
Trong Python, chúng ta có thể làm việc với tệp tin bằng cách sử dụng hàm `open()`. Hàm này trả về một đối tượng tệp tin, cho phép chúng ta đọc, ghi hoặc thực hiện các hoạt động khác trên tệp tin. Có hai chế độ mở tệp tin chính: `r` (read) để đọc và `w` (write) để ghi. Ngoài ra, chúng ta cũng có thể sử dụng `a` (append) để thêm nội dung vào cuối tệp tin.

Khi làm việc với tệp tin, chúng ta cần phải đóng tệp tin sau khi sử dụng xong bằng cách gọi phương thức `close()`. Tuy nhiên, để tránh việc quên đóng tệp tin, chúng ta có thể sử dụng câu lệnh `with`, nó sẽ tự động đóng tệp tin khi chúng ta kết thúc làm việc với nó.

## Ví dụ
Ví dụ về cách đọc và ghi tệp tin:
```python
# Mở tệp tin và đọc nội dung
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Mở tệp tin và ghi nội dung
with open('example.txt', 'w') as file:
    file.write('Xin chào, thế giới!')
```
Ví dụ trên minh họa cách đọc và ghi nội dung vào một tệp tin có tên là `example.txt`.

## Bài tập
Bài tập 1: Tạo một tệp tin có tên là `hello.txt` và ghi nội dung "Xin chào, Python!" vào đó.

Bài tập 2: Đọc nội dung của tệp tin `hello.txt` và in ra màn hình.

Bài tập 3: Thêm nội dung "Làm việc với tệp tin là rất thú vị!" vào cuối tệp tin `hello.txt`.

Bài tập 4: Tạo một chương trình cho phép người dùng nhập nội dung và lưu vào một tệp tin có tên do người dùng chỉ định.

Những bài tập trên sẽ giúp bạn nắm vững cách làm việc với tệp tin trong Python và có thể áp dụng vào các dự án thực tế. Hãy thử nghiệm và khám phá thêm về các tính năng của Python khi làm việc với tệp tin!
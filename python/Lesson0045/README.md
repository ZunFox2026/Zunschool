# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin trên hệ thống. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp tin trong Python, bao gồm cả việc đọc và viết tệp tin.

## Lý thuyết
Trong Python, bạn có thể làm việc với tệp tin bằng cách sử dụng hàm `open()`. Hàm này trả về một đối tượng tệp tin, cho phép bạn đọc và viết dữ liệu vào tệp tin. Có ba chế độ mở tệp tin chính:
- `r`: Mở tệp tin để đọc.
- `w`: Mở tệp tin để viết. Nếu tệp tin đã tồn tại, nội dung sẽ bị xóa.
- `a`: Mở tệp tin để thêm nội dung vào cuối tệp tin.
Bạn cũng có thể sử dụng các chế độ khác như `r+`, `w+`, `a+` để vừa đọc vừa viết tệp tin.

## Ví dụ
Dưới đây là một số ví dụ về cách làm việc với tệp tin trong Python:
```python
# Mở tệp tin để đọc
f = open('test.txt', 'r')
print(f.read())
f.close()

# Mở tệp tin để viết
f = open('test.txt', 'w')
f.write('Hello, World!')
f.close()

# Mở tệp tin để thêm nội dung vào cuối tệp tin
f = open('test.txt', 'a')
f.write(' Đây là nội dung thêm vào.')
f.close()
```
Lưu ý rằng sau khi làm việc với tệp tin, bạn nên đóng tệp tin lại bằng cách gọi phương thức `close()` để giải phóng tài nguyên hệ thống.

## Bài tập
Bài tập này yêu cầu bạn thực hiện các nhiệm vụ sau:
- Tạo một tệp tin mới có tên là `my_file.txt`.
- Viết nội dung "Xin chào, thế giới!" vào tệp tin này.
- Đọc nội dung của tệp tin và in ra màn hình.
- Thêm nội dung "Đây là nội dung thêm vào." vào cuối tệp tin.
- Đóng tệp tin lại sau khi làm việc xong.

Hãy thực hiện các bước trên và chạy chương trình để xem kết quả. Đây là một ví dụ cơ bản về cách làm việc với tệp tin trong Python. Bạn có thể mở rộng và áp dụng kiến thức này vào các dự án thực tế.
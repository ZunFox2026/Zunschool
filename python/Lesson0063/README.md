# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp tin trong Python, bao gồm cả việc đọc và viết tệp tin.

## Lý thuyết
Trong Python, bạn có thể làm việc với tệp tin bằng cách sử dụng hàm `open()`. Hàm này sẽ trả về một đối tượng tệp tin, cho phép bạn thực hiện các hoạt động như đọc và viết tệp tin. Có hai chế độ chính khi làm việc với tệp tin: chế độ đọc (`'r'`) và chế độ viết (`'w'`). Khi bạn mở một tệp tin ở chế độ đọc, bạn có thể đọc nội dung của tệp tin đó. Ngược lại, khi bạn mở một tệp tin ở chế độ viết, bạn có thể viết nội dung vào tệp tin đó. Nếu tệp tin chưa tồn tại, Python sẽ tự động tạo một tệp tin mới.

Ngoài ra, bạn cũng có thể sử dụng chế độ đọc và viết cùng lúc (`'r+'` hoặc `'w+'`), hoặc chế độ附 thêm (`'a'`) để thêm nội dung vào cuối tệp tin.

## Ví dụ
Dưới đây là một số ví dụ về cách làm việc với tệp tin trong Python:
```python
# Mở tệp tin và đọc nội dung
f = open('example.txt', 'r')
content = f.read()
print(content)
f.close()

# Mở tệp tin và viết nội dung
f = open('example.txt', 'w')
f.write('Xin chào, thế giới!')
f.close()

# Mở tệp tin và thêm nội dung
f = open('example.txt', 'a')
f.write('\nTôi là Zunny, trợ giảng Python.')
f.close()
```
 Trong ví dụ trên, chúng ta đã mở tệp tin `example.txt` ở chế độ đọc, đọc nội dung, và in ra màn hình. Sau đó, chúng ta đã mở tệp tin đó ở chế độ viết, viết nội dung vào tệp tin. Cuối cùng, chúng ta đã mở tệp tin đó ở chế độ附 thêm, và thêm nội dung vào cuối tệp tin.

## Bài tập
Bài tập cho bạn:
- Tạo một tệp tin mới có tên `hello.txt`.
- Viết nội dung `Xin chào, thế giới!` vào tệp tin đó.
- Đọc nội dung của tệp tin đó và in ra màn hình.
- Thêm nội dung `Tôi là [Tên của bạn], trợ giảng Python.` vào cuối tệp tin.
- Đọc lại nội dung của tệp tin và in ra màn hình.

Hãy thử thực hiện các bước trên và xem kết quả!
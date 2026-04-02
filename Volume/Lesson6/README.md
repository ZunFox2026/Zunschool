# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin. Trong bài này, chúng ta sẽ tìm hiểu về các cách làm việc với tệp trong Python, bao gồm cả việc đọc và viết tệp.

## Lý thuyết
Trong Python, bạn có thể làm việc với tệp bằng cách sử dụng hàm `open()`. Hàm này trả về một đối tượng tệp, cho phép bạn thực hiện các hoạt động như đọc, viết, hoặc đóng tệp. Có nhiều chế độ mở tệp khác nhau, bao gồm:
- `r`: Mở tệp để đọc.
- `w`: Mở tệp để viết, nếu tệp đã tồn tại thì nội dung sẽ bị xóa.
- `a`: Mở tệp để thêm nội dung vào cuối tệp.
- `r+`: Mở tệp để đọc và viết.
- `x`: Tạo một tệp mới để viết, nếu tệp đã tồn tại thì sẽ trả về lỗi.

Khi bạn mở một tệp, bạn cần nhớ đóng nó lại khi không cần sử dụng nữa bằng cách sử dụng phương thức `close()`. Tuy nhiên, một cách tốt hơn là sử dụng câu lệnh `with`, nó sẽ tự động đóng tệp khi bạn xong việc.

## Ví dụ
Ví dụ sau đây sẽ minh họa cách mở một tệp, viết nội dung vào tệp, và sau đó đọc nội dung từ tệp:
```python
# Mở tệp và viết nội dung
with open('example.txt', 'w') as f:
    f.write('Xin chào, thế giới!\n')

# Mở tệp và đọc nội dung
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
```
Kết quả của ví dụ trên sẽ là nội dung `'Xin chào, thế giới!\n'` được in ra màn hình.

## Bài tập
Bài tập này yêu cầu bạn thực hiện các bước sau:
1. Tạo một tệp mới có tên `bai_tap.txt`.
2. Viết nội dung `'Tôi đang học Python.'` vào tệp `bai_tap.txt`.
3. Đọc nội dung từ tệp `bai_tap.txt` và in nó ra màn hình.
4. Thêm nội dung `'Tôi yêu lập trình.'` vào cuối tệp `bai_tap.txt`.
5. Đọc lại nội dung từ tệp `bai_tap.txt` và in nó ra màn hình.

Hãy thử thực hiện các bước trên và xem kết quả!
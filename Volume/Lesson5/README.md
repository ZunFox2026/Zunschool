# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một kỹ năng quan trọng trong lập trình. Trong bài này, chúng ta sẽ tìm hiểu về cách đọc và ghi tệp trong Python. Đây là một trong những kỹ năng cơ bản nhưng quan trọng để lưu trữ và xử lý dữ liệu.

## Lý thuyết
Python cung cấp nhiều cách để làm việc với tệp, bao gồm cả đọc và ghi. Để đọc một tệp, bạn cần sử dụng hàm `open()` với chế độ `'r'` (read). Để ghi một tệp, bạn cần sử dụng hàm `open()` với chế độ `'w'` (write) hoặc `'a'` (append). 

Chế độ `'w'` sẽ xóa nội dung cũ và ghi nội dung mới vào tệp, trong khi chế độ `'a'` sẽ thêm nội dung mới vào cuối tệp. 

Ngoài ra, bạn cũng cần đóng tệp sau khi sử dụng bằng hàm `close()` để tránh mất dữ liệu.

## Ví dụ
Dưới đây là ví dụ về cách đọc và ghi tệp:
```python
# Mở tệp và đọc nội dung
f = open('example.txt', 'r')
content = f.read()
print(content)
f.close()

# Mở tệp và ghi nội dung
f = open('example.txt', 'w')
f.write('Xin chào, thế giới!')
f.close()

# Mở tệp và thêm nội dung
f = open('example.txt', 'a')
f.write('\nThật tuyệt vời!')
f.close()
```
Trong ví dụ trên, chúng ta mở tệp `example.txt` ở chế độ đọc, đọc nội dung và in ra màn hình. Sau đó, chúng ta mở tệp ở chế độ ghi, xóa nội dung cũ và ghi nội dung mới vào tệp. Cuối cùng, chúng ta mở tệp ở chế độ thêm và thêm nội dung mới vào cuối tệp.

## Bài tập
Bài tập này yêu cầu bạn tạo một chương trình để quản lý danh sách sinh viên. Chương trình sẽ cho phép người dùng thêm, xóa và xem danh sách sinh viên. Dữ liệu sẽ được lưu trữ trong một tệp có tên `students.txt`. 

Yêu cầu:
- Tạo một hàm để thêm sinh viên vào danh sách.
- Tạo một hàm để xóa sinh viên khỏi danh sách.
- Tạo một hàm để xem danh sách sinh viên.
- Sử dụng hàm `open()` để đọc và ghi tệp.
- Sử dụng hàm `close()` để đóng tệp sau khi sử dụng.

Khi hoàn thành bài tập, bạn sẽ có một chương trình đơn giản để quản lý danh sách sinh viên và hiểu rõ hơn về cách làm việc với tệp trong Python.
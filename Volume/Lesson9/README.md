# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình. Tệp tin là nơi lưu trữ dữ liệu, và việc đọc, ghi, sửa đổi tệp tin là điều cần thiết trong nhiều ứng dụng. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với tệp tin trong Python.

## Lý thuyết
Trong Python, chúng ta có thể sử dụng hàm `open()` để mở một tệp tin. Hàm `open()` trả về một đối tượng tệp tin, mà chúng ta có thể sử dụng để đọc, ghi, sửa đổi tệp tin. Có ba chế độ mở tệp tin:
- `r`: Chế độ đọc (read). Đây là chế độ mặc định.
- `w`: Chế độ ghi (write). Nếu tệp tin đã tồn tại, nội dung của nó sẽ bị xóa.
- `a`: Chế độ附加 (append). Nếu tệp tin đã tồn tại, nội dung mới sẽ được thêm vào cuối tệp tin.
- `x`: Chế độ tạo mới (create). Nếu tệp tin đã tồn tại, việc mở tệp tin sẽ thất bại.

Chúng ta cũng có thể sử dụng các hàm như `read()`, `write()`, `close()` để đọc, ghi, đóng tệp tin.

## Ví dụ
Dưới đây là một số ví dụ về làm việc với tệp tin:
```python
# Mở tệp tin để đọc
f = open('example.txt', 'r')
content = f.read()
print(content)
f.close()

# Mở tệp tin để ghi
f = open('example.txt', 'w')
f.write('Đây là nội dung mới')
f.close()

# Mở tệp tin để附加
f = open('example.txt', 'a')
f.write(' Nội dung được thêm vào')
f.close()
```
## Bài tập
Bài tập này yêu cầu bạn tạo một chương trình Python để quản lý danh sách sinh viên. Chương trình sẽ lưu trữ danh sách sinh viên trong một tệp tin tên là `sinh_vien.txt`. Mỗi sinh viên sẽ được lưu trữ trong một dòng, với thông tin bao gồm tên, tuổi, và điểm trung bình.

Yêu cầu:
- Tạo một hàm để thêm sinh viên vào danh sách.
- Tạo một hàm để hiển thị danh sách sinh viên.
- Tạo một hàm để lưu trữ danh sách sinh viên vào tệp tin.
- Tạo một hàm để đọc danh sách sinh viên từ tệp tin.

Gợi ý: Sử dụng các hàm `open()`, `read()`, `write()`, `close()` để làm việc với tệp tin. Sử dụng các hàm `append()`, `insert()` để thêm sinh viên vào danh sách.
# Làm việc với Tệp
## Giới thiệu
Làm việc với tệp là một kỹ năng quan trọng trong lập trình. Trong bài này, chúng ta sẽ tìm hiểu về cách đọc và ghi tệp trong Python. Đây là một chủ đề cơ bản nhưng rất quan trọng, vì nó cho phép chúng ta lưu trữ và đọc dữ liệu từ tệp.

## Lý thuyết
Trong Python, chúng ta có thể làm việc với tệp bằng cách sử dụng функци (hàm) `open()`. Hàm này trả về một đối tượng tệp, mà chúng ta có thể sử dụng để đọc hoặc ghi dữ liệu. Có hai chế độ chính khi làm việc với tệp: đọc (`'r'`) và ghi (`'w'`). Nếu tệp không tồn tại, chế độ ghi sẽ tạo một tệp mới. Nếu tệp đã tồn tại, chế độ ghi sẽ xóa nội dung cũ và thay thế bằng nội dung mới.

Chúng ta cũng có thể sử dụng chế độ đọc và ghi đồng thời (`'r+'`), hoặc chế độ附加 (`'a'`), chế độ này sẽ thêm nội dung vào cuối tệp mà không xóa nội dung cũ.

## Ví dụ
Dưới đây là một số ví dụ về cách làm việc với tệp trong Python:
- Đọc tệp:
  ```python
  f = open('example.txt', 'r')
  content = f.read()
  print(content)
  f.close()
  ```
- Ghi tệp:
  ```python
  f = open('example.txt', 'w')
  f.write('Xin chào thế giới!')
  f.close()
  ```
- Ghi và đọc tệp:
  ```python
  f = open('example.txt', 'w')
  f.write('Xin chào thế giới!')
  f.close()

  f = open('example.txt', 'r')
  content = f.read()
  print(content)
  f.close()
  ```

## Bài tập
- Tạo một tệp văn bản mới có tên `hello.txt` và ghi vào đó dòng chữ "Xin chào thế giới!".
- Đọc nội dung của tệp `hello.txt` và in ra màn hình.
- Tạo một tệp mới có tên `number.txt` và ghi vào đó các số từ 1 đến 10, mỗi số trên một dòng.
- Đọc nội dung của tệp `number.txt` và in ra màn hình.
- Thêm các số từ 11 đến 15 vào cuối tệp `number.txt`.
- Đọc lại nội dung của tệp `number.txt` và in ra màn hình để kiểm tra.
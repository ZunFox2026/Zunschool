# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một phần quan trọng trong lập trình. Tệp tin là nơi lưu trữ dữ liệu, và việc đọc, viết, và xử lý tệp tin là một kỹ năng cần thiết cho bất kỳ lập trình viên nào. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp tin trong Python.

## Lý thuyết
Tệp tin có thể được chia thành hai loại: tệp tin văn bản và tệp tin nhị phân. Tệp tin văn bản chứa dữ liệu dưới dạng văn bản, trong khi tệp tin nhị phân chứa dữ liệu dưới dạng số nhị phân. Python cung cấp các hàm và phương thức để đọc và viết tệp tin, bao gồm `open()`, `read()`, `write()`, và `close()`. 

Để mở một tệp tin, chúng ta sử dụng hàm `open()`, với hai tham số: tên tệp tin và chế độ mở. Chế độ mở có thể là `r` (đọc), `w` (viết), `a` (thêm vào cuối), hoặc `x` (tạo mới). Sau khi mở tệp tin, chúng ta có thể đọc hoặc viết dữ liệu vào tệp tin bằng các hàm `read()` và `write()`. Cuối cùng, chúng ta nên đóng tệp tin bằng hàm `close()` để giải phóng tài nguyên.

## Ví dụ
Ví dụ, chúng ta muốn tạo một tệp tin văn bản mới và viết một dòng văn bản vào tệp tin đó:
```python
f = open("test.txt", "w")
f.write("Xin chào, thế giới!")
f.close()
```
Hoặc, chúng ta muốn đọc nội dung của một tệp tin văn bản:
```python
f = open("test.txt", "r")
content = f.read()
print(content)
f.close()
```
Chúng ta cũng có thể sử dụng câu lệnh `with` để mở và đóng tệp tin một cách an toàn:
```python
with open("test.txt", "r") as f:
    content = f.read()
    print(content)
```
## Bài tập
Bài tập 1: Tạo một tệp tin văn bản mới và viết 5 dòng văn bản vào tệp tin đó.
Bài tập 2: Đọc nội dung của một tệp tin văn bản và in ra màn hình.
Bài tập 3: Thêm 3 dòng văn bản vào cuối của một tệp tin văn bản có sẵn.
Bài tập 4: Tạo một tệp tin nhị phân mới và viết một số liệu vào tệp tin đó.
Bài tập 5: Đọc nội dung của một tệp tin nhị phân và in ra màn hình.

Bài tập này sẽ giúp bạn rèn luyện kỹ năng làm việc với tệp tin trong Python. Hãy thử nghiệm và tìm hiểu thêm về các hàm và phương thức liên quan đến tệp tin trong Python.
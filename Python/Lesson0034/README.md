# Python 34 cấp Cơ bản

## Giới thiệu

Bài học "Python 34 cấp Cơ bản" là bài thứ 34 trong chuỗi bài học giúp người mới bắt đầu làm quen với ngôn ngữ lập trình Python một cách hệ thống và dễ hiểu. Bài học này tập trung vào việc củng cố kiến thức cơ bản thông qua việc ôn tập các khái niệm đã học và áp dụng vào các ví dụ thực tế. Mục tiêu là giúp học viên tự tin hơn trong việc viết mã Python, hiểu rõ cấu trúc chương trình và cách sử dụng các câu lệnh điều kiện, vòng lặp, hàm và xử lý dữ liệu đơn giản.

## Lý thuyết

Trong bài học này, chúng ta sẽ ôn lại một số khái niệm trọng tâm của Python ở cấp độ cơ bản:
- Biến và kiểu dữ liệu: `int`, `float`, `str`, `bool`, `list`, `dict`.
- Câu lệnh điều kiện: `if`, `elif`, `else`.
- Vòng lặp: `for`, `while`.
- Hàm: định nghĩa với `def`, tham số, giá trị trả về.
- Xử lý lỗi cơ bản với `try` và `except`.

Việc nắm vững các khái niệm này là nền tảng để học các chủ đề nâng cao hơn như lập trình hướng đối tượng, làm việc với tệp và thư viện.

## Ví dụ

Dưới đây là ví dụ minh họa sử dụng hàm để kiểm tra số chẵn/lẻ:

```python
def kiem_tra_chan_le(n):
    if n % 2 == 0:
        return "Số chẵn"
    else:
        return "Số lẻ"

# Gọi hàm
so = 10
print(f"{so} là {kiem_tra_chan_le(so)}")
```

Kết quả:
```
10 là Số chẵn
```

## Bài tập

1. Viết hàm tính tổng các số từ 1 đến n.
2. Viết chương trình nhập vào một danh sách tên và in ra tên có độ dài lớn nhất.
3. Viết chương trình sử dụng vòng lặp `while` để đếm ngược từ 5 về 0, in ra màn hình từng số.

> Gợi ý: Sử dụng `input()` để nhận dữ liệu từ người dùng, và nhớ kiểm tra kiểu dữ liệu khi cần.

Hoàn thành bài tập sẽ giúp bạn củng cố kỹ năng lập trình cơ bản và chuẩn bị tốt hơn cho các bài học tiếp theo.
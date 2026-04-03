# Bài 20: Python Cơ bản

## Giới thiệu

Python là một trong những ngôn ngữ lập trình phổ biến nhất hiện nay nhờ cú pháp đơn giản, dễ học và khả năng ứng dụng rộng rãi trong nhiều lĩnh vực như lập trình web, phân tích dữ liệu, trí tuệ nhân tạo và tự động hóa. Bài học này sẽ cung cấp những kiến thức cơ bản nhất về Python, giúp người mới bắt đầu làm quen với cách viết và chạy chương trình đơn giản.

## Lý thuyết

Python là ngôn ngữ thông dịch, nghĩa là mã nguồn được thực thi từng dòng mà không cần biên dịch toàn bộ chương trình. Một chương trình Python thường bắt đầu với lệnh `print()` để xuất thông tin ra màn hình. Các kiểu dữ liệu cơ bản trong Python bao gồm:
- `int`: số nguyên (ví dụ: `5`, `-3`)
- `float`: số thập phân (ví dụ: `3.14`)
- `str`: chuỗi ký tự (ví dụ: `"Xin chào"`)
- `bool`: giá trị đúng/sai (`True` hoặc `False`)

Các biến trong Python được khai báo bằng cách gán giá trị thông qua dấu `=`. Python tự động nhận diện kiểu dữ liệu dựa trên giá trị được gán.

## Ví dụ

Dưới đây là một chương trình Python đơn giản in ra dòng chữ "Xin chào, thế giới!" và thực hiện một phép tính nhỏ:

```python
# In ra màn hình
print("Xin chào, thế giới!")

# Khai báo biến và tính toán
ten = "An"
tuoi = 15
diem_trung_binh = 8.7

print(f"Chào bạn {ten}, bạn {tuoi} tuổi và điểm trung bình là {diem_trung_binh}.")
```

Kết quả khi chạy chương trình:
```
Xin chào, thế giới!
Chào bạn An, bạn 15 tuổi và điểm trung bình là 8.7.
```

## Bài tập

1. Viết chương trình in ra tên và lớp của bạn.
2. Tạo hai biến `a` và `b` với giá trị số nguyên, sau đó in ra tổng của chúng.
3. Sử dụng `input()` để hỏi người dùng tên họ, rồi chào họ bằng câu: "Xin chào, [tên]!".

> Gợi ý: Dùng `input("Nhập tên: ")` để nhận dữ liệu từ người dùng.
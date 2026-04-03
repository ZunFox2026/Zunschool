# Python 5 cấp Cơ bản – Bài 5

## Giới thiệu

Chào mừng bạn đến với bài học thứ 5 trong chuỗi "Python 5 cấp Cơ bản"! Ở bài học này, chúng ta sẽ tìm hiểu về **câu lệnh điều kiện** – một trong những khái niệm nền tảng quan trọng nhất trong lập trình. Câu lệnh điều kiện giúp chương trình của bạn "ra quyết định" dựa trên các điều kiện cụ thể, từ đó thực hiện các hành động khác nhau. Điều này mở ra khả năng tạo ra các chương trình linh hoạt và thông minh hơn.

## Lý thuyết

Trong Python, câu lệnh điều kiện được thực hiện bằng từ khóa `if`, `elif` (else if) và `else`. Cú pháp cơ bản như sau:

```python
if điều_kiện:
    # Khối lệnh được thực hiện nếu điều kiện đúng
elif điều_kiện_khác:
    # Khối lệnh được thực hiện nếu điều kiện trước sai và điều kiện này đúng
else:
    # Khối lệnh được thực hiện nếu tất cả điều kiện trên đều sai
```

Các điều kiện thường sử dụng các toán tử so sánh như: `==`, `!=`, `<`, `>`, `<=`, `>=`. Kết quả của điều kiện là `True` hoặc `False`.

## Ví dụ

Dưới đây là một ví dụ đơn giản kiểm tra xem một số có phải là số dương, âm hay bằng không:

```python
so = int(input("Nhập một số: "))

if so > 0:
    print("Đây là số dương.")
elif so < 0:
    print("Đây là số âm.")
else:
    print("Đây là số không.")
```

Khi chạy chương trình, nếu người dùng nhập `5`, màn hình sẽ hiển thị: `Đây là số dương.`

## Bài tập

**Bài tập:** Viết chương trình yêu cầu người dùng nhập điểm số (từ 0 đến 10). Chương trình sẽ in ra xếp loại như sau:
- 9-10: Xuất sắc
- 7-8: Khá
- 5-6: Trung bình
- Dưới 5: Yếu

Gợi ý: Sử dụng `if`, `elif`, `else` để kiểm tra các khoảng điểm. Hãy thử tự viết code trước khi xem lời giải!
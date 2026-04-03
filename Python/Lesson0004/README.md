# Python 4 Cấp Độ Cơ Bản – Bài 4

## Giới thiệu

Bài học này nằm trong chuỗi bài "Python 4 Cấp Độ Cơ Bản", giúp người mới bắt đầu làm quen với ngôn ngữ lập trình Python một cách hệ thống. Ở bài 4, chúng ta sẽ tìm hiểu về **câu lệnh điều kiện** – một trong những nền tảng quan trọng nhất trong lập trình. Câu lệnh điều kiện cho phép chương trình đưa ra quyết định dựa trên các điều kiện cụ thể, từ đó thực hiện các hành động khác nhau.

## Lý thuyết

Trong Python, câu lệnh điều kiện được thực hiện chủ yếu bằng từ khóa `if`, `elif` (else if) và `else`. Cú pháp cơ bản như sau:

```python
if điều_kiện:
    # Khối lệnh được thực hiện nếu điều_kiện đúng
elif điều_kiện_khác:
    # Khối lệnh được thực hiện nếu điều_kiện_khác đúng
else:
    # Khối lệnh được thực hiện nếu tất cả điều kiện trên sai
```

Các toán tử so sánh thường dùng: `==` (bằng), `!=` (khác), `<`, `>`, `<=`, `>=`. Kết quả của điều kiện là `True` hoặc `False`.

## Ví dụ

Dưới đây là một chương trình kiểm tra số chẵn/lẻ:

```python
so = int(input("Nhập một số nguyên: "))

if so % 2 == 0:
    print("Số bạn nhập là số chẵn.")
else:
    print("Số bạn nhập là số lẻ.")
```

Chương trình này yêu cầu người dùng nhập một số, sau đó kiểm tra xem số đó chia hết cho 2 hay không. Nếu có, in ra "số chẵn", ngược lại in ra "số lẻ".

## Bài tập

1. Viết chương trình nhập tuổi của một người, in ra "Bạn đã đủ tuổi lái xe" nếu tuổi >= 18, ngược lại in ra "Bạn chưa đủ tuổi lái xe".
2. Viết chương trình nhập ba số a, b, c, tìm và in ra số lớn nhất.
3. Viết chương trình kiểm tra xem một năm có phải là năm nhuận hay không (năm nhuận chia hết cho 4, nhưng nếu chia hết cho 100 thì phải chia hết cho 400).

> Gợi ý: Sử dụng `if`, `elif`, `else` và các toán tử so sánh để hoàn thành bài tập.
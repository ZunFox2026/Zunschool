# Python 27: Lập Trình Cơ Bản Từ A Đến Z

## Giới thiệu

Bài học này là phần tổng kết của chuỗi bài "Lập Trình Cơ Bản Từ A Đến Z", giúp người học hệ thống lại toàn bộ kiến thức lập trình Python ở cấp độ cơ bản. Dù bạn mới bắt đầu hay đang ôn tập, bài học này sẽ củng cố nền tảng vững chắc để bạn tự tin bước vào các chủ đề nâng cao như lập trình hướng đối tượng, làm việc với file, hoặc phát triển ứng dụng.

## Lý thuyết

Lập trình cơ bản bao gồm các khái niệm cốt lõi:
- **Biến và kiểu dữ liệu**: số nguyên (`int`), số thực (`float`), chuỗi (`str`), boolean (`bool`).
- **Câu điều kiện**: `if`, `elif`, `else` để rẽ nhánh chương trình.
- **Vòng lặp**: `for` và `while` dùng để lặp lại công việc.
- **Hàm**: `def` giúp nhóm mã thành các khối có thể tái sử dụng.
- **Danh sách (list)**: cấu trúc dữ liệu lưu trữ nhiều phần tử.

Hiểu rõ các khái niệm này là bước nền tảng để phát triển các chương trình thực tế.

## Ví dụ

Dưới đây là một chương trình Python nhỏ minh họa các khái niệm trên: kiểm tra số chẵn/lẻ và tính tổng các số từ 1 đến n.

```python
def tinh_tong(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i
    return tong

def kiem_tra_chan_le(so):
    if so % 2 == 0:
        return "chẵn"
    else:
        return "lẻ"

# Chương trình chính
n = int(input("Nhập một số nguyên: "))
print(f"Số {n} là số {kiem_tra_chan_le(n)}")
print(f"Tổng các số từ 1 đến {n} là: {tinh_tong(n)}")
```

## Bài tập

1. Viết hàm tính giai thừa của một số nguyên dương.
2. Tạo chương trình nhập vào danh sách tên, sau đó in ra theo thứ tự ngược lại.
3. Viết vòng lặp in các số từ 1 đến 50, nhưng nếu số chia hết cho 3 thì in "Fizz", chia hết cho 5 thì in "Buzz", nếu chia hết cho cả hai thì in "FizzBuzz".

> **Gợi ý**: Sử dụng `if-elif-else` và toán tử `%` để kiểm tra chia hết.

Chúc bạn học tốt và thành thạo lập trình Python từ những bước cơ bản nhất!
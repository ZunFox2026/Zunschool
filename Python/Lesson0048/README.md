# Python 48 Cấp Cơ Bản

## Giới thiệu

Bài học "Python 48 Cấp Cơ Bản" là bài thứ 48 trong chuỗi bài học được thiết kế giúp người mới bắt đầu làm quen và nắm vững các kiến thức lập trình Python từ cơ bản đến nâng cao. Bài học này tập trung vào việc tổng hợp và vận dụng các khái niệm đã học như biến, vòng lặp, điều kiện, hàm và cấu trúc dữ liệu để giải quyết các bài toán thực tế. Đây là bước quan trọng để người học củng cố nền tảng trước khi chuyển sang các chủ đề nâng cao hơn như làm việc với file, thư viện hay lập trình hướng đối tượng.

## Lý thuyết

Trong bài học này, chúng ta ôn lại các kiến thức nền tảng của Python:
- **Biến và kiểu dữ liệu**: int, float, str, bool, list, dict,...
- **Cấu trúc điều kiện**: `if`, `elif`, `else`
- **Vòng lặp**: `for`, `while`
- **Hàm**: định nghĩa bằng `def`, tham số, giá trị trả về
- **Xử lý lỗi cơ bản**: dùng `try-except`

Mục tiêu là giúp người học biết cách kết hợp các thành phần này để viết chương trình hoàn chỉnh, có logic rõ ràng và dễ bảo trì.

## Ví dụ

Dưới đây là một ví dụ tổng hợp sử dụng các kiến thức trên để kiểm tra số nguyên tố:

```python
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Kiểm tra các số từ 1 đến 10
for num in range(1, 11):
    if kiem_tra_so_nguyen_to(num):
        print(f"{num} là số nguyên tố")
    else:
        print(f"{num} không phải số nguyên tố")
```

## Bài tập

1. Viết hàm tính tổng các số chẵn trong danh sách.
2. Viết chương trình nhập vào một chuỗi và đếm số lần xuất hiện của từng ký tự (không phân biệt hoa thường).
3. Tạo danh sách các số từ 1 đến 20, sau đó in ra các số chia hết cho 3 hoặc 5.

> Gợi ý: Sử dụng vòng lặp, điều kiện và cấu trúc dữ liệu list hoặc dict để giải quyết bài tập.
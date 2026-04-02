# Bài 36: Python Cơ Bản

## Giới thiệu
Chào mừng bạn đến với **Bài 36: Python Cơ Bản**. Đây là bài học tổng hợp, được thiết kế đặc biệt cho người mới bắt đầu nhằm hệ thống hóa các kiến thức nền tảng nhất. Mục tiêu là giúp bạn nắm vững cú pháp, tư duy điều khiển luồng chương trình và kỹ năng viết code sạch, dễ bảo trì. Sau bài học, bạn sẽ tự tin xử lý dữ liệu cơ bản, triển khai logic rẽ nhánh/lặp và đóng gói code thành các hàm tái sử dụng, tạo nền tảng vững chắc cho các chủ đề nâng cao sau này.

## Lý thuyết
Bài học tập trung vào ba trụ cột cốt lõi:
- **Biến & Kiểu dữ liệu:** Python dùng định kiểu động, cho phép gán giá trị linh hoạt. Các kiểu thường gặp: `int`, `float`, `str`, `bool`, `list`, `dict`. Hiểu rõ bản chất kiểu giúp tránh lỗi `TypeError` và tối ưu hiệu năng.
- **Cấu trúc điều khiển:** `if/elif/else` xử lý rẽ nhánh; `for` lặp qua dãy hoặc `range()`; `while` lặp khi điều kiện đúng. **Quy tắc vàng:** Thụt lề (indentation) là bắt buộc để Python xác định khối lệnh, thường dùng 4 khoảng trắng.
- **Hàm (Functions):** Định nghĩa bằng `def`, giúp chia nhỏ bài toán. Hàm có thể nhận tham số (vị trí, từ khóa, mặc định) và trả kết quả qua `return`. Việc đặt tên hàm rõ nghĩa và viết docstring là thói quen tốt ngay từ đầu.

## Ví dụ
Minh họa kết hợp hàm, vòng lặp và điều kiện để kiểm tra số nguyên tố:
```python
def kiem_tra_nguyen_to(n):
    """Kiểm tra số nguyên tố cơ bản."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

so_test = 29
ket_qua = kiem_tra_nguyen_to(so_test)
print(f"Số {so_test} có phải nguyên tố? {ket_qua}")
```

## Bài tập
Thực hành ngay để củng cố kiến thức:
1. Viết hàm `tinh_tong_chu_so(n)` nhận số nguyên dương `n`, trả về tổng các chữ số của nó.
2. Dùng vòng lặp `for` in ra bảng cửu chương từ 2 đến 9, mỗi bảng cách nhau một dòng trống.
3. Tạo list chứa 10 số ngẫu nhiên (1–100), dùng `if` và `for` in ra các số chia hết cho 3 hoặc 5.

💡 *Mẹo:* Luôn kiểm tra kiểu đầu vào, dùng f-string định dạng output và ghi chú thích ngắn gọn. Nếu gặp lỗi, hãy đọc kỹ traceback và kiểm tra thụt lề. Chúc bạn code vui! 🐍
# Python 54 Cấp Cơ Bản

## Giới thiệu

Bài học "Python 54 Cấp Cơ Bản" là bài thứ 54 trong chuỗi bài học từ cơ bản đến nâng cao với ngôn ngữ lập trình Python. Bài học này tập trung vào việc củng cố kiến thức về **hàm (functions)** – một khái niệm nền tảng giúp tổ chức và tái sử dụng mã hiệu quả. Việc hiểu và sử dụng hàm đúng cách sẽ giúp người học viết chương trình rõ ràng, dễ bảo trì và phát triển.

## Lý thuyết

Hàm trong Python là khối lệnh thực hiện một nhiệm vụ cụ thể và có thể được gọi từ bất kỳ đâu trong chương trình. Hàm giúp tránh lặp lại mã và chia nhỏ chương trình thành các phần nhỏ dễ quản lý.

Cú pháp định nghĩa hàm:
```python
def ten_ham(tham_so):
    # Nội dung hàm
    return ket_qua
```

- Từ khóa `def` dùng để khai báo hàm.
- `tham_so` là các giá trị đầu vào (có thể có hoặc không).
- Câu lệnh `return` trả về kết quả (tùy chọn).

Hàm có thể không trả về giá trị (hàm void), hoặc trả về một hoặc nhiều giá trị.

## Ví dụ

Dưới đây là ví dụ về hàm tính tổng hai số:

```python
def tinh_tong(a, b):
    return a + b

# Gọi hàm
ket_qua = tinh_tong(5, 3)
print("Tổng là:", ket_qua)  # Kết quả: Tổng là: 8
```

## Bài tập

1. Viết hàm `tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong)` nhận vào chiều dài và chiều rộng, trả về diện tích hình chữ nhật.
2. Viết hàm `kiem_tra_chan_le(n)` kiểm tra và in ra số `n` là chẵn hay lẻ.
3. Viết hàm `tinh_giai_thua(n)` tính giai thừa của một số nguyên dương (sử dụng vòng lặp hoặc đệ quy đơn giản).

> Gợi ý: Sử dụng `return` để trả về kết quả và gọi hàm để kiểm tra kết quả.
# Python 31 Cấp Cơ Bản

## Giới thiệu

Bài học số 31 trong chuỗi bài học "Python 31 cấp Cơ bản" giúp người học củng cố kiến thức lập trình cơ bản bằng Python thông qua việc luyện tập với hàm, vòng lặp và xử lý dữ liệu đơn giản. Đây là bước quan trọng để chuẩn bị cho các chủ đề nâng cao hơn như làm việc với tệp, thư viện hay lập trình hướng đối tượng. Bài học này tập trung vào việc áp dụng kiến thức đã học vào thực hành, giúp người học hiểu sâu hơn về cách tổ chức mã nguồn và giải quyết bài toán cụ thể.

## Lý thuyết

Trong bài học này, chúng ta sẽ ôn lại các khái niệm cơ bản như:
- **Hàm (def)**: Cách định nghĩa và sử dụng hàm để tái sử dụng mã.
- **Vòng lặp (for, while)**: Lặp qua danh sách hoặc thực hiện công việc lặp lại.
- **Cấu trúc điều kiện (if, elif, else)**: Rẽ nhánh chương trình dựa trên điều kiện.
- **Danh sách (list)**: Lưu trữ và xử lý nhiều phần tử.

Việc kết hợp các thành phần này giúp xây dựng chương trình rõ ràng, dễ bảo trì và mở rộng.

## Ví dụ

Dưới đây là một ví dụ về hàm tính tổng các số chẵn trong danh sách:

```python
def tong_so_chan(danh_sach):
    tong = 0
    for so in danh_sach:
        if so % 2 == 0:
            tong += so
    return tong

# Gọi hàm
ds = [1, 2, 3, 4, 5, 6]
ket_qua = tong_so_chan(ds)
print("Tổng các số chẵn là:", ket_qua)
```

Kết quả: `Tổng các số chẵn là: 12`

## Bài tập

1. Viết hàm `dem_so_le(danh_sach)` đếm số lượng số lẻ trong danh sách.
2. Viết hàm `tim_so_lon_nhat(danh_sach)` trả về số lớn nhất mà **không dùng hàm max()**.
3. (Nâng cao) Viết chương trình nhập vào một danh sách số nguyên từ bàn phím, sau đó in ra tổng, trung bình và các số chẵn.

Chúc bạn học tốt và thành thạo Python!
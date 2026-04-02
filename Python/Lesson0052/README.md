## Giới thiệu
Chào mừng bạn đến với **Bài 52: Python Cơ bản**. Bài học này được thiết kế dành cho người mới bắt đầu, giúp bạn làm chủ nền tảng lập trình Python một cách hệ thống và thực tiễn. Qua bài học, bạn sẽ hiểu rõ luồng thực thi chương trình, biết cách khai báo biến, xử lý kiểu dữ liệu, áp dụng cấu trúc điều khiển và đóng gói logic vào hàm. Mục tiêu là giúp bạn tự tin viết, chạy và gỡ lỗi những script Python đầu tiên. Hãy đảm bảo môi trường Python 3.8+ đã sẵn sàng và cùng bắt đầu!

## Lý thuyết
Python nổi bật nhờ cú pháp trực quan và triết lý "code dễ đọc". Các kiến thức trọng tâm gồm:
- **Biến & Kiểu dữ liệu:** Python tự động suy luận kiểu. Kiểu cơ bản: `int`, `float`, `str`, `bool`. Kiểm tra bằng `type()`.
- **Toán tử:** Số học (`+`, `-`, `*`, `/`, `//`, `%`, `**`), so sánh (`==`, `!=`, `>`, `<=`), logic (`and`, `or`, `not`).
- **Cấu trúc điều khiển:** `if/elif/else` xử lý rẽ nhánh; `for` duyệt iterable; `while` lặp khi điều kiện đúng. Kết hợp `break`, `continue`.
- **Hàm (Function):** Khai báo bằng `def`, hỗ trợ tham số mặc định, `*args`. Trả kết quả bằng `return`. Hàm giúp mã modular và dễ bảo trì.
- **Quy tắc bắt buộc:** Thụt lề (indentation) thay thế dấu `{}`. Khuyến nghị 4 khoảng trắng, tuân thủ PEP 8.

## Ví dụ
```python
# Ví dụ tổng hợp: Tính điểm trung bình và xếp loại
def tinh_diem_trung_binh(d_toan, d_ly, d_hoa):
    return (d_toan + d_ly + d_hoa) / 3

def xep_loai(dtb):
    if dtb >= 8.5: return "Giỏi"
    elif dtb >= 6.5: return "Khá"
    elif dtb >= 5.0: return "Trung bình"
    else: return "Yếu"

# Dữ liệu mẫu & thực thi
diem = [8.0, 7.5, 9.0]
dtb = tinh_diem_trung_binh(*diem)
print(f"Điểm trung bình: {dtb:.2f} → Xếp loại: {xep_loai(dtb)}")
```

## Bài tập
1. **Hình học cơ bản:** Viết chương trình nhập bán kính `r`, tính chu vi `C = 2πr` và diện tích `S = πr²`. In kết quả định dạng `.2f`.
2. **Năm nhuận:** Tạo hàm `la_nam_nhuan(nam)` trả về `True/False`. Dùng vòng lặp `for` liệt kê năm nhuận trong khoảng 2000–2025.
3. **Xử lý danh sách:** Cho danh sách `[{"ten": "An", "toan": 9, "van": 7}, ...]`. Viết hàm tính DTB, xếp loại từng người, in bảng kết quả căn chỉnh cột.

💡 *Mẹo:* Luôn kiểm tra kiểu dữ liệu đầu vào, chia nhỏ bài toán thành hàm con, và chạy thử từng phần. Chúc bạn thực hành hiệu quả!
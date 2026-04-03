"""
Python 33 Cấp Cơ Bản - Bài học 1: Các Khái Niệm Cơ Bản trong Python
Tác giả: Học viên Python
Ngày: 2023-11-05
Mô tả: Bài học đầu tiên giúp người mới bắt đầu làm quen với cú pháp cơ bản,
         biến, kiểu dữ liệu, vòng lặp, hàm và xử lý lỗi đơn giản.
"""

# 1. In ra màn hình
print("Chào mừng bạn đến với Python 33 Cấp Cơ Bản!")

# 2. Biến và kiểu dữ liệu
ten = "An"           # Chuỗi (string)
tuoi = 16            # Số nguyên (int)
chieu_cao = 1.75     # Số thực (float)
la_hoc_sinh = True   # Boolean (True/False)

# In thông tin ra màn hình
print(f"Tên: {ten}, Tuổi: {tuoi}, Chiều cao: {chieu_cao}m, Là học sinh: {la_hoc_sinh}")

# 3. Danh sách (list) và vòng lặp for
diem_so = [8, 9, 7, 10, 8.5]
print("Các điểm số của bạn An:")
for diem in diem_so:
    print(f" - {diem}")

# 4. Sử dụng hàm để tính trung bình
def tinh_diem_trung_binh(danh_sach_diem):
    """
    Hàm tính điểm trung bình của danh sách điểm
    :param danh_sach_diem: list các số thực
    :return: điểm trung bình (float)
    """
    if len(danh_sach_diem) == 0:
        return 0
    tong = sum(danh_sach_diem)
    trung_binh = tong / len(danh_sach_diem)
    return trung_binh

# Gọi hàm và in kết quả
dtb = tinh_diem_trung_binh(diem_so)
print(f"Điểm trung bình: {dtb:.2f}")

# 5. Ví dụ 2: Kiểm tra số chẵn/lẻ
def kiem_tra_chan_le(so):
    if so % 2 == 0:
        return f"{so} là số chẵn."
    else:
        return f"{so} là số lẻ."

# Sử dụng hàm
print(kiem_tra_chan_le(7))
print(kiem_tra_chan_le(4))

# 6. Ví dụ 3: Xử lý lỗi với try-except
def chia_hai_so(a, b):
    """
    Hàm chia hai số, xử lý lỗi chia cho 0
    """
    try:
        ket_qua = a / b
        return f"{a} chia {b} = {ket_qua}"
    except ZeroDivisionError:
        return "Lỗi: Không thể chia cho 0!"

# Thử gọi hàm với các trường hợp
print(chia_hai_so(10, 2))
print(chia_hai_so(10, 0))

# 7. Bài tập nhỏ: Đếm số chẵn trong danh sách
"""
Bài tập:
Viết hàm dem_so_chan(danh_sach) nhận vào một danh sách số nguyên
và trả về số lượng số chẵn trong danh sách.
"""

def dem_so_chan(danh_sach):
    """
    Đếm số lượng số chẵn trong danh sách
    :param danh_sach: list số nguyên
    :return: số lượng số chẵn (int)
    """
    dem = 0
    for so in danh_sach:
        if so % 2 == 0:
            dem += 1
    return dem

# Kiểm thử bài tập
so_nguyen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ket_qua_bai_tap = dem_so_chan(so_nguyen)
print(f"Danh sách: {so_nguyen}")
print(f"Số lượng số chẵn: {ket_qua_bai_tap}")

# 8. Tổng kết và in lời chào
print("\n--- Hoàn thành bài học cơ bản đầu tiên! ---")
print("Hãy luyện tập thêm bằng cách tự viết các hàm nhỏ và xử lý dữ liệu!")

# Chạy chương trình chính
def main():
    print("=== CHƯƠNG TRÌNH CHÍNH ===")
    print("Đây là bài học cơ bản đầu tiên trong chuỗi 33 cấp Python.")
    tinh_diem_trung_binh([7, 8, 9])
    print(kiem_tra_chan_le(15))
    print(chia_hai_so(20, 4))
    print(f"Đếm số chẵn: {dem_so_chan([2, 4, 6, 7, 9])}")

# Gọi hàm main khi chạy file
if __name__ == "__main__":
    main()
```

---

✅ **Giải thích ngắn:**
- File Python này giới thiệu các khái niệm cơ bản: biến, kiểu dữ liệu, vòng lặp, hàm, xử lý lỗi.
- Có 3 ví dụ minh họa: tính điểm trung bình, kiểm tra chẵn lẻ, chia số an toàn.
- Bài tập nhỏ: đếm số chẵn trong danh sách (kèm lời giải).
- Dùng `main()` và `if __name__ == "__main__":` để kiểm soát luồng chương trình.

📁 Lưu file với tên: `python_33_co_ban_bai1.py` và chạy bằng Python 3.
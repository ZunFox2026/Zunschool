"""
Bài học: Python 28 Cấp Cơ Bản (Mẫu đại diện)
Mục tiêu: Giới thiệu 28 khái niệm cơ bản qua ví dụ và bài tập nhỏ
Tác giả: Học viên Python
Ngày: 2024
"""

def main():
    # 1. In ra màn hình
    print("=== PYTHON 28 CẤP CƠ BẢN ===")

    # 2. Biến và kiểu dữ liệu
    ten = "Python"          # chuỗi
    tuoi = 10               # số nguyên
    diem = 9.5              # số thực
    dat_diem = True         # boolean

    # 3. In biến
    print(f"Tên: {ten}, Tuổi: {tuoi}, Điểm: {diem}, Đạt điểm: {dat_diem}")

    # 4. Nhập dữ liệu từ người dùng
    ten_nguoi_dung = input("Nhập tên của bạn: ")

    # 5-6. Câu điều kiện if-else
    if len(ten_nguoi_dung) > 5:
        print("Tên bạn khá dài!")
    else:
        print("Tên bạn ngắn gọn!")

    # 7. Vòng lặp for
    print("In số từ 1 đến 5:")
    for i in range(1, 6):
        print(i, end=" ")
    print()  # xuống dòng

    # 8. Danh sách (list)
    mon_hoc = ["Toán", "Lý", "Hóa", "Sinh"]
    print("Các môn học:", mon_hoc)

    # 9. Truy cập phần tử danh sách
    print("Môn đầu tiên:", mon_hoc[0])

    # 10. Thêm phần tử vào danh sách
    mon_hoc.append("Văn")
    print("Sau khi thêm Văn:", mon_hoc)

    # 11. Vòng lặp while
    dem = 0
    print("Đếm ngược từ 3:")
    while dem < 3:
        print(3 - dem)
        dem += 1

    # 12. Hàm đơn giản
    def xin_chao(ten):
        return f"Xin chào, {ten}!"

    # 13. Gọi hàm
    print(xin_chao(ten_nguoi_dung))

    # 14. Hàm với tham số mặc định
    def chao_hoi(ten, loi_chao="Xin chào"):
        return f"{loi_chao}, {ten}!"

    print(chao_hoi("An"))  # dùng mặc định
    print(chao_hoi("Bình", "Chúc mừng"))  # thay đổi tham số

    # 15. Dictionary (từ điển)
    hoc_sinh = {
        "ten": "Minh",
        "lop": "8A",
        "diem_toan": 9
    }
    print("Thông tin học sinh:", hoc_sinh)

    # 16. Truy cập giá trị trong dictionary
    print("Học sinh tên:", hoc_sinh["ten"])

    # 17. Thêm cặp key-value
    hoc_sinh["diem_van"] = 8.5
    print("Sau khi thêm điểm Văn:", hoc_sinh)

    # 18. Xử lý ngoại lệ (try-except)
    try:
        chia = 10 / 0
    except ZeroDivisionError:
        print("Không thể chia cho 0!")

    # 19. Kiểm tra kiểu dữ liệu
    print("Kiểu dữ liệu của 'tuoi':", type(tuoi))

    # 20. Ép kiểu
    so_chuoi = "123"
    so_thuc = int(so_chuoi) + 1
    print("Ép kiểu chuỗi thành số:", so_thuc)

    # 21. Hàm len()
    print("Độ dài tên bạn:", len(ten_nguoi_dung))

    # 22. Cắt chuỗi
    chuoi = "Hello World"
    print("Cắt 5 ký tự đầu:", chuoi[:5])

    # 23. upper() và lower()
    print("Chuyển thành in hoa:", chuoi.upper())

    # 24. Kiểm tra chuỗi con
    if "World" in chuoi:
        print("Chuỗi có chứa 'World'")

    # 25. Tạo danh sách bằng comprehension
    binh_phuong = [x**2 for x in range(1, 6)]
    print("Bình phương các số 1-5:", binh_phuong)

    # 26. Sử dụng tuple
    diem_xy = (3, 4)
    print("Tọa độ điểm:", diem_xy)

    # 27. Import module
    import math
    print("Căn bậc 2 của 16:", math.sqrt(16))

    # 28. Ghi chú và tài liệu (đang làm!)

    # === VÍ DỤ THỰC HÀNH ===
    print("\n=== VÍ DỤ 1: Tính tổng dãy số ===")
    day_so = [1, 2, 3, 4, 5]
    tong = sum(day_so)
    print(f"Tổng {day_so} = {tong}")

    print("\n=== VÍ DỤ 2: Kiểm tra số chẵn ===")
    for num in [2, 7, 8, 11]:
        loai = "chẵn" if num % 2 == 0 else "lẻ"
        print(f"{num} là số {loai}")

    # === BÀI TẬP NHỎ ===
    print("\n=== BÀI TẬP: Đảo ngược chuỗi ===")
    chuoi_bai_tap = input("Nhập một chuỗi: ")
    chuoi_dao = chuoi_bai_tap[::-1]
    print(f"Chuỗi đảo ngược: {chuoi_dao}")

    print("Hoàn thành 28 cấp cơ bản!")


# Chạy chương trình
if __name__ == "__main__":
    main()
```

---

### Hướng dẫn sử dụng:
1. Lưu file với tên `python_28_cap_co_ban.py`
2. Chạy bằng lệnh: `python python_28_cap_co_ban.py`
3. Nhập tên và một chuỗi khi được yêu cầu

### Mục tiêu đạt được:
- Hiểu 28 khái niệm cơ bản trong Python
- Thực hành với ví dụ minh họa
- Làm bài tập nhỏ để củng cố kiến thức

> ✅ Phù hợp cho người mới bắt đầu học Python!
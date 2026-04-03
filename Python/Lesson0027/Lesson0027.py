# Python 27: Lập Trình Cơ Bản Từ A Đến Z
# Bài học: Tìm hiểu các khái niệm cơ bản trong Python: biến, kiểu dữ liệu, điều kiện, vòng lặp, hàm và danh sách.

def main():
    # --- 1. Biến và Kiểu Dữ Liệu ---
    # Biến là nơi lưu trữ dữ liệu
    ten = "An"           # chuỗi (string)
    tuoi = 16            # số nguyên (int)
    chieu_cao = 1.75     # số thực (float)
    la_hoc_sinh = True   # giá trị logic (boolean)

    print("Thông tin cá nhân:")
    print(f"Tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Chiều cao: {chieu_cao} m")
    print(f"Là học sinh: {la_hoc_sinh}")

    # --- 2. Câu lệnh điều kiện (if-elif-else) ---
    # Ví dụ 1: Kiểm tra tuổi để biết học sinh có được lái xe không
    if tuoi >= 18:
        print(f"{ten} đã đủ tuổi để lái xe.")
    else:
        print(f"{ten} chưa đủ tuổi lái xe. Cần chờ {18 - tuoi} năm nữa.")

    # Ví dụ 2: Phân loại học lực theo điểm số
    diem = 8.5
    if diem >= 9.0:
        xep_loai = "Xuất sắc"
    elif diem >= 8.0:
        xep_loai = "Giỏi"
    elif diem >= 6.5:
        xep_loai = "Khá"
    else:
        xep_loai = "Cần cố gắng hơn"

    print(f"Điểm: {diem} → Xếp loại: {xep_loai}")

    # --- 3. Vòng lặp (for) ---
    # Ví dụ: In ra các số từ 1 đến 5
    print("\nIn số từ 1 đến 5:")
    for i in range(1, 6):
        print(f"Số: {i}")

    # --- 4. Danh sách (list) ---
    # Tạo danh sách các môn học
    cac_mon_hoc = ["Toán", "Lý", "Hóa", "Văn", "Anh"]

    print("\nCác môn học yêu thích:")
    for mon in cac_mon_hoc:
        print(f"• {mon}")

    # Thêm môn học mới
    cac_mon_hoc.append("Sử")
    print(f"\nSau khi thêm môn Sử: {cac_mon_hoc}")

    # --- 5. Hàm (function) ---
    # Hàm tính diện tích hình chữ nhật
    def tinh_dien_tich_chu_nhat(chieu_dai, chieu_rong):
        """Tính diện tích hình chữ nhật"""
        return chieu_dai * chieu_rong

    # Gọi hàm và in kết quả
    dien_tich = tinh_dien_tich_chu_nhat(10, 5)
    print(f"\nDiện tích hình chữ nhật 10x5: {dien_tich} m²")

    # Hàm chào hỏi
    def chao_teo(ten, tuoi):
        return f"Xin chào, tôi tên là {ten}, năm nay {tuoi} tuổi!"

    loi_chao = chao_teo("Bình", 15)
    print(loi_chao)

    # --- Bài tập nhỏ ---
    print("\n--- BÀI TẬP NHỎ ---")
    print("1. Viết chương trình nhập vào tên và điểm số, in ra xếp loại học lực.")
    print("2. Tạo danh sách 3 thành phố bạn muốn đến, in ra và thêm 1 thành phố nữa.")
    print("3. Viết hàm tính chu vi hình tròn với công thức: 2 * pi * r")

    # Gợi ý giải bài tập 3:
    import math

    def tinh_chu_vi_hinh_tron(ban_kinh):
        return 2 * math.pi * ban_kinh

    # Kiểm thử hàm
    chu_vi = tinh_chu_vi_hinh_tron(5)
    print(f"Chu vi hình tròn bán kính 5: {chu_vi:.2f}")

    print("\nChúc mừng bạn đã hoàn thành bài học cơ bản!")


# Gọi hàm chính
if __name__ == "__main__":
    main()
```

---

✅ **Giải thích ngắn:**
- Bài học tổng hợp các khái niệm cơ bản nhất trong Python.
- Có 2 ví dụ rõ ràng về `if` và `for`.
- 3 bài tập nhỏ giúp luyện tập.
- Dùng `f-string`, hàm, list, kiểu dữ liệu, nhập/xuất cơ bản.

📌 **Hướng dẫn sử dụng:**
1. Lưu mã vào file `basic_python_27.py`
2. Chạy bằng lệnh: `python basic_python_27.py`
3. Xem kết quả và thử sửa đổi theo ý bạn!
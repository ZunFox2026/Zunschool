# python_basics_10_levels.py
# Tên file: python_basics_10_levels.py
# Mô tả: Bài học Python 10 cấp độ cơ bản - Dành cho người mới bắt đầu
# Gồm các chủ đề từ biến, kiểu dữ liệu, điều kiện, vòng lặp đến hàm và danh sách

def main():
    print("=== PYTHON 10 CẤP CƠ BẢN - BÀI HỌC GIỚI THIỆU ===\n")

    # Cấp 1: In ra màn hình
    print("Cấp 1: In ra màn hình")
    print("Xin chào, đây là bài học Python cơ bản!")
    
    # Cấp 2: Biến và kiểu dữ liệu
    print("\nCấp 2: Biến và kiểu dữ liệu")
    ten = "An"           # chuỗi
    tuoi = 15            # số nguyên
    chieu_cao = 1.65     # số thực
    hoc_gioi = True      # boolean
    print(f"Tên: {ten}, Tuổi: {tuoi}, Chiều cao: {chieu_cao}m, Học giỏi: {hoc_gioi}")

    # Cấp 3: Nhập dữ liệu từ người dùng
    print("\nCấp 3: Nhập dữ liệu")
    ten_nguoi_dung = input("Nhập tên của bạn: ")
    print(f"Rất vui được gặp bạn, {ten_nguoi_dung}!")

    # Cấp 4: Câu điều kiện if-else
    print("\nCấp 4: Câu điều kiện")
    diem = 8
    if diem >= 5:
        print("Bạn đã đậu!")
    else:
        print("Bạn cần cố gắng hơn.")

    # Cấp 5: Vòng lặp for
    print("\nCấp 5: Vòng lặp for")
    print("In các số từ 1 đến 5:")
    for i in range(1, 6):
        print(i, end=" ")
    print()  # Xuống dòng

    # Cấp 6: Vòng lặp while
    print("\nCấp 6: Vòng lặp while")
    dem = 3
    while dem > 0:
        print(f"Còn {dem} giây...")
        dem -= 1
    print("Hết giờ!")

    # Cấp 7: Danh sách (list)
    print("\nCấp 7: Danh sách")
    mon_an = ["Phở", "Cơm", "Bún"]
    print("Các món ăn yêu thích:", mon_an)
    mon_an.append("Sushi")  # Thêm phần tử
    print("Sau khi thêm Sushi:", mon_an)

    # Cấp 8: Hàm đơn giản
    print("\nCấp 8: Hàm")
    def xin_chao(ten):
        return f"Xin chào, {ten}!"
    
    print(xin_chao("Bình"))

    # Cấp 9: Xử lý lỗi đơn giản (try-except)
    print("\nCấp 9: Xử lý lỗi")
    try:
        so = int(input("Nhập một số nguyên: "))
        print(f"Bạn đã nhập: {so}")
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")

    # Cấp 10: Tổng hợp ví dụ nhỏ
    print("\nCấp 10: Tổng hợp - Tính tổng các số chẵn từ 1 đến 10")
    tong = 0
    for num in range(1, 11):
        if num % 2 == 0:
            tong += num
    print(f"Tổng các số chẵn từ 1 đến 10 là: {tong}")

    # === VÍ DỤ THỰC HÀNH ===
    print("\n=== VÍ DỤ THỰC HÀNH ===")
    # Ví dụ 1: Tính điểm trung bình
    print("Ví dụ 1: Tính điểm trung bình")
    diem_toan = 8.5
    diem_van = 7.0
    dtb = (diem_toan + diem_van) / 2
    print(f"Điểm trung bình: {dtb:.1f}")

    # Ví dụ 2: Kiểm tra số chẵn/lẻ
    print("\nVí dụ 2: Kiểm tra số chẵn/lẻ")
    n = 7
    if n % 2 == 0:
        print(f"{n} là số chẵn.")
    else:
        print(f"{n} là số lẻ.")

    # === BÀI TẬP NHỎ ===
    print("\n=== BÀI TẬP NHỎ ===")
    print("Bài tập: Viết chương trình nhập 3 số và in ra số lớn nhất.")
    print("Gợi ý: Dùng hàm max() hoặc câu điều kiện if-elif-else.")

    # Gợi ý giải bài tập (có thể uncomment để chạy)
    """
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    c = float(input("Nhập số thứ ba: "))
    lon_nhat = max(a, b, c)
    print(f"Số lớn nhất là: {lon_nhat}")
    """

    print("\nChúc mừng bạn đã hoàn thành 10 cấp độ cơ bản!")
    print("Hãy luyện tập thêm để thành thạo Python!")

# Chạy chương trình
if __name__ == "__main__":
    main()
```

---

### 💡 **Hướng dẫn sử dụng:**
- Lưu nội dung trên vào file `python_basics_10_levels.py`
- Chạy bằng lệnh: `python python_basics_10_levels.py`
- Học theo từng cấp, đọc comment tiếng Việt để hiểu
- Làm bài tập nhỏ để củng cố kiến thức

### ✅ Mục tiêu đạt được:
- Hiểu các khái niệm cơ bản của Python
- Biết sử dụng biến, vòng lặp, điều kiện, hàm
- Rèn kỹ năng lập trình qua ví dụ và bài tập

--- 
**Chúc bạn học Python vui vẻ và hiệu quả! 🐍**
# Python 22 Cấp Cơ Bản - Bài học tổng hợp 22 cấp độ cơ bản trong Python
# Tác giả: Học viên Python
# Mục tiêu: Ôn tập các khái niệm cơ bản trong Python qua 22 cấp độ
# Độ dài: Khoảng 100 dòng, có ví dụ và bài tập nhỏ

def main():
    """
    Hàm chính thực hiện 22 cấp độ cơ bản trong Python
    Mỗi cấp là một khái niệm đơn giản, được minh họa bằng ví dụ
    """

    print("=== KHỞI ĐỘNG: 22 CẤP CƠ BẢN TRONG PYTHON ===\n")

    # Cấp 1: In ra màn hình
    print("1. In ra màn hình:")
    print("Hello, Python!")

    # Cấp 2: Biến và kiểu dữ liệu
    print("\n2. Biến và kiểu dữ liệu:")
    ten = "An"  # chuỗi
    tuoi = 15   # số nguyên
    diem_tb = 8.5  # số thực
    print(f"Tên: {ten}, Tuổi: {tuoi}, Điểm: {diem_tb}")

    # Cấp 3: Nhập dữ liệu từ người dùng
    print("\n3. Nhập dữ liệu:")
    name = input("Nhập tên của bạn: ")
    print(f"Xin chào {name}!")

    # Cấp 4: Toán tử cơ bản
    print("\n4. Toán tử cơ bản:")
    a, b = 10, 3
    print(f"{a} + {b} = {a + b}")
    print(f"{a} ** {b} = {a ** b}")  # lũy thừa

    # Cấp 5: Câu lệnh điều kiện if
    print("\n5. Câu lệnh if:")
    if tuoi >= 18:
        print("Bạn đã trưởng thành.")
    else:
        print("Bạn chưa trưởng thành.")

    # Cấp 6: Câu lệnh elif
    print("\n6. Câu lệnh elif:")
    diem = 75
    if diem >= 90:
        print("Xếp loại: Xuất sắc")
    elif diem >= 70:
        print("Xếp loại: Khá")
    else:
        print("Xếp loại: Trung bình")

    # Cấp 7: Vòng lặp for
    print("\n7. Vòng lặp for:")
    for i in range(3):
        print(f"Lần lặp thứ {i+1}")

    # Cấp 8: Vòng lặp while
    print("\n8. Vòng lặp while:")
    count = 0
    while count < 3:
        print(f"Đếm: {count}")
        count += 1

    # Cấp 9: Danh sách (list)
    print("\n9. Danh sách:")
    fruits = ["táo", "chuối", "cam"]
    print("Các loại trái cây:", fruits)

    # Cấp 10: Truy cập phần tử danh sách
    print("\n10. Truy cập danh sách:")
    print("Trái cây đầu tiên:", fruits[0])

    # Cấp 11: Thêm phần tử vào danh sách
    print("\n11. Thêm phần tử:")
    fruits.append("dưa hấu")
    print("Sau khi thêm:", fruits)

    # Cấp 12: Tuple (bộ)
    print("\n12. Tuple:")
    toa_do = (10, 20)
    print("Tọa độ:", toa_do)

    # Cấp 13: Từ điển (dictionary)
    print("\n13. Từ điển:")
    sinh_vien = {"ten": "Bình", "tuoi": 20, "lop": "12A1"}
    print("Thông tin sinh viên:", sinh_vien)

    # Cấp 14: Truy cập từ điển
    print("\n14. Truy cập giá trị từ điển:")
    print("Tên sinh viên:", sinh_vien["ten"])

    # Cấp 15: Hàm đơn giản
    print("\n15. Định nghĩa hàm:")
    def xin_chao(ten):
        return f"Xin chào {ten}!"
    print(xin_chao("Lan"))

    # Cấp 16: Hàm có tham số mặc định
    print("\n16. Hàm có tham số mặc định:")
    def chao_hoi(ten, loi_chao="Xin chào"):
        return f"{loi_chao}, {ten}!"
    print(chao_hoi("Minh"))
    print(chao_hoi("Hà", "Chào bạn"))

    # Cấp 17: Xử lý ngoại lệ (try-except)
    print("\n17. Xử lý lỗi:")
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("Không thể chia cho 0!")

    # Cấp 18: Mở và ghi file
    print("\n18. Ghi file:")
    with open("hello.txt", "w", encoding="utf-8") as f:
        f.write("Xin chào từ Python!")
    print("Đã ghi file hello.txt")

    # Cấp 19: Đọc file
    print("\n19. Đọc file:")
    with open("hello.txt", "r", encoding="utf-8") as f:
        noi_dung = f.read()
    print("Nội dung file:", noi_dung)

    # Cấp 20: Import module
    print("\n20. Import module:")
    import math
    print(f"Căn bậc 2 của 16 là: {math.sqrt(16)}")

    # Cấp 21: List comprehension
    print("\n21. List comprehension:")
    binh_phuong = [x**2 for x in range(5)]
    print("Bình phương các số 0-4:", binh_phuong)

    # Cấp 22: Bài tập nhỏ
    print("\n22. BÀI TẬP NHỎ:")
    print("Viết chương trình tính tổng các số chẵn từ 1 đến 10")

    # Giải bài tập
    tong = sum([x for x in range(1, 11) if x % 2 == 0])
    print(f"Tổng các số chẵn từ 1 đến 10: {tong}")

    print("\n=== KẾT THÚC 22 CẤP CƠ BẢN ===")


# Ví dụ 1: Sử dụng hàm để kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    """Hàm kiểm tra một số có phải là số nguyên tố không"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ví dụ 2: Tìm số lớn nhất trong danh sách
def tim_so_lon_nhat(danh_sach):
    """Tìm số lớn nhất trong danh sách"""
    if not danh_sach:
        return None
    lon_nhat = danh_sach[0]
    for so in danh_sach:
        if so > lon_nhat:
            lon_nhat = so
    return lon_nhat


# Bài tập nhỏ: Viết hàm tính giai thừa
def tinh_giai_thua(n):
    """Tính giai thừa của số n"""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    ket_qua = 1
    for i in range(2, n + 1):
        ket_qua *= i
    return ket_qua


if __name__ == "__main__":
    main()

    # Chạy ví dụ
    print("\n--- VÍ DỤ THÊM ---")
    print("Số 17 có phải số nguyên tố?", kiem_tra_so_nguyen_to(17))
    print("Số lớn nhất trong [3, 7, 2, 9, 1]:", tim_so_lon_nhat([3, 7, 2, 9, 1]))
    print("5! =", tinh_giai_thua(5))

    # Bài tập cho người học
    print("\n--- BÀI TẬP CHO BẠN ---")
    print("1. Viết hàm đếm số từ trong một chuỗi.")
    print("2. Viết chương trình tìm các số chia hết cho 3 trong khoảng 1-50.")
    print("3. Tạo từ điển lưu tên và điểm, sau đó in ra học sinh có điểm cao nhất.")
```
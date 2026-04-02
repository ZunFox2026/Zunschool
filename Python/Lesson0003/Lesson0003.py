"""
Bài 3: Python Cơ bản
Nội dung: Biến, kiểu dữ liệu, toán tử, nhập/xuất dữ liệu và câu lệnh điều kiện.
"""

def main():
    # 1. Nhập dữ liệu từ bàn phím và gán vào biến
    # Lưu ý: input() luôn trả về chuỗi (str), cần ép kiểu nếu cần tính toán
    ten = input("Nhập họ và tên của bạn: ")
    tuoi = int(input("Nhập tuổi của bạn: "))
    chieu_cao = float(input("Nhập chiều cao của bạn (mét): "))
    la_hoc_sinh = True  # Kiểu boolean (True/False)

    # 2. Xuất dữ liệu ra màn hình sử dụng f-string (Python 3.6+)
    print("\n===== THÔNG TIN CÁ NHÂN =====")
    print(f"Họ tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Chiều cao: {chieu_cao} m")
    print(f"Đang đi học: {la_hoc_sinh}")

    # 3. Sử dụng toán tử số học
    print("\n===== TÍNH TOÁN CƠ BẢN =====")
    nam_sinh = 2024 - tuoi          # Phép trừ
    chieu_cao_cm = chieu_cao * 100  # Phép nhân
    print(f"Năm sinh ước tính: {nam_sinh}")
    print(f"Chiều cao quy đổi sang cm: {chieu_cao_cm:.0f} cm")  # Làm tròn 0 chữ số thập phân

    # 4. Câu lệnh điều kiện if - elif - else
    print("\n===== PHÂN LOẠI ĐỘ TUỔI =====")
    if tuoi < 18:
        print("Bạn thuộc nhóm vị thành niên.")
    elif 18 <= tuoi < 30:
        print("Bạn thuộc nhóm thanh niên.")
    elif 30 <= tuoi < 50:
        print("Bạn thuộc nhóm trung niên.")
    else:
        print("Bạn thuộc nhóm cao tuổi.")

    # 5. Toán tử so sánh và logic (and, or, not)
    print("\n===== KIỂM TRA ĐIỀU KIỆN =====")
    # Kiểm tra đồng thời hai điều kiện
    if tuoi >= 18 and chieu_cao >= 1.5:
        print("Bạn đủ điều kiện tham gia chương trình.")
    else:
        print("Bạn chưa đủ điều kiện tham gia chương trình.")

    # 6. Ví dụ toán tử chia lấy nguyên (//) và chia lấy dư (%)
    print("\n===== TOÁN TỬ ĐẶC BIỆT =====")
    so_ngay = 100
    so_tuan = so_ngay // 7  # Chia lấy nguyên
    so_du = so_ngay % 7     # Chia lấy dư
    print(f"{so_ngay} ngày tương đương {so_tuan} tuần và {so_du} ngày.")

# Khối lệnh chính để chạy chương trình
if __name__ == "__main__":
    main()
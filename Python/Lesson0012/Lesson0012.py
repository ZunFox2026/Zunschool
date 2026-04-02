# -*- coding: utf-8 -*-
"""
Bài 12: Python Cơ bản
Mô tả: File minh hoá một số kiến thức cơ bản của Python như:
    - Biến, kiểu dữ liệu
    - Nhập/xuất
    - Cấu trúc điều kiện và vòng lặp
    - Hàm
    - List, tuple, dict
    - Xử lý file đơn giản
Mỗi phần được bao trong hàm riêng để dễ đọc và kiểm tra.
"""

def chao_hoi():
    """Yêu cầu người dùng nhập tên và in ra lời chào."""
    ten = input("Nhập tên của bạn: ").strip()
    print(f"Xin chào, {ten}! Chúc bạn học Python vui vẻ.\n")


def phep_toan_co_ban():
    """Thực hiện một số phép toán cơ bản và in kết quả."""
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    if b != 0:
        print(f"a / b = {a / b}")
    else:
        print("Không thể chia cho 0.")
    print(f"a // b (chia lấy phần nguyên) = {a // b if b != 0 else 'không xác định'}")
    print(f"a % b (chia lấy dư) = {a % b if b != 0 else 'không xác定'}\n")


def kiem_tra_so_nguyen_to(n: int) -> bool:
    """Kiểm tra xem n có phải là số nguyên tố hay không."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def demo_so_nguyen_to():
    """Nhập một số và kiểm tra xem đó có phải số nguyên tố không."""
    try:
        so = int(input("Nhập một số nguyên để kiểm tra nguyên tố: "))
    except ValueError:
        print("Giá trị nhập không phải là số nguyên.\n")
        return
    if kiem_tra_so_nguyen_to(so):
        print(f"{so} là số nguyên tố.\n")
    else:
        print(f"{so} không phải là số nguyên tố.\n")


def in_bang_cuu_chuong(n: int):
    """In bảng cửu chương của n (từ 1 đến 10)."""
    print(f"Bảng cửu chương của {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()  # dòng trống


def xu_ly_list():
    """Minh hoá một số thao tác cơ bản với list."""
    print("--- Thao tác với list ---")
    # Tạo list từ nhập người dùng
    raw = input("Nhập các số cách nhau bằng dấu cách (ví dụ: 3 5 2 8): ")
    try:
        lst = [int(x) for x in raw.split()]
    except ValueError:
        print("Có giá trị không phải số nguyên. Sử dụng list mặc định [1,2,].
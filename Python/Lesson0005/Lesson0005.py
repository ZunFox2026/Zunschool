# -*- coding: utf-8 -*-
"""
Bài 5: Python Cơ bản
Minh hoạ một số khái niệm cơ bản:
- Biến và kiểu dữ liệu
- Nhập/xuất
- Câu lệnh điều kiện
- Vòng lặp
- Hàm
"""

def tinh_tong_chu_so(n: int) -> int:
    """
    Hàm tính tổng các chữ số của một số nguyên dương n.
    """
    tong = 0
    while n > 0:
        tong += n % 10   # Lấy chữ số cuối cùng
        n //= 10         # Loại bỏ chữ số cuối cùng
    return tong

def kiem_tra_so_nguyen_to(n: int) -> bool:
    """
    Kiểm tra xem n có phải là số nguyên tố hay không.
    Trả về True nếu là số nguyên tố, ngược lại False.
    """
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

def main() -> None:
    """
    Hàm chính thực hiện luồng chương trình:
    1. Nhập một số nguyên từ người dùng.
    2. In ra tổng các chữ số của số đó.
    3. Kiểm tra và in ra xem số đó có phải là số nguyên tố không.
    """
    try:
        so = int(input("Nhập vào một số nguyên dương: "))
        if so <= 0:
            print("Vui lòng nhập số nguyên dương lớn hơn 0.")
            return
    except ValueError:
        print("Giá trị nhập vào không phải là số nguyên. Vui lòng thử lại.")
        return

    # Tính tổng các chữ số
    tong_chu_so = tinh_tong_chu_so(so)
    print(f"Tổng các chữ số của {so} là: {tong_chu_so}")

    # Kiểm tra số nguyên tố
    if kiem_tra_so_nguyen_to(so):
        print(f"{so} là số nguyên tố.")
    else:
        print(f"{so} không phải là số nguyên tố.")

if __name__ == "__main__":
    main()
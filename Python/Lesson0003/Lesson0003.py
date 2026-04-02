# -*- coding: utf-8 -*-
"""
Bài 3 - Cấp Cơ bản
Chương trình đơn giản: đọc hai số nguyên từ вход và in ra tổng của chúng.
"""

def solve() -> None:
    """
    Đọc đầu vào, tính tổng hai số và in kết quả.
    Định dạng đầu vào (theo đề bài phổ biến):
        a b
    où a và b là hai số nguyên cách nhau bởi khoảng trắng.
    """
    try:
        # Đọc một dòng từ stdin, loại bỏ ký tự newline và khoảng trắng thừa
        line = input().strip()
        if not line:
            # Nếu dòng trống, không làm gì
            return
        # Tách chuỗi thành các thành phần và chuyển đổi sang int
        a_str, b_str = line.split()
        a = int(a_str)
        b = int(b_str)
    except ValueError:
        # Nếu đầu vào không đúng định dạng, thông báo lỗi và thoát
        print("Đầu vào không hợp lệ. Vui lòng nhập hai số nguyên cách nhau bởi khoảng trắng.")
        return

    # Tính tổng và in ra kết quả
    tong = a + b
    print(tong)


if __name__ == "__main__":
    # Khi script được chạy trực tiếp, gọi hàm solve()
    solve()
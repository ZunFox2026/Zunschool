def kiem_tra_nguyen_to(n):
    # Kiểm tra số nguyên tố
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to():
    # Nhập số từ người dùng
    n = int(input("Nhập số cần kiểm tra: "))
    
    # Kiểm tra số nguyên tố
    if kiem_tra_nguyen_to(n):
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không là số nguyên tố")

# Chạy chương trình
tim_so_nguyen_to()
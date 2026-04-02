def kiem_tra_so_nguyen_to(n):
    # Kiểm tra số nguyên tố
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to():
    # Nhập số từ bàn phím
    so = int(input("Nhập số: "))
    
    # Kiểm tra số nguyên tố
    if kiem_tra_so_nguyen_to(so):
        print(f"{so} là số nguyên tố")
    else:
        print(f"{so} không là số nguyên tố")

# Chạy chương trình
tim_so_nguyen_to()
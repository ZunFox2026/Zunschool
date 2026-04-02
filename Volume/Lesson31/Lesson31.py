def kiem_tra_so_nguyen_to(n):
    # Hàm kiểm tra số nguyên tố
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        # Chỉ cần kiểm tra đến căn bậc hai của số
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to():
    # Hàm tìm số nguyên tố
    so_can_kiem_tra = int(input("Nhập số cần kiểm tra: "))
    if kiem_tra_so_nguyen_to(so_can_kiem_tra):
        print(f"{so_can_kiem_tra} là số nguyên tố")
    else:
        print(f"{so_can_kiem_tra} không là số nguyên tố")

# Gọi hàm tìm số nguyên tố
tim_so_nguyen_to()
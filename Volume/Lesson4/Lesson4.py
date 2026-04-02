def tinh_tong(n):
    # Hàm tính tổng các số từ 1 đến n
    tong = 0
    for i in range(1, n+1):
        tong += i
    return tong

# Ví dụ sử dụng hàm tinh_tong
n = 10
ket_qua = tinh_tong(n)
print(f'Tổng các số từ 1 đến {n} là: {ket_qua}')

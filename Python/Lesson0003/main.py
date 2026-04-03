import random

# Ví dụ 1: In các số chẵn từ 0 đến 10
print("=== Ví dụ 1: In các số chẵn từ 0 đến 10 ===")
for i in range(0, 11, 2):  # Bắt đầu từ 0, kết thúc trước 11, bước nhảy 2
    print(i)

# Ví dụ 2: Đoán số (sử dụng while)
print("\n=== Ví dụ 2: Đoán số từ 1 đến 10 ===")
so_bi_mat = random.randint(1, 10)
print("Tôi đã chọn một số từ 1 đến 10. Hãy đoán xem là số nào!")

doan = 0
while doan != so_bi_mat:
    doan = int(input("Hãy đoán số: "))
    if doan < so_bi_mat:
        print("Quá nhỏ! Thử lại nào.")
    elif doan > so_bi_mat:
        print("Quá lớn! Thử lại nào.")
    else:
        print("Chính xác! Bạn đã đoán đúng!")

# Ví dụ 3: In từng ký tự trong chuỗi
print("\n=== Ví dụ 3: In từng ký tự trong chuỗi 'Python' ===")
chuoi = "Python"
for ky_tu in chuoi:
    print(ky_tu)

# In một dòng phân cách cuối
print("\n--- Kết thúc ví dụ ---")
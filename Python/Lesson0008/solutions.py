# solutions.py - Lời giải Bài 8: try-except

# Bài 1: Nhập tuổi
# Xử lý khi người dùng nhập không phải số hoặc tuổi âm

def bai1():
    try:
        tuoi = int(input("Nhập tuổi của bạn: "))
        if tuoi < 0:
            print("Lỗi: Tuổi không thể là số âm!")
        else:
            print(f"Tuổi của bạn là: {tuoi}")
    except ValueError:
        print("Lỗi: Bạn phải nhập một số nguyên!")

# Bài 2: Tính trung bình cộng
# Nhập hai số và tính trung bình, xử lý lỗi nhập sai

def bai2():
    try:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        trung_binh = (a + b) / 2
        print(f"Trung bình cộng: {trung_binh}")
    except ValueError:
        print("Lỗi: Bạn phải nhập số hợp lệ!")

# Bài 3: Truy cập từ điển
# Người dùng nhập khóa, truy cập giá trị trong từ điển
# Nếu khóa không tồn tại -> báo lỗi

def bai3():
    tu_dien = {"ten": "An", "tuoi": 20, "lop": "K12"}
    try:
        khoa = input("Nhập khóa (ten/tuoi/lop): ")
        print(f"Giá trị: {tu_dien[khoa]}")
    except KeyError:
        print("Lỗi: Khóa không tồn tại trong từ điển!")

# Bài 4: Tính căn bậc hai
# Tính căn bậc hai của một số, báo lỗi nếu số âm

def bai4():
    try:
        so = float(input("Nhập một số: "))
        if so < 0:
            print("Lỗi: Không thể tính căn bậc hai của số âm!")
        else:
            can_bac_hai = so ** 0.5
            print(f"Căn bậc hai của {so} là: {can_bac_hai}")
    except ValueError:
        print("Lỗi: Bạn phải nhập một số hợp lệ!")

# Bài 5: Rút thăm trúng thưởng
# Rút ngẫu nhiên một phần thưởng từ danh sách
# Xử lý nếu danh sách rỗng (dù ở đây không rỗng, nhưng minh họa cách xử lý)

def bai5():
    import random
    phan_thuong = ["Túi xách", "Sách", "Bút", "Áo thun"]
    try:
        if len(phan_thuong) == 0:
            raise IndexError("Danh sách phần thưởng rỗng!")
        thuong = random.choice(phan_thuong)
        print(f"Chúc mừng! Bạn nhận được: {thuong}")
    except IndexError as e:
        print(f"Lỗi: {e}")

# Gọi các hàm để kiểm tra
# Bạn có thể bỏ comment từng dòng để chạy thử
# bai1()
# bai2()
# bai3()
# bai4()
# bai5()
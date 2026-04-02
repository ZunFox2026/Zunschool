# Bài 73: Lập Trình Cơ Bản

# Hàm in ra màn hình
def in_man_hinh():
    print("Xin chào, lập trình cơ bản!")

# Hàm nhập từ bàn phím
def nhap_tu_ban_phim():
    ten = input("Nhập tên của bạn: ")
    print("Xin chào, " + ten + "!")

# Hàm thực hiện phép tính cơ bản
def phep_tinh_co_ban():
    so1 = float(input("Nhập số thứ nhất: "))
    so2 = float(input("Nhập số thứ hai: "))
    print("Tổng: ", so1 + so2)
    print("Hiệu: ", so1 - so2)
    print("Tích: ", so1 * so2)
    if so2 != 0:
        print("Thương: ", so1 / so2)

# Hàm chính
def main():
    print("Lập Trình Cơ Bản")
    in_man_hinh()
    nhap_tu_ban_phim()
    phep_tinh_co_ban()

# Chạy chương trình
if __name__ == "__main__":
    main()
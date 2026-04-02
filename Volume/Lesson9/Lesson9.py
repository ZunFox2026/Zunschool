# Mở tệp tin để đọc
def doc_tep():
    # Mở tệp tin với quyền đọc
    f = open("test.txt", "r")
    # Đọc nội dung tệp tin
    print(f.read())
    # Đóng tệp tin
    f.close()

# Mở tệp tin để ghi
def ghi_tep():
    # Mở tệp tin với quyền ghi
    f = open("test.txt", "w")
    # Ghi nội dung vào tệp tin
    f.write("Xin chào, thế giới!")
    # Đóng tệp tin
    f.close()

# Mở tệp tin để thêm nội dung
def them_tep():
    # Mở tệp tin với quyền thêm
    f = open("test.txt", "a")
    # Thêm nội dung vào tệp tin
    f.write("\nNội dung mới!")
    # Đóng tệp tin
    f.close()

# Kiểm tra sự tồn tại của tệp tin
import os
def kiem_tra_ton_tai():
    if os.path.exists("test.txt"):
        print("Tệp tin tồn tại!")
    else:
        print("Tệp tin không tồn tại!")

# Xóa tệp tin
def xoa_tep():
    if os.path.exists("test.txt"):
        os.remove("test.txt")
        print("Tệp tin đã được xóa!")
    else:
        print("Tệp tin không tồn tại!")

# Minh họa các chức năng
if __name__ == "__main__":
    ghi_tep()
    doc_tep()
    them_tep()
    doc_tep()
    kiem_tra_ton_tai()
    xoa_tep()
    kiem_tra_ton_tai()
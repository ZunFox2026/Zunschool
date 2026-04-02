# Mở tệp tin để đọc
def doc tep():
    try:
        # Mở tệp tin với quyền đọc
        f = open("test.txt", "r")
        # Đọc nội dung tệp tin
        content = f.read()
        # In nội dung tệp tin
        print(content)
    except FileNotFoundError:
        print("Tệp tin không tồn tại")
    finally:
        # Đóng tệp tin
        f.close()

# Mở tệp tin để ghi
def ghi tep():
    try:
        # Mở tệp tin với quyền ghi
        f = open("test.txt", "w")
        # Ghi nội dung vào tệp tin
        f.write("Xin chào thế giới!")
    except Exception as e:
        print("Lỗi khi ghi tệp tin: ", str(e))
    finally:
        # Đóng tệp tin
        f.close()

# Mở tệp tin để thêm nội dung
def them_noi_dung():
    try:
        # Mở tệp tin với quyền thêm
        f = open("test.txt", "a")
        # Thêm nội dung vào tệp tin
        f.write("\nĐây là nội dung thêm vào")
    except Exception as e:
        print("Lỗi khi thêm nội dung: ", str(e))
    finally:
        # Đóng tệp tin
        f.close()

# Chương trình chính
if __name__ == "__main__":
    # Đọc tệp tin
    doc_tep()
    # Ghi tệp tin
    ghi_tep()
    # Thêm nội dung vào tệp tin
    them_noi_dung()
    # Đọc lại tệp tin sau khi thêm nội dung
    doc_tep()
# Bài 5: Làm việc với tệp

# Mở tệp và đọc nội dung
def doc_tep(ten_tep):
    try:
        # Mở tệp ở chế độ đọc
        f = open(ten_tep, 'r')
        # Đọc nội dung tệp
        noi_dung = f.read()
        # Đóng tệp
        f.close()
        return noi_dung
    except FileNotFoundError:
        print("Tệp không tồn tại")
        return None

# Ghi nội dung vào tệp
def ghi_tep(ten_tep, noi_dung):
    try:
        # Mở tệp ở chế độ ghi
        f = open(ten_tep, 'w')
        # Ghi nội dung vào tệp
        f.write(noi_dung)
        # Đóng tệp
        f.close()
    except Exception as e:
        print("Lỗi khi ghi tệp: ", str(e))

# Chương trình chính
def main():
    ten_tep = 'test.txt'
    noi_dung = 'Xin chào, thế giới!'
    
    # Ghi nội dung vào tệp
    ghi_tep(ten_tep, noi_dung)
    
    # Đọc nội dung từ tệp
    noi_dung_doc = doc_tep(ten_tep)
    
    # In nội dung
    if noi_dung_doc is not None:
        print("Nội dung tệp: ", noi_dung_doc)

if __name__ == "__main__":
    main()
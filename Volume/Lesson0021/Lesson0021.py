# Mở tệp tin và đọc nội dung
def doc_tep_tin(ten_tep):
    try:
        # Mở tệp tin ở chế độ đọc
        f = open(ten_tep, 'r')
        # Đọc nội dung tệp tin
        noi_dung = f.read()
        # Đóng tệp tin
        f.close()
        return noi_dung
    except FileNotFoundError:
        print("Tệp tin không tồn tại")
        return None

# Mở tệp tin và ghi nội dung
def ghi_tep_tin(ten_tep, noi_dung):
    try:
        # Mở tệp tin ở chế độ ghi
        f = open(ten_tep, 'w')
        # Ghi nội dung vào tệp tin
        f.write(noi_dung)
        # Đóng tệp tin
        f.close()
    except Exception as e:
        print("Lỗi khi ghi tệp tin: ", str(e))

# Chương trình chính
if __name__ == "__main__":
    # Ghi nội dung vào tệp tin
    ten_tep = "test.txt"
    noi_dung = "Xin chào, thế giới!"
    ghi_tep_tin(ten_tep, noi_dung)
    
    # Đọc nội dung từ tệp tin
    print("Nội dung tệp tin:")
    noi_dung_doc = doc_tep_tin(ten_tep)
    if noi_dung_doc is not None:
        print(noi_dung_doc)
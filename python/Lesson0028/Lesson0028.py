# Bài 28: Làm việc với tệp tin
# Mở tệp tin và đọc nội dung
def doc_tepp_tin(ten_tep):
    try:
        # Mở tệp tin ở chế độ đọc
        f = open(ten_tep, 'r', encoding='utf-8')
        # Đọc nội dung tệp tin
        noi_dung = f.read()
        # Đóng tệp tin
        f.close()
        return noi_dung
    except FileNotFoundError:
        print("Tệp tin không tồn tại")
        return None

# Mở tệp tin và ghi nội dung
def ghi_tepp_tin(ten_tep, noi_dung):
    try:
        # Mở tệp tin ở chế độ ghi
        f = open(ten_tep, 'w', encoding='utf-8')
        # Ghi nội dung vào tệp tin
        f.write(noi_dung)
        # Đóng tệp tin
        f.close()
    except Exception as e:
        print("Lỗi khi ghi tệp tin: ", str(e))

# Đọc và ghi tệp tin
ten_tep = 'example.txt'
noi_dung = "Xin chào, thế giới!"
ghi_tepp_tin(ten_tep, noi_dung)
print("Nội dung tệp tin:")
print(doc_tepp_tin(ten_tep))
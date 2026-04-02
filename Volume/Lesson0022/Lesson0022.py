# Mở tệp tin và đọc nội dung
def doc_tep():
    # Mở tệp tin với chế độ đọc (r)
    f = open("test.txt", "r")
    
    # Đọc nội dung tệp tin
    noi_dung = f.read()
    
    # In nội dung tệp tin
    print(noi_dung)
    
    # Đóng tệp tin
    f.close()

# Mở tệp tin và ghi nội dung
def ghi_tep():
    # Mở tệp tin với chế độ ghi (w)
    f = open("test.txt", "w")
    
    # Ghi nội dung vào tệp tin
    f.write("Xin chào, thế giới!")
    
    # Đóng tệp tin
    f.close()

# Mở tệp tin và thêm nội dung
def them_tep():
    # Mở tệp tin với chế độ thêm (a)
    f = open("test.txt", "a")
    
    # Thêm nội dung vào tệp tin
    f.write("\nTôi là lập trình viên Python!")
    
    # Đóng tệp tin
    f.close()

# Gọi hàm để chạy
doc_tep()
ghi_tep()
them_tep()
doc_tep()
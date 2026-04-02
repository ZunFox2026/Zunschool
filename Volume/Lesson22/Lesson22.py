# Mở tệp tin để đọc
def doc_tep():
    # Mở tệp tin 'example.txt' ở chế độ đọc
    f = open('example.txt', 'r')
    
    # Đọc nội dung tệp tin
    noi_dung = f.read()
    
    # In nội dung tệp tin
    print(noi_dung)
    
    # Đóng tệp tin
    f.close()

# Mở tệp tin để ghi
def ghi_tep():
    # Mở tệp tin 'example.txt' ở chế độ ghi
    f = open('example.txt', 'w')
    
    # Ghi nội dung vào tệp tin
    f.write('Xin chào, thế giới!')
    
    # Đóng tệp tin
    f.close()

# Mở tệp tin để thêm nội dung
def them_noi_dung():
    # Mở tệp tin 'example.txt' ở chế độ thêm
    f = open('example.txt', 'a')
    
    # Thêm nội dung vào tệp tin
    f.write('\nĐây là nội dung được thêm vào.')
    
    # Đóng tệp tin
    f.close()

# Chương trình chính
def main():
    # Tạo tệp tin 'example.txt' nếu không tồn tại
    try:
        open('example.txt', 'r')
    except FileNotFoundError:
        open('example.txt', 'w').close()
    
    # Đọc tệp tin
    print("Đọc tệp tin:")
    doc_tep()
    
    # Ghi tệp tin
    print("\nGhi tệp tin:")
    ghi_tep()
    doc_tep()
    
    # Thêm nội dung vào tệp tin
    print("\nThếm nội dung vào tệp tin:")
    them_noi_dung()
    doc_tep()

if __name__ == "__main__":
    main()
# Mở file và đọc nội dung
def doc_noi_dung_file(ten_file):
    try:
        # Mở file ở chế độ đọc
        with open(ten_file, 'r', encoding='utf-8') as file:
            # Đọc nội dung file
            noi_dung = file.read()
            return noi_dung
    except FileNotFoundError:
        print("File không tồn tại")
        return None

# Ghi nội dung vào file
def ghi_noi_dung_vao_file(ten_file, noi_dung):
    try:
        # Mở file ở chế độ ghi
        with open(ten_file, 'w', encoding='utf-8') as file:
            # Ghi nội dung vào file
            file.write(noi_dung)
    except Exception as e:
        print("Lỗi khi ghi file:", str(e))

# Chương trình chính
def main():
    ten_file = 'example.txt'
    noi_dung = "Xin chào, thế giới!"

    # Ghi nội dung vào file
    ghi_noi_dung_vao_file(ten_file, noi_dung)

    # Đọc và in nội dung file
    noi_dung_doc = doc_noi_dung_file(ten_file)
    if noi_dung_doc:
        print("Nội dung file:", noi_dung_doc)

if __name__ == "__main__":
    main()
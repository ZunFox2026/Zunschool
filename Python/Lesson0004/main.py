def chao_ten(ten):
    """
    Hàm in lời chào với tên được truyền vào
    """
    print(f"Chào bạn {ten}! Rất vui được gặp bạn.")

# Gọi hàm với đối số
chao_ten("Lan")
chao_ten("Minh")


def tinh_dien_tich(chieu_dai, chieu_rong):
    """
    Hàm tính diện tích hình chữ nhật
    Trả về diện tích
    """
    dien_tich = chieu_dai * chieu_rong
    return dien_tich

# Gọi hàm và in kết quả
dien_tich = tinh_dien_tich(10, 5)
print(f"Diện tích hình chữ nhật: {dien_tich}")


def kiem_tra_chan_le(so):
    """
    Hàm kiểm tra một số là chẵn hay lẻ
    Trả về chuỗi "chẵn" hoặc "lẻ"
    """
    if so % 2 == 0:
        return "chẵn"
    else:
        return "lẻ"

# Gọi hàm và in kết quả
print(kiem_tra_chan_le(7))
print(kiem_tra_chan_le(4))

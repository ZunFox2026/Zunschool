# Bài 45: Python Cơ bản
# Chương trình quản lý điểm học sinh minh họa các khái niệm cơ bản:
# biến, kiểu dữ liệu, nhập xuất, điều kiện, vòng lặp, hàm, danh sách và xử lý lỗi cơ bản.

def nhap_diem():
    """Hàm nhập danh sách điểm môn học từ bàn phím."""
    diem = []
    print("Nhập điểm các môn học (nhập 'xong' để kết thúc):")
    while True:
        mon = input("Tên môn học: ")
        if mon.lower() == 'xong':
            break
        try:
            diem_mon = float(input(f"  Điểm môn {mon}: "))
            if 0 <= diem_mon <= 10:
                diem.append(diem_mon)
            else:
                print("  ⚠️ Điểm phải nằm trong khoảng 0 - 10. Vui lòng nhập lại!")
        except ValueError:
            print("  ⚠️ Vui lòng nhập số hợp lệ!")
    return diem

def tinh_trung_binh(danh_sach_diem):
    """Hàm tính điểm trung bình từ danh sách điểm."""
    if not danh_sach_diem:
        return 0.0
    return sum(danh_sach_diem) / len(danh_sach_diem)

def xep_loai_hoc_luc(diem_tb):
    """Hàm xếp loại học lực dựa trên điểm trung bình."""
    if diem_tb >= 8.0:
        return "Giỏi"
    elif diem_tb >= 6.5:
        return "Khá"
    elif diem_tb >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def hien_thi_ket_qua(ho_ten, diem_tb, xep_loai):
    """Hàm hiển thị kết quả ra màn hình."""
    print("\n" + "=" * 35)
    print(f"👤 Họ tên       : {ho_ten}")
    print(f"📊 Điểm trung bình: {diem_tb:.2f}")
    print(f"🏅 Xếp loại     : {xep_loai}")
    print("=" * 35)

def main():
    """Hàm chính điều khiển luồng chương trình."""
    print("🐍 Bài 45: Python Cơ bản - Quản lý điểm học sinh")
    ho_ten = input("Nhập họ tên học sinh: ").strip()

    if not ho_ten:
        print("⚠️ Bạn chưa nhập tên! Chương trình kết thúc.")
        return

    ds_diem = nhap_diem()

    if not ds_diem:
        print("⚠️ Không có điểm nào được nhập! Chương trình kết thúc.")
        return

    dtb = tinh_trung_binh(ds_diem)
    loai = xep_loai_hoc_luc(dtb)

    hien_thi_ket_qua(ho_ten, dtb, loai)

    # Minh họa thêm về vòng lặp và chỉ số (enumerate)
    print("\n📝 Chi tiết điểm từng môn:")
    for i, d in enumerate(ds_diem, start=1):
        print(f"  - Môn {i}: {d:.1f}")

# Kiểm tra xem file có được chạy trực tiếp hay không
if __name__ == "__main__":
    main()
# Bài 39: Python Cơ bản
# Chương trình quản lý và thống kê điểm học sinh đơn giản

def nhap_thong_tin_hoc_sinh():
    """Nhập tên và điểm của một học sinh với kiểm tra dữ liệu đầu vào."""
    ten = input("Nhập tên học sinh: ").strip()
    while True:
        try:
            diem = float(input("Nhập điểm số (0-10): "))
            if 0 <= diem <= 10:
                break
            print("⚠️ Điểm phải nằm trong khoảng từ 0 đến 10.")
        except ValueError:
            print("⚠️ Vui lòng nhập một số hợp lệ.")
    return {"ten": ten, "diem": diem}


def tinh_diem_trung_binh(danh_sach_hoc_sinh):
    """Tính điểm trung bình của toàn danh sách."""
    if not danh_sach_hoc_sinh:
        return 0.0
    tong_diem = sum(hs["diem"] for hs in danh_sach_hoc_sinh)
    return tong_diem / len(danh_sach_hoc_sinh)


def xep_loai_hoc_luc(diem):
    """Xếp loại học lực dựa trên điểm số theo thang điểm 10."""
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"


def hien_thi_danh_sach(danh_sach_hoc_sinh):
    """In danh sách học sinh kèm điểm và xếp loại dưới dạng bảng."""
    if not danh_sach_hoc_sinh:
        print("📭 Danh sách hiện đang trống.")
        return
    # Định dạng bảng cho thẳng hàng
    tieu_de = "{:<20} {:<10} {:<10}".format("Tên học sinh", "Điểm", "Xếp loại")
    print(f"\n📋 {tieu_de}")
    print("-" * 45)
    for hs in danh_sach_hoc_sinh:
        loai = xep_loai_hoc_luc(hs["diem"])
        dong = "{:<20} {:<10.1f} {:<10}".format(hs["ten"], hs["diem"], loai)
        print(dong)


def main():
    """Hàm chính chứa vòng lặp điều khiển chương trình."""
    danh_sach = []
    print("=" * 45)
    print("🎓 CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM HỌC SINH")
    print("=" * 45)

    while True:
        print("\n--- MENU LỰA CHỌN ---")
        print("1. Thêm học sinh mới")
        print("2. Hiển thị danh sách")
        print("3. Tính điểm trung bình lớp")
        print("4. Thoát chương trình")

        lua_chon = input("👉 Nhập lựa chọn (1-4): ").strip()

        if lua_chon == "1":
            hs_moi = nhap_thong_tin_hoc_sinh()
            danh_sach.append(hs_moi)
            print(f"✅ Đã lưu thành công: {hs_moi['ten']}")

        elif lua_chon == "2":
            hien_thi_danh_sach(danh_sach)

        elif lua_chon == "3":
            diem_tb = tinh_diem_trung_binh(danh_sach)
            print(f"📊 Điểm trung bình cả lớp: {diem_tb:.2f}")

        elif lua_chon == "4":
            print("👋 Hẹn gặp lại! Chương trình kết thúc.")
            break

        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 4.")


# Điểm vào chương trình chính
if __name__ == "__main__":
    main()
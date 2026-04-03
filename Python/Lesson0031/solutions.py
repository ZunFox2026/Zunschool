import json

# Bài tập 1: Tạo và lưu cấu hình ứng dụng
def luu_cau_hinh():
    cau_hinh = {
        "giao_dien": "sáng",
        "am_thanh": 80,
        "nhan_dang_khuon_mat": True,
        "nguoi_dung_gan_nhat": "Nguyen Van A"
    }
    # Ghi cấu hình vào file JSON
    with open("cau_hinh.json", "w", encoding="utf-8") as f:
        json.dump(cau_hinh, f, ensure_ascii=False, indent=4)
    print("Đã lưu cấu hình vào file 'cau_hinh.json'")

# Bài tập 2: Đọc và kiểm tra dữ liệu JSON
def kiem_tra_du_lieu():
    with open("sinh_vien.json", "r", encoding="utf-8") as f:
        ds_sv = json.load(f)
    
    # Kiểm tra sinh viên có điểm dưới 5
    sinh_vien_yeu = [sv for sv in ds_sv if sv["diem"] < 5]
    
    if sinh_vien_yeu:
        print("Các sinh viên có điểm dưới 5:")
        for sv in sinh_vien_yeu:
            print(f"- {sv['ten']}: {sv['diem']}")
    else:
        print("Không có sinh viên nào có điểm dưới 5.")

# Bài tập 3: Cập nhật điểm sinh viên
def cap_nhat_diem(ma_sv, diem_moi):
    with open("sinh_vien.json", "r", encoding="utf-8") as f:
        ds_sv = json.load(f)
    
    tim_thay = False
    for sv in ds_sv:
        if sv["ma"] == ma_sv:
            print(f"Cập nhật điểm sinh viên {sv['ten']}: {sv['diem']} -> {diem_moi}")
            sv["diem"] = diem_moi
            tim_thay = True
            break
    
    if not tim_thay:
        print(f"Không tìm thấy sinh viên có mã {ma_sv}")
        return
    
    # Ghi lại danh sách đã cập nhật
    with open("sinh_vien.json", "w", encoding="utf-8") as f:
        json.dump(ds_sv, f, ensure_ascii=False, indent=4)

# Bài tập 4: Tạo báo cáo JSON
def tao_bao_cao():
    with open("sinh_vien.json", "r", encoding="utf-8") as f:
        ds_sv = json.load(f)
    
    tong_so_sv = len(ds_sv)
    diem_trung_binh = sum(sv["diem"] for sv in ds_sv) / tong_so_sv
    so_sv_gioi = sum(1 for sv in ds_sv if sv["diem"] >= 8.0)
    
    bao_cao = {
        "tong_so_sv": tong_so_sv,
        "diem_trung_binh": round(diem_trung_binh, 2),
        "so_sv_gioi": so_sv_gioi
    }
    
    with open("bao_cao.json", "w", encoding="utf-8") as f:
        json.dump(bao_cao, f, ensure_ascii=False, indent=4)
    
    print("Đã tạo báo cáo vào file 'bao_cao.json'")

# Gọi các hàm để kiểm tra
if __name__ == "__main__":
    luu_cau_hinh()
    kiem_tra_du_lieu()
    cap_nhat_diem("SV002", 8.8)
    tao_bao_cao()
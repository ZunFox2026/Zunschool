import json

# Ví dụ 1: Chuyển đổi dữ liệu Python sang JSON và ngược lại

data = {
    "ten": "Nguyen Van A",
    "tuoi": 25,
    "dia_chi": {
        "tinh": "Hà Nội",
        "quan": "Cầu Giấy"
    },
    "so_thich": ["đọc sách", "lập trình", "đi bộ"]
}

# Chuyển đối tượng Python thành chuỗi JSON
json_string = json.dumps(data, ensure_ascii=False, indent=4)
print("Dữ liệu dưới dạng JSON:")
print(json_string)

# Chuyển ngược từ JSON về đối tượng Python
python_obj = json.loads(json_string)
print("\nDữ liệu Python sau khi chuyển lại:")
print(python_obj)

# Ví dụ 2: Ghi dữ liệu ra file JSON
with open("nguoi_dung.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("\nĐã ghi dữ liệu vào file 'nguoi_dung.json'")

# Ví dụ 3: Đọc dữ liệu từ file JSON
with open("nguoi_dung.json", "r", encoding="utf-8") as f:
    du_lieu_doc = json.load(f)

print("\nDữ liệu đọc từ file:")
print(du_lieu_doc)

# Ví dụ 4: Ứng dụng thực tế - Quản lý danh sách sinh viên
sinh_vien = [
    {"ma": "SV001", "ten": "Tran Thi B", "diem": 8.5},
    {"ma": "SV002", "ten": "Le Van C", "diem": 7.2},
    {"ma": "SV003", "ten": "Pham Thi D", "diem": 9.0}
]

# Lưu danh sách sinh viên vào file
with open("sinh_vien.json", "w", encoding="utf-8") as f:
    json.dump(sinh_vien, f, ensure_ascii=False, indent=4)

# Đọc và xử lý dữ liệu
with open("sinh_vien.json", "r", encoding="utf-8") as f:
    ds_sv = json.load(f)

print("\nDanh sách sinh viên:")
for sv in ds_sv:
    print(f"- {sv['ten']} (Mã: {sv['ma']}) - Điểm: {sv['diem']}")

# Tìm sinh viên có điểm cao nhất
sv_gioi_nhat = max(ds_sv, key=lambda x: x['diem'])
print(f"\nSinh viên xuất sắc nhất: {sv_gioi_nhat['ten']} với {sv_gioi_nhat['diem']} điểm")
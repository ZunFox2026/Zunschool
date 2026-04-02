"""
Bài 46: Thao tác cơ bản với List trong Python
Cấp độ: Cơ bản
"""

def main():
    # 1. Khởi tạo danh sách (List)
    print("=== 1. Khởi tạo List ===")
    ds_trong = []  # Danh sách rỗng
    ds_so = [10, 20, 30, 40, 50]
    ds_hon_hop = ["Python", 3.14, True, [1, 2]]  # Hỗ trợ nhiều kiểu dữ liệu
    print(f"Danh sách rỗng: {ds_trong}")
    print(f"Danh sách số: {ds_so}")
    print(f"Danh sách hỗn hợp: {ds_hon_hop}")

    # 2. Truy cập phần tử (Indexing & Slicing)
    print("\n=== 2. Truy cập phần tử ===")
    print(f"Phần tử đầu tiên: {ds_so[0]}")
    print(f"Phần tử cuối cùng (index âm): {ds_so[-1]}")
    print(f"Cắt từ index 1 đến 3 (loại trừ 4): {ds_so[1:4]}")
    print(f"Lấy 3 phần tử cuối cùng: {ds_so[-3:]}")
    print(f"Lấy toàn bộ nhưng đảo ngược: {ds_so[::-1]}")

    # 3. Thêm phần tử
    print("\n=== 3. Thêm phần tử ===")
    ds_so.append(60)  # Thêm vào cuối danh sách
    print(f"Sau append(60): {ds_so}")
    ds_so.insert(0, 5)  # Thêm vào vị trí index 0, đẩy các phần tử khác sang phải
    print(f"Sau insert(0, 5): {ds_so}")
    ds_so.extend([70, 80])  # Nối thêm iterable (list khác) vào cuối
    print(f"Sau extend([70, 80]): {ds_so}")

    # 4. Sửa phần tử
    print("\n=== 4. Sửa phần tử ===")
    ds_so[0] = 99  # Gán giá trị mới cho index cụ thể
    print(f"Sau gán ds_so[0] = 99: {ds_so}")
    ds_so[1:3] = [11, 22]  # Sửa nhiều phần tử liên tiếp bằng slicing
    print(f"Sau gán ds_so[1:3] = [11, 22]: {ds_so}")

    # 5. Xóa phần tử
    print("\n=== 5. Xóa phần tử ===")
    ds_so.remove(11)  # Xóa theo giá trị (lần xuất hiện đầu tiên)
    print(f"Sau remove(11): {ds_so}")
    phan_tu_xoa = ds_so.pop()  # Xóa và trả về phần tử cuối cùng
    print(f"pop() trả về: {phan_tu_xoa}, ds_so còn: {ds_so}")
    phan_tu_xoa_2 = ds_so.pop(0)  # Xóa và trả về phần tử tại index 0
    print(f"pop(0) trả về: {phan_tu_xoa_2}, ds_so còn: {ds_so}")
    del ds_so[1]  # Xóa theo index bằng từ khóa del
    print(f"Sau del ds_so[1]: {ds_so}")
    ds_so.clear()  # Xóa sạch tất cả phần tử trong list
    print(f"Sau clear(): {ds_so}")

    # 6. Các phương thức & toán tử thường dùng
    print("\n=== 6. Các thao tác & phương thức khác ===")
    ds_moi = [3, 1, 4, 1, 5, 9, 2]
    print(f"Danh sách gốc: {ds_moi}")
    print(f"Độ dài (len): {len(ds_moi)}")
    print(f"Số lần xuất hiện của 1 (count): {ds_moi.count(1)}")
    print(f"Vị trí đầu tiên của 4 (index): {ds_moi.index(4)}")
    print(f"Kiểm tra 5 có trong list không (in): {5 in ds_moi}")

    # Sắp xếp & Đảo ngược
    ds_sap_xep = ds_moi.copy()  # Tạo bản sao độc
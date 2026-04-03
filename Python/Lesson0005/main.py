# main.py - Bài học 5: List và các thao tác cơ bản

# Ví dụ 1: Quản lý danh sách mua sắm
print("=== Ví dụ 1: Quản lý danh sách mua sắm ===")
shopping_list = ["sữa", "trứng", "bánh mì"]
print("Danh sách hiện tại:", shopping_list)

# Thêm món mới
shopping_list.append("pho mát")
print("Sau khi thêm pho mát:", shopping_list)

# Xóa một món
shopping_list.remove("trứng")
print("Sau khi xóa trứng:", shopping_list)

# Hiển thị món đầu và cuối
print("Món đầu:", shopping_list[0])
print("Món cuối:", shopping_list[-1])

print()  # Dòng trống

# Ví dụ 2: Tính điểm trung bình học sinh
print("=== Ví dụ 2: Tính điểm trung bình ===")
diem_toan = 8
điem_ly = 7
điem_hoa = 9
điem_sinh = 10

diem = [diem_toan, diem_ly, diem_hoa, diem_sinh]
print("Các điểm số:", diem)

# Tính trung bình
diem_trung_binh = sum(diem) / len(diem)
print(f"Điểm trung bình: {diem_trung_binh:.2f}")

print()  # Dòng trống

# Ví dụ 3: Tìm phần tử lớn nhất
print("=== Ví dụ 3: Tìm số lớn nhất ===")
numbers = [3, 7, 2, 9, 1, 5]
print("Danh sách số:", numbers)

# Tìm số lớn nhất bằng cách duyệt
max_num = numbers[0]  # Giả sử phần tử đầu là lớn nhất
for num in numbers:
    if num > max_num:
        max_num = num

print("Số lớn nhất là:", max_num)

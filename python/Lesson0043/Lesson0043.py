# Bài 43: Làm việc với File CSV
# Mô tả: Bài này sẽ hướng dẫn cách đọc và ghi dữ liệu vào file CSV bằng Python

# Import thư viện csv để làm việc với file CSV
import csv

# Dữ liệu mẫu để ghi vào file CSV
du_lieu = [
    ["Tên", "Tuổi", "Địa chỉ"],
    ["Nguyễn Văn A", 25, "Hà Nội"],
    ["Trần Thị B", 30, "TP Hồ Chí Minh"],
    ["Lê Văn C", 28, "Đà Nẵng"]
]

# Ghi dữ liệu vào file CSV
def ghi_csv(du_lieu, ten_file):
    # Mở file CSV ở chế độ viết ('w')
    with open(ten_file, 'w', newline='') as file:
        # Tạo đối tượng writer để ghi dữ liệu vào file
        writer = csv.writer(file)
        # Ghi từng dòng dữ liệu vào file
        for dong in du_lieu:
            writer.writerow(dong)

# Đọc dữ liệu từ file CSV
def doc_csv(ten_file):
    # Mở file CSV ở chế độ đọc ('r')
    with open(ten_file, 'r') as file:
        # Tạo đối tượng reader để đọc dữ liệu từ file
        reader = csv.reader(file)
        # Đọc và in từng dòng dữ liệu từ file
        for i, dong in enumerate(reader):
            print(f"Dòng {i+1}: {dong}")

# Tên file CSV
ten_file = 'du_lieu.csv'

# Ghi dữ liệu vào file CSV
ghi_csv(du_lieu, ten_file)
print(f"Đã ghi dữ liệu vào file {ten_file}")

# Đọc dữ liệu từ file CSV
print(f"\nĐọc dữ liệu từ file {ten_file}:")
doc_csv(ten_file)
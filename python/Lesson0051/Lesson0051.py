# Bài 51: Làm việc với file CSV

# Import thư viện cần thiết
import csv

# Hàm đọc file CSV
def doc_file_csv(ten_file):
    # Mở file CSV và đọc nội dung
    with open(ten_file, 'r') as file:
        # Sử dụng csv.reader để đọc file CSV
        csv_reader = csv.reader(file)
        # Duyệt qua từng dòng trong file CSV
        for dong in csv_reader:
            # In ra từng dòng
            print(dong)

# Hàm ghi file CSV
def ghi_file_csv(ten_file, noi_dung):
    # Mở file CSV và ghi nội dung
    with open(ten_file, 'w', newline='') as file:
        # Sử dụng csv.writer để ghi file CSV
        csv_writer = csv.writer(file)
        # Ghi nội dung vào file CSV
        csv_writer.writerows(noi_dung)

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tên file CSV
    ten_file = "example.csv"
    # Nội dung cần ghi vào file CSV
    noi_dung = [
        ["Tên", "Tuổi", "Địa chỉ"],
        ["Nguyễn Văn A", "25", "Hà Nội"],
        ["Trần Thị B", "30", "TP.HCM"]
    ]
    
    # Ghi nội dung vào file CSV
    ghi_file_csv(ten_file, noi_dung)
    
    # Đọc file CSV
    print("Nội dung file CSV:")
    doc_file_csv(ten_file)
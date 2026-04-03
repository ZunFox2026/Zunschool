### Bài tập 1
# Viết hàm tinh_can_bac_hai(x) nhận vào một số x.
# Nếu x âm, ném lỗi ValueError.
# Nếu x không phải số, ném lỗi TypeError.
# Trả về căn bậc hai của x.
# Gợi ý: dùng math.sqrt()

### Bài tập 2
# Viết chương trình yêu cầu người dùng nhập tên file để đọc.
# Dùng try-except để xử lý trường hợp file không tồn tại.
# In nội dung file nếu tìm thấy, hoặc thông báo lỗi nếu không.

### Bài tập 3
# Viết hàm chuyen_doi_chuoi_sang_so(s) nhận một chuỗi.
# Trả về số nguyên nếu chuyển đổi thành công.
# Nếu thất bại, in thông báo và trả về 0.
# Dùng try-except để bắt lỗi.

### Bài tập 4
# Viết một chương trình mô phỏng rút thăm trúng thưởng.
# Người dùng nhập số tiền cược (phải là số dương > 0).
# Nếu nhập sai, yêu cầu nhập lại tối đa 3 lần.
# Nếu sau 3 lần vẫn sai, in "Hủy phiên cược".
# Gợi ý: dùng vòng lặp và try-except.

### Bài tập 5
# Tạo một lớp SoAmError kế thừa từ Exception.
# Viết hàm kiem_tra_so_duong(n) kiểm tra n > 0.
# Nếu n <= 0, ném lỗi SoAmError("Số phải dương!").
# Viết khối try-except để xử lý lỗi này.
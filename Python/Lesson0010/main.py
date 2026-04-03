# main.py
# Bài học 10: Ôn tập và Dự án nhỏ (Calculator, Quiz)
# Các ví dụ minh họa

# --- VÍ DỤ 1: Máy tính đơn giản ---
# Chương trình thực hiện 4 phép toán: cộng, trừ, nhân, chia

def calculator():
    print("=== MÁY TÍNH ĐƠN GIẢN ===")
    print("Chọn phép toán:")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    
    # Nhập lựa chọn
    lua_chon = input("Nhập số tương ứng (1-4): ")
    
    # Kiểm tra lựa chọn hợp lệ
    if lua_chon not in ['1', '2', '3', '4']:
        print("Lựa chọn không hợp lệ!")
        return
    
    # Nhập hai số
    try:
        so_a = float(input("Nhập số thứ nhất: "))
        so_b = float(input("Nhập số thứ hai: "))
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")
        return
    
    # Thực hiện phép toán
    ket_qua = 0
    if lua_chon == '1':
        ket_qua = so_a + so_b
        phep_toan = "Cộng"
    elif lua_chon == '2':
        ket_qua = so_a - so_b
        phep_toan = "Trừ"
    elif lua_chon == '3':
        ket_qua = so_a * so_b
        phep_toan = "Nhân"
    elif lua_chon == '4':
        if so_b == 0:
            print("Lỗi: Không thể chia cho 0!")
            return
        ket_qua = so_a / so_b
        phep_toan = "Chia"
    
    print(f"{phep_toan}: {so_a} và {so_b} = {ket_qua}")

# Gọi hàm để chạy máy tính
# Bỏ dấu # ở dòng dưới để chạy
# calculator()


# --- VÍ DỤ 2: Trò chơi Đố vui đơn giản ---
# Chương trình đặt câu hỏi và chấm điểm

def quiz_game():
    print("\n=== TRÒ CHƠI ĐỐ VUI ===")
    print("Hãy trả lời các câu hỏi sau!")
    
    # Danh sách các câu hỏi và đáp án
    cau_hoi = [
        {"noi_dung": "Python được tạo ra bởi ai?", "dap_an": "guido van rossum"},
        {"noi_dung": "Hàm nào dùng để in ra màn hình?", "dap_an": "print"},
        {"noi_dung": "Từ khóa để định nghĩa hàm trong Python là gì?", "dap_an": "def"}
    ]
    
    diem = 0  # Biến lưu điểm số
    
    # Duyệt qua từng câu hỏi
    for i, q in enumerate(cau_hoi, 1):
        print(f"Câu {i}: {q['noi_dung']}")
        tra_loi = input("Trả lời: ").strip().lower()
        
        if tra_loi == q['dap_an'].lower():
            print("✓ Đúng rồi!\n")
            diem += 1
        else:
            print(f"✗ Sai rồi! Đáp án đúng là: {q['dap_an']}\n")
    
    print(f"Kết quả: Bạn đúng {diem}/{len(cau_hoi)} câu.")
    
    # Đánh giá theo điểm
    if diem == len(cau_hoi):
        print("Xuất sắc! Bạn là cao thủ Python!")
    elif diem >= len(cau_hoi) / 2:
        print("Tốt lắm! Hãy tiếp tục học nhé.")
    else:
        print("Cần cố gắng hơn nữa!")

# Gọi hàm để chơi đố vui
# Bỏ dấu # ở dòng dưới để chạy
# quiz_game()


# --- CHẠY CẢ HAI CHƯƠNG TRÌNH ---
# Bỏ comment 2 dòng dưới để chạy cả hai
if __name__ == "__main__":
    calculator()
    quiz_game()
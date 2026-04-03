#################
# BÀI TẬP
#################

class EmailDescriptor:
    """
    Bài tập 1: Viết một descriptor kiểm tra định dạng email đơn giản.
    Yêu cầu: phải chứa '@' và kết thúc bằng '.com', '.org', hoặc '.edu'
    """
    pass  # TODO: triển khai

class ChoicesDescriptor:
    """
    Bài tập 2: Viết descriptor chỉ chấp nhận giá trị nằm trong danh sách choices cho trước.
    Ví dụ: status = ChoicesDescriptor(['active', 'inactive', 'pending'])
    """
    pass  # TODO: triển khai

class EncryptedDescriptor:
    """
    Bài tập 3: Viết descriptor tự động mã hóa giá trị khi lưu và giải mã khi đọc.
    Gợi ý: có thể dùng hàm băm đơn giản hoặc mã hóa XOR (cho ví dụ đơn giản).
    """
    pass  # TODO: triển khai

class User:
    # Áp dụng các descriptor ở trên
    email = EmailDescriptor()
    status = ChoicesDescriptor(['active', 'inactive', 'pending'])
    password = EncryptedDescriptor()

    def __init__(self, email, status, password):
        self.email = email
        self.status = status
        self.password = password
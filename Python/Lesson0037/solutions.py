### Bài tập 1: Viết hàm chia an toàn
def chia_so_an_toan(a, b):
    try:
        # Kiểm tra kiểu dữ liệu
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Cả hai đối số phải là số")
        
        ket_qua = a / b
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0.")
    except TypeError as e:
        print(f"Lỗi kiểu dữ liệu: {e}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print(f"Kết quả: {a} / {b} = {ket_qua}")
    finally:
        print("(Hoàn tất hàm chia)")


### Bài tập 2: Đọc danh sách số từ file
def doc_danh_sach_so(ten_file):
    danh_sach = []
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:  # Bỏ qua dòng trống
                    try:
                        so = float(line)
                        danh_sach.append(so)
                    except ValueError:
                        print(f"Bỏ qua dòng không hợp lệ: '{line}'")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
    else:
        print(f"Đọc thành công {len(danh_sach)} số.")
    finally:
        print("(Hoàn tất việc đọc file)")
    
    return danh_sach


### Bài tập 3: Lớp Student với kiểm tra điểm
class InvalidGradeError(Exception):
    """Ngoại lệ khi điểm không hợp lệ (không nằm trong khoảng 0-10)"""
    def __init__(self, grade):
        self.grade = grade
        super().__init__(f"Điểm không hợp lệ: {grade}. Điểm phải từ 0 đến 10.")

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def them_diem(self, grade):
        try:
            if not isinstance(grade, (int, float)):
                raise TypeError("Điểm phải là số")
            if grade < 0 or grade > 10:
                raise InvalidGradeError(grade)
            
            self.grades.append(grade)
            print(f"Thêm điểm {grade} cho học sinh {self.name}")
        except InvalidGradeError as e:
            print(f"Lỗi điểm: {e}")
        except TypeError as e:
            print(f"Lỗi kiểu dữ liệu: {e}")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")
        else:
            print("Thêm điểm thành công!")
        finally:
            print("(Kết thúc thao tác thêm điểm)")


### Bài tập 4: Mở file an toàn với finally
def mo_file_va_doc(ten_file):
    file = None
    try:
        file = open(ten_file, 'r', encoding='utf-8')
        noi_dung = file.read()
        print("Nội dung file:")
        print(noi_dung)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'")
    except PermissionError:
        print(f"Lỗi: Không có quyền truy cập file '{ten_file}'")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
    finally:
        if file and not file.closed:
            file.close()
            print("(File đã được đóng an toàn)")


### Bài tập 5: Kiểm tra độ tuổi với ngoại lệ tùy chỉnh
class AgeLimitError(Exception):
    """Ngoại lệ khi độ tuổi không nằm trong giới hạn cho phép"""
    def __init__(self, age, message="Độ tuổi không phù hợp"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def kiem_tra_dang_ky(age):
    try:
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Tuổi phải là số nguyên dương")
        
        if age < 18:
            raise AgeLimitError(age, "Người dùng chưa đủ 18 tuổi để đăng ký")
        if age > 65:
            raise AgeLimitError(age, "Người dùng vượt quá độ tuổi đăng ký")
        
        print(f"Đăng ký thành công! Tuổi: {age}")
    except ValueError as e:
        print(f"Lỗi giá trị: {e}")
    except AgeLimitError as e:
        print(f"Lỗi độ tuổi: {e}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print("Xác nhận đăng ký hoàn tất.")
    finally:
        print("(Kiểm tra độ tuổi kết thúc)")
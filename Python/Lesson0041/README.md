# Bài 41: Xử Lý Ngoại Lệ (Exception Handling) trong Python

## Giới thiệu

Trong quá trình chạy chương trình, có thể xảy ra các lỗi không mong muốn như chia cho 0, truy cập phần tử ngoài danh sách, hoặc nhập liệu sai định dạng. Những lỗi này được gọi là **ngoại lệ (exception)**. Nếu không được xử lý, chương trình sẽ dừng đột ngột. **Xử lý ngoại lệ** giúp chương trình tiếp tục chạy dù có lỗi, bằng cách bắt và xử lý các ngoại lệ một cách an toàn.

## Lý thuyết

Python cung cấp cơ chế `try...except` để xử lý ngoại lệ:

- **`try`**: Chứa đoạn code có thể gây lỗi.
- **`except`**: Xử lý lỗi nếu xảy ra trong khối `try`.
- Có thể bắt nhiều loại ngoại lệ riêng biệt.
- Dùng `else` để thực hiện code nếu không có lỗi.
- Dùng `finally` để thực hiện code dù có lỗi hay không (thường dùng để dọn dẹp tài nguyên).

Các ngoại lệ phổ biến: `ZeroDivisionError`, `ValueError`, `IndexError`, `TypeError`,...

## Ví dụ

```python
try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    print("Kết quả a / b =", a / b)
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")
else:
    print("Phép chia thành công!")
finally:
    print("Kết thúc chương trình.")
```

**Giải thích**:  
- Nếu người dùng nhập chữ thay vì số → `ValueError` được bắt.
- Nếu chia cho 0 → `ZeroDivisionError` được bắt.
- Nếu không có lỗi → in dòng "Phép chia thành công!".
- Dòng trong `finally` luôn được in ra.

## Bài tập

1. Viết chương trình nhập vào một danh sách số nguyên, yêu cầu người dùng nhập chỉ số và in phần tử tại vị trí đó. Xử lý lỗi nếu chỉ số vượt quá độ dài danh sách (`IndexError`).
2. Viết chương trình đọc một tệp văn bản. Dùng `try...except` để xử lý trường hợp tệp không tồn tại (`FileNotFoundError`).
3. Tạo chương trình tính căn bậc hai của một số. Bắt lỗi nếu số âm (`ValueError` khi dùng `math.sqrt()`).
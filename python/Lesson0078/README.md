# Tìm Số Nguyên Tố
## Giới thiệu
Số nguyên tố là một khái niệm cơ bản trong toán học, nó là những số tự nhiên lớn hơn 1 và chỉ chia hết cho 1 và chính nó. Bài viết này sẽ hướng dẫn cách tìm số nguyên tố bằng ngôn ngữ lập trình Python. Đây là một kỹ năng quan trọng trong lập trình và có nhiều ứng dụng trong thực tế.

## Lý thuyết
Một số được coi là nguyên tố nếu nó lớn hơn 1 và chỉ có hai ước là 1 và chính nó. Để kiểm tra một số có phải là nguyên tố hay không, chúng ta có thể sử dụng thuật toán sau:
- Kiểm tra số đó có lớn hơn 1 hay không.
- Duyệt qua tất cả các số từ 2 đến căn bậc hai của số đó, nếu số đó chia hết cho bất kỳ số nào trong khoảng này thì nó không phải là số nguyên tố.
Nếu số đó vượt qua được cả hai bước trên thì nó là một số nguyên tố.

## Ví dụ
Chúng ta sẽ viết một chương trình Python để kiểm tra một số có phải là nguyên tố hay không.
Giả sử chúng ta muốn kiểm tra số 25 có phải là số nguyên tố hay không.
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(25))  # Kết quả: False
```
Kết quả cho thấy số 25 không phải là số nguyên tố vì nó chia hết cho 5.

## Bài tập
Bài tập này yêu cầu bạn viết một chương trình Python để tìm tất cả các số nguyên tố trong một khoảng từ a đến b.
- Đầu tiên, bạn cần định nghĩa hàm `is_prime(n)` như trên để kiểm tra một số có phải là nguyên tố hay không.
- Sau đó, bạn sẽ duyệt qua tất cả các số trong khoảng từ a đến b và kiểm tra từng số bằng hàm `is_prime(n)`.
- Nếu một số là nguyên tố, bạn sẽ in nó ra màn hình.

Ví dụ, nếu khoảng là từ 1 đến 30, chương trình của bạn sẽ in ra tất cả các số nguyên tố trong khoảng này.
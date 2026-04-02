# Tìm Số Nguyên Tố
## Giới thiệu
Số nguyên tố là một số tự nhiên lớn hơn 1, chỉ có hai ước là 1 và chính nó. Bài viết này sẽ hướng dẫn cách tìm số nguyên tố bằng ngôn ngữ lập trình Python. Đây là một chủ đề cơ bản nhưng rất quan trọng trong toán học và lập trình.

## Lý thuyết
Để tìm số nguyên tố, chúng ta cần kiểm tra mỗi số tự nhiên lớn hơn 1 để xem nó có phải là số nguyên tố hay không. Một số được coi là nguyên tố nếu nó chỉ chia hết cho 1 và chính nó. Ví dụ, số 5 là số nguyên tố vì nó chỉ chia hết cho 1 và 5. Ngược lại, số 6 không phải là số nguyên tố vì nó chia hết cho 1, 2, 3 và 6.

Chúng ta có thể sử dụng thuật toán sau để kiểm tra số nguyên tố:
- Nếu số nhỏ hơn hoặc bằng 1, nó không phải là số nguyên tố.
- Nếu số chỉ chia hết cho 1 và chính nó, nó là số nguyên tố.
- Ngược lại, số không phải là số nguyên tố.

## Ví dụ
Ví dụ, chúng ta muốn kiểm tra số 7 có phải là số nguyên tố hay không. Chúng ta sẽ thực hiện các bước sau:
- Kiểm tra số 7 có nhỏ hơn hoặc bằng 1 hay không. Vì 7 lớn hơn 1 nên chúng ta tiếp tục bước tiếp theo.
- Kiểm tra số 7 có chia hết cho các số từ 2 đến 6 hay không. Vì 7 không chia hết cho bất kỳ số nào trong các số này, nên chúng ta kết luận rằng 7 là số nguyên tố.

Dưới đây là một đoạn code Python đơn giản để kiểm tra số nguyên tố:
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # Output: True
```

## Bài tập
Bài tập cho bạn đọc:
- Viết một chương trình Python để tìm tất cả các số nguyên tố trong khoảng từ 1 đến 100.
- Tối ưu hóa chương trình bằng cách chỉ kiểm tra các số chia hết lên đến căn bậc hai của số cần kiểm tra.
- In ra các số nguyên tố tìm được.

Đây là một bài tập cơ bản nhưng rất hữu ích để giúp bạn hiểu và áp dụng kiến thức về số nguyên tố vào lập trình.
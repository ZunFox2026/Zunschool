# Lập Trình Cơ Bản
Bài học này cung cấp kiến thức cơ bản về lập trình, bao gồm các khái niệm, cấu trúc và cách viết code hiệu quả.

## Giới thiệu
Lập trình là quá trình thiết kế, viết, kiểm tra và bảo trì code để tạo ra các chương trình máy tính. Nó đòi hỏi sự kết hợp giữa logic, toán học và kỹ năng giải quyết vấn đề. Trong bài học này, chúng ta sẽ khám phá các khái niệm cơ bản của lập trình, bao gồm biến, kiểu dữ liệu, cấu trúc điều khiển và hàm.

## Lý thuyết
Trong lập trình, chúng ta cần hiểu về các khái niệm sau:
- Biến: Là nơi lưu trữ dữ liệu trong chương trình.
- Kiểu dữ liệu: Chỉ định loại dữ liệu mà biến có thể chứa, chẳng hạn như số nguyên, chuỗi, boolean.
- Cấu trúc điều khiển: Cho phép chương trình thực hiện các hành động khác nhau dựa trên điều kiện, chẳng hạn như if-else, switch-case.
- Hàm: Là một khối code có thể được gọi nhiều lần từ các phần khác nhau của chương trình.

Ví dụ, trong Python, chúng ta có thể khai báo biến như sau:
```python
x = 5  # khai báo biến x với giá trị 5
y = "Hello"  # khai báo biến y với giá trị "Hello"
```
Chúng ta cũng có thể sử dụng cấu trúc điều khiển để kiểm tra điều kiện:
```python
if x > 10:
    print("x lớn hơn 10")
else:
    print("x nhỏ hơn hoặc bằng 10")
```
## Ví dụ
Để minh họa cách áp dụng các khái niệm trên, hãy xem xét ví dụ sau:
Giả sử chúng ta muốn viết một chương trình để kiểm tra xem một số có phải là số chẵn hay không.
```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

num = 10
if is_even(num):
    print(f"{num} là số chẵn")
else:
    print(f"{num} là số lẻ")
```
## Bài tập
Để ôn lại kiến thức, hãy thực hiện các bài tập sau:
1. Viết một chương trình để tính tổng của hai số.
2. Tạo một hàm để kiểm tra xem một số có phải là số nguyên tố hay không.
3. Viết một chương trình để in ra các số chẵn từ 1 đến 100.

Bằng cách hoàn thành các bài tập này, bạn sẽ có thể nắm vững các khái niệm cơ bản của lập trình và sẵn sàng để tiếp tục học các chủ đề nâng cao hơn.
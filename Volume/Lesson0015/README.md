# Làm quen với Thư viện
## Giới thiệu
Thư viện là một tập hợp các hàm, lớp và biến đã được định nghĩa sẵn, giúp cho việc lập trình trở nên dễ dàng và hiệu quả hơn. Trong Python, chúng ta có thể sử dụng các thư viện có sẵn hoặc tự tạo ra các thư viện của riêng mình. Việc sử dụng thư viện giúp cho code trở nên ngắn gọn và dễ bảo trì hơn.

## Lý thuyết
Một thư viện thường bao gồm các thành phần sau:
- Hàm (function): là một khối code thực hiện một nhiệm vụ cụ thể.
- Lớp (class): là một định nghĩa cho một đối tượng, bao gồm các thuộc tính và phương thức.
- Biến (variable): là một tên được gán cho một giá trị.

Để sử dụng một thư viện, chúng ta cần phải nhập (import) nó vào chương trình. Có thể nhập toàn bộ thư viện hoặc chỉ nhập các thành phần cụ thể mà chúng ta cần.

## Ví dụ
Ví dụ, chúng ta muốn sử dụng hàm `sin` từ thư viện `math` để tính sin của một góc:
```python
import math

goc = 30  # độ
sin_goc = math.sin(math.radians(goc))
print(f"Sin của {goc} độ là {sin_goc}")
```
Trong ví dụ trên, chúng ta nhập toàn bộ thư viện `math` và sử dụng hàm `sin` để tính sin của một góc.

## Bài tập
Bài tập 1: Viết một chương trình sử dụng thư viện `random` để sinh ra một số ngẫu nhiên giữa 1 và 100.

Bài tập 2: Viết một chương trình sử dụng thư viện `math` để tính diện tích và chu vi của một hình tròn có bán kính là 5.

Bài tập 3: Tìm hiểu về thư viện `time` và viết một chương trình sử dụng nó để hiển thị thời gian hiện tại.

Những bài tập trên sẽ giúp bạn làm quen với việc sử dụng thư viện trong Python và áp dụng vào các vấn đề thực tế. Hãy thử nghiệm và khám phá thêm về các thư viện khác trong Python!
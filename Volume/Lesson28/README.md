# Làm việc với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất của Python, được sử dụng để tạo ra các biểu đồ và hình ảnh chất lượng cao. Nó cung cấp một loạt các công cụ để tạo ra các loại biểu đồ khác nhau, từ biểu đồ đơn giản đến các biểu đồ phức tạp. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với thư viện matplotlib để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Để bắt đầu làm việc với matplotlib, bạn cần phải nhập thư viện này vào chương trình của mình bằng cách sử dụng lệnh `import matplotlib.pyplot as plt`. Sau đó, bạn có thể sử dụng các hàm và phương thức của matplotlib để tạo ra các biểu đồ.

Một số hàm và phương thức cơ bản của matplotlib bao gồm:
- `plt.plot()`: Tạo ra một biểu đồ đường thẳng.
- `plt.bar()`: Tạo ra một biểu đồ cột.
- `plt.scatter()`: Tạo ra một biểu đồ điểm.
- `plt.title()`: Thêm tiêu đề cho biểu đồ.
- `plt.xlabel()`: Thêm nhãn cho trục x.
- `plt.ylabel()`: Thêm nhãn cho trục y.
- `plt.show()`: Hiển thị biểu đồ.

## Ví dụ
Dưới đây là một ví dụ về cách tạo ra một biểu đồ đường thẳng đơn giản:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Biểu đồ đường thẳng')
plt.xlabel('Trục x')
plt.ylabel('Trục y')
plt.show()
```
Kết quả sẽ là một biểu đồ đường thẳng với tiêu đề, nhãn trục x và trục y.

## Bài tập
Bài tập cho bạn:
- Tạo ra một biểu đồ cột với 5 cột, mỗi cột có giá trị tương ứng là 10, 20, 30, 40, 50.
- Thêm tiêu đề, nhãn trục x và trục y cho biểu đồ.
- Hiển thị biểu đồ.
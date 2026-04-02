# Làm việc với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất trong Python, được sử dụng để tạo ra các biểu đồ và hình ảnh chất lượng cao. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với thư viện matplotlib để tạo ra các biểu đồ cơ bản.

Matplotlib cung cấp nhiều công cụ và tính năng để tạo ra các biểu đồ khác nhau, từ biểu đồ đơn giản đến biểu đồ phức tạp. Nó cũng hỗ trợ nhiều loại biểu đồ, bao gồm biểu đồ đường, biểu đồ cột, biểu đồ tròn, v.v.

## Lý thuyết
Để bắt đầu làm việc với matplotlib, bạn cần nhập thư viện này vào chương trình Python của mình bằng cách sử dụng câu lệnh `import matplotlib.pyplot as plt`. Sau đó, bạn có thể sử dụng các hàm và công cụ của matplotlib để tạo ra các biểu đồ.

Một số hàm cơ bản trong matplotlib bao gồm:
- `plt.plot()`: Tạo ra biểu đồ đường.
- `plt.bar()`: Tạo ra biểu đồ cột.
- `plt.pie()`: Tạo ra biểu đồ tròn.
- `plt.title()`: Thêm tiêu đề cho biểu đồ.
- `plt.xlabel()`: Thêm nhãn cho trục x.
- `plt.ylabel()`: Thêm nhãn cho trục y.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách tạo ra biểu đồ đường sử dụng matplotlib:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Biểu đồ đường')
plt.xlabel('Trục x')
plt.ylabel('Trục y')
plt.show()
```
Khi chạy chương trình này, bạn sẽ thấy một biểu đồ đường với tiêu đề "Biểu đồ đường" và nhãn cho trục x và trục y.

## Bài tập
Bài tập 1: Tạo ra biểu đồ cột với các giá trị x = [1, 2, 3, 4, 5] và y = [2, 4, 6, 8, 10].
Bài tập 2: Tạo ra biểu đồ tròn với các giá trị x = [10, 20, 30, 40] và nhãn cho từng phần của biểu đồ.
Bài tập 3: Tạo ra biểu đồ đường với các giá trị x = [1, 2, 3, 4, 5] và y = [1, 8, 27, 64, 125], và thêm tiêu đề, nhãn cho trục x và trục y.
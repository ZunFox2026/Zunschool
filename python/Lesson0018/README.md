# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất trong Python để tạo ra các biểu đồ và đồ thị. Nó cung cấp một tập hợp các công cụ mạnh mẽ để tạo ra các biểu đồ 2D và 3D, từ các biểu đồ đơn giản đến các biểu đồ phức tạp. Với matplotlib, bạn có thể tạo ra các biểu đồ để minh họa dữ liệu của mình một cách rõ ràng và hiệu quả.

## Lý thuyết
Matplotlib cung cấp nhiều loại biểu đồ khác nhau, bao gồm biểu đồ đường, biểu đồ cột, biểu đồ tròn, biểu đồ phân tán, v.v. Để tạo ra một biểu đồ, bạn cần phải nhập thư viện matplotlib vào chương trình của mình, sau đó sử dụng các hàm và phương thức của thư viện để tạo ra biểu đồ. Ví dụ, bạn có thể sử dụng hàm `plot()` để tạo ra một biểu đồ đường, hoặc hàm `bar()` để tạo ra một biểu đồ cột.

Một số khái niệm quan trọng trong matplotlib bao gồm:
- **Trục (Axes)**: Là khu vực mà biểu đồ được vẽ.
- **Đồ thị (Figure)**: Là cửa sổ chứa biểu đồ.
- **Biểu đồ (Plot)**: Là đồ họa được tạo ra bằng cách sử dụng dữ liệu.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng matplotlib để tạo ra một biểu đồ đường:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Biểu đồ đường')
plt.show()
```
Kết quả sẽ là một biểu đồ đường với trục x và trục y được gán nhãn và tiêu đề.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một biểu đồ cột để so sánh số lượng sinh viên của ba trường đại học khác nhau. Giả sử bạn có dữ liệu sau:
- Trường A: 1000 sinh viên
- Trường B: 1500 sinh viên
- Trường C: 2000 sinh viên

Hãy sử dụng matplotlib để tạo ra một biểu đồ cột với các nhãn và tiêu đề phù hợp. Bạn có thể sử dụng hàm `bar()` để tạo ra biểu đồ cột. Hãy thử nghiệm với các tùy chọn khác nhau của hàm `bar()` để tạo ra biểu đồ của mình.
# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất để tạo đồ họa trong Python. Nó cung cấp các công cụ mạnh mẽ và linh hoạt để tạo ra nhiều loại biểu đồ khác nhau, từ biểu đồ đơn giản đến biểu đồ phức tạp. Trong bài này, chúng ta sẽ tìm hiểu cách làm quen với thư viện matplotlib và cách sử dụng nó để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Matplotlib cung cấp nhiều loại biểu đồ khác nhau, bao gồm biểu đồ đường, biểu đồ cột, biểu đồ tròn, v.v. Để tạo ra một biểu đồ, chúng ta cần nhập thư viện matplotlib và sử dụng các hàm của nó. Ví dụ, để tạo ra một biểu đồ đường, chúng ta có thể sử dụng hàm `plot()` của matplotlib. Chúng ta cũng cần định nghĩa các giá trị x và y của biểu đồ.

Matplotlib cũng cung cấp nhiều tùy chọn để tùy chỉnh biểu đồ, chẳng hạn như thay đổi màu sắc, kích thước, v.v. Chúng ta có thể sử dụng các hàm như `title()`, `xlabel()`, `ylabel()` để thêm tiêu đề và nhãn cho biểu đồ.

## Ví dụ
Dưới đây là một ví dụ về cách tạo ra một biểu đồ đường đơn giản sử dụng matplotlib:
- Đầu tiên, nhập thư viện matplotlib: `import matplotlib.pyplot as plt`
- Định nghĩa các giá trị x và y: `x = [1, 2, 3, 4, 5]; y = [1, 4, 9, 16, 25]`
- Tạo biểu đồ: `plt.plot(x, y)`
- Thêm tiêu đề và nhãn: `plt.title('Biểu đồ đường'); plt.xlabel('X'); plt.ylabel('Y')`
- Hiển thị biểu đồ: `plt.show()`

Kết quả sẽ là một biểu đồ đường với các giá trị x và y đã định nghĩa.

## Bài tập
Để luyện tập, hãy thực hiện các bài tập sau:
- Tạo một biểu đồ cột với các giá trị x và y đã định nghĩa.
- Tạo một biểu đồ tròn với các giá trị x và y đã định nghĩa.
- Thay đổi màu sắc và kích thước của biểu đồ đường trong ví dụ trên.
- Thêm nhãn và tiêu đề cho các biểu đồ trên.

Bằng cách thực hiện các bài tập này, bạn sẽ có thể làm quen với thư viện matplotlib và tạo ra các biểu đồ cơ bản.
# Làm quen với Thư viện Matplotlib
## Giới thiệu
Matplotlib là một thư viện vẽ đồ họa vô cùng mạnh mẽ và phổ biến trong Python. Nó được sử dụng rộng rãi trong nhiều lĩnh vực như khoa học, kỹ thuật, tài chính,... để tạo ra các biểu đồ, đồ thị, hình ảnh từ dữ liệu. Với Matplotlib, bạn có thể tạo ra nhiều loại đồ họa khác nhau, từ đơn giản như đồ thị 2D đến phức tạp như đồ thị 3D, hình ảnh phân bố,...

Matplotlib cung cấp nhiều tính năng như tùy chỉnh màu sắc, phong cách, kích thước, thêm nhãn, tiêu đề, lưới,... giúp người dùng có thể tạo ra các đồ họa đẹp mắt và chuyên nghiệp. Ngoài ra, Matplotlib cũng hỗ trợ nhiều loại dữ liệu đầu vào khác nhau, bao gồm cả dữ liệu số và dữ liệu không gian.

## Lý thuyết
Để bắt đầu sử dụng Matplotlib, bạn cần import thư viện này vào chương trình Python của mình. Sau đó, bạn có thể sử dụng các hàm và phương thức của Matplotlib để tạo ra các đồ họa. Một số hàm và phương thức cơ bản của Matplotlib bao gồm:
- `plot()`: Tạo ra một đồ thị 2D đơn giản.
- `scatter()`: Tạo ra một đồ thị phân bố điểm.
- `bar()`: Tạo ra một biểu đồ cột.
- `hist()`: Tạo ra một biểu đồ phân bố histogram.
- `imshow()`: Tạo ra một hình ảnh từ dữ liệu 2D.

Ngoài ra, bạn cũng có thể tùy chỉnh các thuộc tính của đồ họa như màu sắc, kích thước, phong cách,... bằng cách sử dụng các phương thức như `set_title()`, `set_xlabel()`, `set_ylabel()`, `legend()`,...

## Ví dụ
Để minh họa cách sử dụng Matplotlib, hãy xem xét ví dụ sau:
```python
import matplotlib.pyplot as plt

# Tạo ra một đồ thị 2D đơn giản
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)

# Thêm tiêu đề và nhãn
plt.title('Đồ thị 2D')
plt.xlabel('X')
plt.ylabel('Y')

# Hiển thị lưới và đồ thị
plt.grid(True)
plt.show()
```
Kết quả sẽ là một đồ thị 2D đơn giản với tiêu đề, nhãn và lưới.

## Bài tập
Để thực hành sử dụng Matplotlib, hãy thực hiện các bài tập sau:
- Tạo ra một biểu đồ cột thể hiện số lượng sản phẩm bán ra trong một tháng.
- Tạo ra một đồ thị phân bố điểm thể hiện mối quan hệ giữa tuổi và chiều cao của một nhóm người.
- Tạo ra một hình ảnh từ dữ liệu 2D thể hiện phân bố nhiệt độ trong một khu vực.

Hy vọng qua các ví dụ và bài tập trên, bạn đã có thể hiểu rõ hơn về cách sử dụng Matplotlib và tạo ra các đồ họa đẹp mắt và chuyên nghiệp.
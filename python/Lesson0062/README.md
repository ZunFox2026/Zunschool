# Lập Trình Cơ Bản về Tính Sóng
## Giới thiệu
Tính sóng là một trong những khái niệm cơ bản trong vật lý học, mô tả sự lan truyền của năng lượng qua không gian. Trong lập trình, tính sóng có thể được ứng dụng để mô phỏng và phân tích các hiện tượng vật lý, cũng như tạo ra các hiệu ứng hình ảnh và âm thanh thú vị. Bài viết này sẽ giới thiệu về tính sóng và cách ứng dụng nó trong lập trình Python.

## Lý thuyết
Tính sóng được mô tả bằng phương trình sóng, thường có dạng y = A * sin(2 * π * f * t + φ), trong đó:
- y là biên độ của sóng
- A là biên độ cực đại
- f là tần số của sóng
- t là thời gian
- φ là pha ban đầu của sóng
Trong lập trình, chúng ta có thể sử dụng các thư viện như NumPy và Matplotlib để tạo ra các sóng và phân tích chúng.

## Ví dụ
Dưới đây là một ví dụ về cách tạo ra một sóng sin trong Python:
```python
import numpy as np
import matplotlib.pyplot as plt

# Định nghĩa các thông số của sóng
A = 1  # biên độ cực đại
f = 1  # tần số
t = np.linspace(0, 10, 1000)  # thời gian

# Tạo sóng sin
y = A * np.sin(2 * np.pi * f * t)

# Vẽ sóng
plt.plot(t, y)
plt.xlabel('Thời gian')
plt.ylabel('Biên độ')
plt.title('Sóng Sin')
plt.show()
```
Kết quả sẽ là một đồ thị biểu diễn sóng sin với biên độ cực đại là 1 và tần số là 1.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một chương trình Python để mô phỏng một sóng hình sin với các thông số sau:
- Biên độ cực đại: 2
- Tần số: 0,5
- Thời gian: từ 0 đến 20
- Pha ban đầu: π/2
Chương trình nên sử dụng các thư viện NumPy và Matplotlib để tạo ra sóng và vẽ đồ thị của nó. Ngoài ra, chương trình cũng nên tính toán và in ra giá trị biên độ cực đại và tần số của sóng.
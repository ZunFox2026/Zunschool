# Làm quen với thư viện Pygame
## Giới thiệu
Thư viện Pygame là một bộ công cụ được sử dụng để tạo ra các trò chơi và ứng dụng đa phương tiện trên nền tảng Python. Pygame cung cấp một cách đơn giản và dễ dàng để tạo ra các ứng dụng có đồ họa và âm thanh. Trong bài này, chúng ta sẽ tìm hiểu về cách cài đặt và sử dụng thư viện Pygame.

Pygame được phát triển bởi Pete Shinners và được phát hành lần đầu tiên vào năm 2000. Kể từ đó, thư viện này đã trở thành một trong những thư viện phổ biến nhất trong cộng đồng Python. Pygame hỗ trợ nhiều nền tảng khác nhau, bao gồm Windows, macOS và Linux.

## Lý thuyết
Để bắt đầu sử dụng Pygame, bạn cần cài đặt nó vào môi trường Python của mình. Bạn có thể làm điều này bằng cách chạy lệnh `pip install pygame` trong terminal hoặc command prompt.

Sau khi cài đặt, bạn có thể nhập thư viện Pygame vào chương trình Python của mình bằng cách sử dụng lệnh `import pygame`. Để tạo ra một ứng dụng Pygame, bạn cần khởi tạo nó bằng cách gọi hàm `pygame.init()`.

Một số hàm cơ bản trong Pygame bao gồm:
- `pygame.display.set_mode((chiều_rộng, chiều_cao))`: Tạo ra một cửa sổ với chiều rộng và chiều cao cụ thể.
- `pygame.display.set_caption("Tiêu đề")`: Đặt tiêu đề cho cửa sổ.
- `pygame.time.Clock()`: Tạo ra một đồng hồ để kiểm soát tốc độ khung hình.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách tạo ra một cửa sổ Pygame:
```python
import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Tạo ra một cửa sổ
screen = pygame.display.set_mode((800, 600))

# Đặt tiêu đề cho cửa sổ
pygame.display.set_caption("Làm quen với Pygame")

# Tạo ra một đồng hồ
clock = pygame.time.Clock()

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vẽ nền màu trắng
    screen.fill((255, 255, 255))

    # Cập nhật màn hình
    pygame.display.flip()

    # Điều chỉnh tốc độ khung hình
    clock.tick(60)
```
Ví dụ trên sẽ tạo ra một cửa sổ với chiều rộng 800 pixel và chiều cao 600 pixel, có tiêu đề "Làm quen với Pygame" và nền màu trắng.

## Bài tập
Bài tập cho bạn:
- Tạo ra một cửa sổ Pygame với chiều rộng 640 pixel và chiều cao 480 pixel.
- Đặt tiêu đề cho cửa sổ là "Bài tập Pygame".
- Vẽ một hình chữ nhật màu đỏ tại vị trí (100, 100) với chiều rộng 200 pixel và chiều cao 100 pixel.
- Sử dụng vòng lặp để cập nhật màn hình và điều chỉnh tốc độ khung hình là 60 khung hình/giây.
- Thêm sự kiện để đóng cửa sổ khi người dùng nhấn nút关闭.
# Làm quen với thư viện Pygame
## Giới thiệu
Thư viện Pygame là một trong những thư viện phổ biến nhất trong Python, được sử dụng để tạo ra các trò chơi và ứng dụng đa phương tiện. Pygame cung cấp một cách đơn giản và dễ dàng để tạo ra các ứng dụng có giao diện người dùng đồ họa, xử lý sự kiện, và chơi âm thanh. Trong bài này, chúng ta sẽ tìm hiểu về cách làm quen với thư viện Pygame và tạo ra một ứng dụng đơn giản.

## Lý thuyết
Trước khi bắt đầu, bạn cần cài đặt Pygame trên máy tính của mình. Bạn có thể làm điều này bằng cách chạy lệnh `pip install pygame` trong terminal. Sau khi cài đặt, bạn có thể nhập thư viện Pygame vào chương trình của mình bằng cách sử dụng lệnh `import pygame`.

Pygame có một số mô-đun chính, bao gồm:
- `pygame.display`: dùng để tạo ra cửa sổ và hiển thị đồ họa.
- `pygame.event`: dùng để xử lý sự kiện, như nhấn phím hoặc di chuột.
- `pygame.draw`: dùng để vẽ đồ họa, như hình chữ nhật, hình tròn, và đường thẳng.
- `pygame.image`: dùng để tải và hiển thị hình ảnh.

## Ví dụ
Ví dụ sau đây sẽ tạo ra một cửa sổ với nền màu xanh và một hình chữ nhật màu đỏ:
```python
import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Tạo cửa sổ
screen = pygame.display.set_mode((800, 600))

# Tạo hình chữ nhật
rect = pygame.Rect(100, 100, 200, 200)

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vẽ nền màu xanh
    screen.fill((0, 255, 0))

    # Vẽ hình chữ nhật màu đỏ
    pygame.draw.rect(screen, (255, 0, 0), rect)

    # Cập nhật màn hình
    pygame.display.flip()

    # Đợi 1/60 giây
    pygame.time.Clock().tick(60)
```
Ví dụ này sẽ tạo ra một cửa sổ với nền màu xanh và một hình chữ nhật màu đỏ. Khi bạn nhấn nút đóng, chương trình sẽ thoát.

## Bài tập
Bài tập sau đây sẽ giúp bạn làm quen với thư viện Pygame:
- Tạo một cửa sổ với nền màu vàng và một hình tròn màu xanh.
- Xử lý sự kiện nhấn phím để di chuyển hình tròn.
- Tạo một ứng dụng đơn giản với một hình chữ nhật có thể di chuyển bằng chuột.
- Tải và hiển thị một hình ảnh trên màn hình.

Hy vọng rằng qua bài này, bạn đã có một cái nhìn tổng quan về thư viện Pygame và có thể bắt đầu tạo ra các ứng dụng và trò chơi của mình. Hãy nhớ rằng, thực hành là chìa khóa để trở thành một lập trình viên giỏi!
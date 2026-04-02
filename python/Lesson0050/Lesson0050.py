# Khởi tạo Pygame
import pygame
import sys

# Khởi tạo các mô-đun của Pygame
pygame.init()

# Thiết lập chiều rộng và chiều cao của cửa sổ
chieu_rong = 800
chieu_cao = 600
man_hinh = pygame.display.set_mode((chieu_rong, chieu_cao))

# Thiết lập tiêu đề của cửa sổ
pygame.display.set_caption("Làm quen với thư viện Pygame")

# Thiết lập màu sắc
mau_den = (0, 0, 0)
mau_trang = (255, 255, 255)

# Thiết lập font chữ
font = pygame.font.SysFont("Arial", 30)

# Vòng lặp chính của trò chơi
while True:
    for su_kien in pygame.event.get():
        if su_kien.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vẽ nền màu đen
    man_hinh.fill(mau_den)

    # Vẽ chữ "Xin chào, Pygame!" màu trắng
    chu = font.render("Xin chào, Pygame!", True, mau_trang)
    man_hinh.blit(chu, (chieu_rong // 2 - chu.get_width() // 2, chieu_cao // 2 - chu.get_height() // 2))

    # Cập nhật màn hình
    pygame.display.flip()

    # Đặt giới hạn khung hình
    pygame.time.Clock().tick(60)
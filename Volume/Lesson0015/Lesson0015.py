# Bài 15: Làm quen với Thư viện
# Thư viện là một tập hợp các hàm, lớp và biến được định nghĩa sẵn, 
# giúp cho việc lập trình trở nên dễ dàng hơn.

# Import thư viện math
import math

# Sử dụng hàm sqrt từ thư viện math để tính căn bậc 2 của 16
can_bac_2 = math.sqrt(16)
print("Căn bậc 2 của 16 là:", can_bac_2)

# Import thư viện random
import random

# Sử dụng hàm randint từ thư viện random để sinh một số ngẫu nhiên từ 1 đến 10
so_ngau_nhien = random.randint(1, 10)
print("Số ngẫu nhiên từ 1 đến 10 là:", so_ngau_nhien)

# Import thư viện time
import time

# Sử dụng hàm time từ thư viện time để hiển thị giờ hiện tại
gio_hien_tai = time.time()
print("Giờ hiện tại là:", time.ctime(gio_hien_tai))

# Import thư viện datetime
from datetime import datetime

# Sử dụng hàm now từ thư viện datetime để hiển thị ngày và giờ hiện tại
ngay_gio_hien_tai = datetime.now()
print("Ngày và giờ hiện tại là:", ngay_gio_hien_tai)
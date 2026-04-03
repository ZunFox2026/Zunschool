from functools import lru_cache
import time

# ====================
# VÍ DỤ 1: Tính số Fibonacci
# ====================

@lru_cache(maxsize=None)
def fibonacci(n):
    """Tính số Fibonacci thứ n bằng đệ quy tối ưu"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Đo thời gian trước và sau khi dùng cache
print("1. Tính Fibonacci(35) với lru_cache")
start = time.time()
result = fibonacci(35)
end = time.time()
print(f"fibonacci(35) = {result}")
print(f"Thời gian: {end - start:.4f} giây\n")

# Xóa bộ nhớ đệm (nếu cần)
fibonacci.cache_clear()

# ====================
# VÍ DỤ 2: Tính tổ hợp C(n, k)
# ====================

@lru_cache(maxsize=None)
def combination(n, k):
    """Tính tổ hợp C(n, k) = n! / (k! * (n-k)!)"""
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    return combination(n-1, k-1) + combination(n-1, k)

print("2. Tính C(10, 4)")
result = combination(10, 4)
print(f"C(10, 4) = {result}")
print(f"Thông tin cache: {combination.cache_info()}\n")

# ====================
# VÍ DỤ 3: Hàm giả lập xử lý chậm
# ====================

@lru_cache(maxsize=32)
def get_product_price(product_id):
    """Giả lập việc tra cứu giá sản phẩm từ cơ sở dữ liệu (chậm)"""
    print(f"Đang tra cứu giá cho sản phẩm {product_id}...")
    time.sleep(1)  # Giả lập độ trễ mạng
    prices = {1: 100000, 2: 150000, 3: 200000}
    return prices.get(product_id, 0)

print("3. Tra cứu giá sản phẩm (lần đầu)")
start = time.time()
price1 = get_product_price(1)
print(f"Giá sản phẩm 1: {price1} VND")
print(f"Thời gian: {time.time() - start:.2f} giây\n")

print("Tra cứu lại sản phẩm 1 (dùng cache)")
start = time.time()
price1_cached = get_product_price(1)
print(f"Giá sản phẩm 1 (cache): {price1_cached} VND")
print(f"Thời gian: {time.time() - start:.2f} giây\n")

# Hiển thị thông tin cache
cache_info = get_product_price.cache_info()
print(f"Thông tin cache: hits={cache_info.hits}, misses={cache_info.misses}, currsize={cache_info.currsize}")
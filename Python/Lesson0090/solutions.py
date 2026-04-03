from functools import lru_cache

# ====================
# Bài tập 1: Hàm Lucas với lru_cache
# ====================
@lru_cache(maxsize=None)
def lucas(n):
    """Tính số Lucas thứ n: L(0)=2, L(1)=1, L(n)=L(n-1)+L(n-2)"""
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

# Kiểm thử
print("Bài tập 1: Số Lucas(10) =", lucas(10))
print("Cache info:", lucas.cache_info())

# ====================
# Bài tập 2: Tổng dãy Fibonacci từ 1 đến n
# ====================
@lru_cache(maxsize=None)
def fibonacci(n):
    """Hàm hỗ trợ: tính số Fibonacci thứ n"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@lru_cache(maxsize=None)
def sum_fibonacci(n):
    """Tính tổng fibonacci(1) + fibonacci(2) + ... + fibonacci(n)"""
    if n <= 0:
        return 0
    if n == 1:
        return fibonacci(1)
    return fibonacci(n) + sum_fibonacci(n-1)

# Kiểm thử
print("\nBài tập 2: Tổng Fibonacci từ 1 đến 10 =", sum_fibonacci(10))
print("Cache info sum_fibonacci:", sum_fibonacci.cache_info())

# ====================
# Bài tập 3: Kiểm tra số nguyên tố với cache
# ====================
@lru_cache(maxsize=None)
def is_prime(n):
    """Kiểm tra n có phải số nguyên tố không"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Kiểm thử
print("\nBài tập 3: is_prime(97) =", is_prime(97))
print("is_prime(100) =", is_prime(100))
print("Cache info:", is_prime.cache_info())

# ====================
# Bài tập 4: Đếm số từ trong câu
# ====================
@lru_cache(maxsize=128)
def word_count(sentence):
    """Đếm số từ trong câu, dùng cache"""
    # Loại bỏ khoảng trắng thừa và tách từ
    words = sentence.strip().split()
    return len(words)

# Kiểm thử
print("\nBài tập 4: word_count('Xin chào các bạn') =", word_count('Xin chào các bạn'))
print("Gọi lại: ", word_count('Xin chào các bạn'))
print("Cache info:", word_count.cache_info())

# Nhận xét: Có thể dùng lru_cache vì chuỗi là hashable
# Nhưng hiệu quả thực tế không cao vì hàm word_count rất nhanh
# Việc dùng cache có thể lãng phí bộ nhớ nếu có nhiều câu khác nhau
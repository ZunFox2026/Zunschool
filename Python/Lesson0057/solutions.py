from functools import lru_cache
import time

# ==================== Bài 1: Giai thừa với lru_cache ====================
def factorial_slow(n):
    if n <= 1:
        return 1
    return n * factorial_slow(n - 1)

@lru_cache(maxsize=None)
def factorial_fast(n):
    if n <= 1:
        return 1
    return n * factorial_fast(n - 1)

# Đo thời gian
n = 20
start = time.time()
factorial_slow(n)
duration_slow = time.time() - start

start = time.time()
factorial_fast(n)
duration_fast = time.time() - start

print(f"Giai thừa({n}) - Không cache: {duration_slow:.6f}s")
print(f"Giai thừa({n}) - Có cache: {duration_fast:.6f}s")
print()

# ==================== Bài 2: Đếm số cách phân tích số n ====================
@lru_cache(maxsize=None)
def count_partitions(n, max_num):
    # Nếu n == 0, có đúng 1 cách (không chọn gì)
    if n == 0:
        return 1
    # Nếu n < 0 hoặc max_num == 0, không có cách nào
    if n < 0 or max_num == 0:
        return 0
    # Tổng số cách = (sử dụng max_num) + (không sử dụng max_num)
    return count_partitions(n - max_num, max_num) + count_partitions(n, max_num - 1)

print(f"Số cách phân tích số 5: {count_partitions(5, 5)}")
print()

# ==================== Bài 3: Đếm số cách tạo chuỗi đối xứng ====================
@lru_cache(maxsize=None)
def count_palindromic_choices_helper(choices_tuple, left, right):
    # Chuyển danh sách thành tuple để có thể cache
    # left, right là chỉ số trái và phải
    if left > right:
        return 1  # Đã xét xong
    if left == right:
        # Một ký tự ở giữa, có thể chọn 1 trong 2
        return 2
    
    total = 0
    # Lấy ký tự có thể chọn tại vị trí left và right
    left_choices = choices_tuple[left]
    right_choices = choices_tuple[right]
    
    # Kiểm tra từng cặp ký tự có thể tạo thành đối xứng
    for c_left in left_choices:
        for c_right in right_choices:
            if c_left == c_right:
                total += count_palindromic_choices_helper(choices_tuple, left + 1, right - 1)
    
    return total

def count_palindromic_choices(choices):
    # Chuyển danh sách thành tuple để có thể hash
    choices_tuple = tuple(tuple(pair) for pair in choices)
    n = len(choices_tuple)
    return count_palindromic_choices_helper(choices_tuple, 0, n - 1)

# Ví dụ: 3 vị trí, mỗi vị trí có 2 lựa chọn
choices_example = [('a', 'b'), ('a', 'b'), ('a', 'b')]
print(f"Số cách tạo chuỗi đối xứng từ {choices_example}: {count_palindromic_choices(choices_example)}")
print()

# ==================== Bài 4: Maximum Subarray bằng đệ quy ====================
@lru_cache(maxsize=None)
def max_subarray_sum(arr_tuple, start, end):
    # Chuyển arr thành tuple để có thể cache
    if start == end:
        return arr_tuple[start]
    
    # Chia dãy thành hai nửa
    mid = (start + end) // 2
    
    # Tổng lớn nhất ở nửa trái
    left_max = max_subarray_sum(arr_tuple, start, mid)
    # Tổng lớn nhất ở nửa phải
    right_max = max_subarray_sum(arr_tuple, mid + 1, end)
    
    # Tổng lớn nhất đi qua điểm giữa
    left_sum = float('-inf')
    current = 0
    for i in range(mid, start - 1, -1):
        current += arr_tuple[i]
        left_sum = max(left_sum, current)
    
    right_sum = float('-inf')
    current = 0
    for i in range(mid + 1, end + 1):
        current += arr_tuple[i]
        right_sum = max(right_sum, current)
    
    cross_max = left_sum + right_sum
    
    return max(left_max, right_max, cross_max)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr_tuple = tuple(arr)
max_sum = max_subarray_sum(arr_tuple, 0, len(arr_tuple) - 1)
print(f"Tổng lớn nhất của dãy con liên tiếp: {max_sum}")
print()

# ==================== Bài 5: Partition Problem ====================
@lru_cache(maxsize=None)
def can_partition(nums_tuple, index, target_sum, current_sum):
    # Nếu đã đạt tổng mục tiêu
    if current_sum == target_sum:
        return True
    # Nếu vượt quá hoặc đã xét hết
    if current_sum > target_sum or index >= len(nums_tuple):
        return False
    
    # Thử thêm phần tử hiện tại hoặc không
    return (can_partition(nums_tuple, index + 1, target_sum, current_sum + nums_tuple[index]) or
            can_partition(nums_tuple, index + 1, target_sum, current_sum))

nums = [1, 5, 11, 5]
total = sum(nums)
if total % 2 != 0:
    result = False
else:
    target = total // 2
    nums_tuple = tuple(nums)
    result = can_partition(nums_tuple, 0, target, 0)

print(f"Có thể chia {nums} thành 2 nhóm có tổng bằng nhau không? {result}")
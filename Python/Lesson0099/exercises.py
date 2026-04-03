import asyncio
import aiohttp
import time

# Bài tập 1: Viết một coroutine `wait_random`
# Nhận vào một tên và khoảng thời gian tối đa (max_delay)
# Chờ một khoảng thời gian ngẫu nhiên từ 0 đến max_delay, rồi in ra tên và thời gian đã chờ
# Gợi ý: dùng random.uniform(0, max_delay) và asyncio.sleep()
async def wait_random(name: str, max_delay: float):
    # TODO: Viết code tại đây
    pass

# Bài tập 2: Viết hàm `run_tasks_concurrently`
# Chạy 5 coroutine wait_random đồng thời với max_delay=3
# Đo thời gian tổng và in kết quả
async def run_tasks_concurrently():
    # TODO: Viết code tại đây
    pass

# Bài tập 3: Viết hàm `fetch_with_timeout`
# Tải một URL với thời gian chờ tối đa 2 giây
# Nếu quá thời gian thì in ra "Timeout", không ném lỗi
# Gợi ý: dùng asyncio.wait_for()
async def fetch_with_timeout(session, url):
    # TODO: Viết code tại đây
    pass

# Bài tập 4: Viết hàm `run_with_timeout_example`
# Tạo danh sách 3 URL (có thể dùng http://httpbin.org/delay/1, /delay/3, /json)
# Dùng fetch_with_timeout để tải đồng thời, xử lý timeout nếu có
async def run_with_timeout_example():
    # TODO: Viết code tại đây
    pass

# Bài tập 5 (nâng cao): Viết một máy chủ mô phỏng
# Tạo một danh sách hàng đợi các tác vụ (tên và độ trễ)
# Sử dụng một vòng lặp async để xử lý từng tác vụ theo thứ tự, nhưng không block
# In ra thời gian bắt đầu và kết thúc mỗi tác vụ
# Gợi ý: dùng asyncio.Queue
async def task_processor(tasks_queue):
    # TODO: Viết code tại đây
    pass

async def run_simulation():
    # Tạo hàng đợi và thêm một số tác vụ
    # Ví dụ: ("Task1", 1.0), ("Task2", 0.5)
    # TODO: Viết code tại đây
    pass
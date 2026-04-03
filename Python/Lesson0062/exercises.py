import asyncio
import aiohttp

# Bài tập 1: Kiểm tra trạng thái của nhiều URL
async def check_url_status(session, url):
    # TODO: Gọi URL và trả về tuple (url, status)
    pass

async def check_multiple_urls(urls):
    # TODO: Sử dụng aiohttp để kiểm tra trạng thái của danh sách URL
    # Trả về danh sách kết quả
    pass

# Bài tập 2: Tạo async generator cho dãy Fibonacci
async def async_fibonacci(n):
    # TODO: Dùng async yield để sinh n số Fibonacci
    # Mô phỏng I/O bằng await asyncio.sleep(0.05)
    pass

# Bài tập 3: Tải nội dung nhiều trang web song song
async def fetch_page_content(session, url):
    # TODO: Tải nội dung trang và trả về độ dài nội dung
    pass

async def fetch_all_pages(urls):
    # TODO: Tải song song và in ra độ dài nội dung mỗi trang
    pass

# Bài tập 4: Đo thời gian thực thi bằng async context manager
class AsyncExecutionTimer:
    def __init__(self, task_name):
        self.task_name = task_name

    async def __aenter__(self):
        # TODO: Ghi nhận thời gian bắt đầu
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # TODO: In ra thời gian thực thi
        pass

async def run_with_timer():
    async with AsyncExecutionTimer("Công việc mẫu"):
        await asyncio.sleep(1.5)

# Bài tập 5: Xử lý lỗi trong môi trường async
async def risky_task(task_id):
    # 50% khả năng lỗi
    if task_id % 2 == 0:
        await asyncio.sleep(1)
        return f"Task {task_id} thành công"
    else:
        await asyncio.sleep(1)
        raise Exception(f"Task {task_id} thất bại")

async def run_risky_tasks():
    # TODO: Chạy 5 tác vụ, bắt lỗi và in kết quả/thông báo lỗi
    pass
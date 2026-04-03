import asyncio
import aiohttp

# Bài tập 1: Viết hàm fetch_url để lấy nội dung từ URL
# Sử dụng aiohttp để gửi request bất đồng bộ
async def fetch_url(url):
    # TODO: Hoàn thiện hàm
    pass

# Bài tập 2: Đọc nhiều tệp tin bất đồng bộ
# Viết hàm read_files_async nhận danh sách tên tệp và trả về nội dung
async def read_files_async(file_list):
    # TODO: Hoàn thiện hàm
    pass

# Bài tập 3: Tạo máy chủ mô phỏng xử lý yêu cầu
# Viết hàm xử lý yêu cầu bất đồng bộ mô phỏng 3 tác vụ với độ trễ khác nhau
async def handle_request(request_id, delay):
    # TODO: In thông báo bắt đầu, đợi delay, in hoàn thành
    pass

async def process_requests(requests):
    # requests là danh sách tuple (id, delay)
    # TODO: Xử lý song song các yêu cầu
    pass

# Bài tập 4: In kết quả khi hoàn thành (dùng as_completed)
async def task_with_result(name, delay):
    # TODO: Chờ delay, trả về kết quả
    pass

async def run_in_order_of_completion():
    # TODO: Tạo các tác vụ và in kết quả theo thứ tự hoàn thành
    pass

# Bài tập 5: Giới hạn số lượng tác vụ chạy song song
async def limited_concurrent_tasks(tasks, limit):
    # TODO: Chạy tối đa `limit` tác vụ tại một thời điểm
    pass
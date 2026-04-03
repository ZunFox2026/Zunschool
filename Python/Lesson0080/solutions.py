import asyncio
import aiohttp
import random

# Bài tập 1: Viết hàm tải danh sách URL bất đồng bộ
async def fetch_urls(urls):
    # Tạo session chung để tiết kiệm tài nguyên
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            # Tạo tác vụ bất đồng bộ cho mỗi URL
            task = session.get(url)
            tasks.append(task)
        
        results = []
        # Thực hiện tất cả yêu cầu và lấy kết quả
        responses = await asyncio.gather(*tasks)
        for response in responses:
            content = await response.text()
            results.append(content)
        return results

# Bài tập 2: Tạo máy chủ xử lý yêu cầu bất đồng bộ (mô phỏng)
async def handle_request(request_id):
    delay = random.uniform(0.5, 2.0)  # Thời gian xử lý ngẫu nhiên
    print(f"Yêu cầu {request_id}: Bắt đầu xử lý (sẽ mất {delay:.2f}s)")
    await asyncio.sleep(delay)
    print(f"Yêu cầu {request_id}: Đã hoàn thành")

async def process_requests(request_ids):
    # Tạo danh sách tác vụ cho từng yêu cầu
    tasks = [handle_request(req_id) for req_id in request_ids]
    # Chạy song song tất cả các tác vụ
    await asyncio.gather(*tasks)

# Bài tập 3: Đếm ngược bất đồng bộ cho nhiều sự kiện
async def countdown(name, seconds):
    for i in range(seconds, 0, -1):
        print(f"{name}: {i}...")
        await asyncio.sleep(1)
    print(f"{name}: Xong!")

async def run_countdowns():
    # Tạo các tác vụ đếm ngược
    task_a = asyncio.create_task(countdown("A", 3))
    task_b = asyncio.create_task(countdown("B", 5))
    task_c = asyncio.create_task(countdown("C", 2))
    
    # Chờ tất cả hoàn thành
    await asyncio.gather(task_a, task_b, task_c)

# Bài tập 4: Xử lý ngoại lệ trong tác vụ bất đồng bộ
async def risky_fetch(session, url):
    async with session.get(url) as response:
        if response.status == 404:
            raise ValueError(f"Không tìm thấy: {url}")
        return await response.text()

async def fetch_with_error_handling(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            # Bao mỗi tác vụ trong một hàm con để xử lý lỗi riêng
            task = asyncio.create_task(safe_fetch(session, url))
            tasks.append(task)
        
        # Chờ tất cả tác vụ hoàn thành, dù có lỗi
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # In kết quả hoặc lỗi
        for url, result in zip(urls, results):
            if isinstance(result, Exception):
                print(f"Lỗi khi tải {url}: {result}")
            else:
                print(f"Tải thành công {url}, độ dài: {len(result)} ký tự")
        
        return results

async def safe_fetch(session, url):
    try:
        return await risky_fetch(session, url)
    except Exception as e:
        return e  # Trả về exception như một giá trị

# Bài tập 5: Đọc nhiều file văn bản lớn bất đồng bộ
async def read_file(filename):
    # Dùng to_thread để đọc file trong luồng nền, tránh chặn event loop
    return await asyncio.to_thread(read_file_sync, filename)

def read_file_sync(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[Lỗi: Không tìm thấy file {filename}]"

async def read_files_async(filenames):
    # Tạo tác vụ đọc file bất đồng bộ
    tasks = [read_file(filename) for filename in filenames]
    results = await asyncio.gather(*tasks)
    
    # In kết quả
    for filename, content in zip(filenames, results):
        print(f"--- Nội dung {filename} ---")
        print(content[:200] + ("..." if len(content) > 200 else ""))
    
    return results

# Hàm main để kiểm thử lời giải
async def main():
    print("=== Bài tập 1: Tải danh sách URL ===")
    urls = ["https://httpbin.org/json", "https://httpbin.org/get"]
    results = await fetch_urls(urls)
    for i, r in enumerate(results):
        print(f"Kết quả {i+1}: {len(r)} ký tự")
    
    print("\n=== Bài tập 2: Xử lý yêu cầu bất đồng bộ ===")
    await process_requests([1, 2, 3, 4])
    
    print("\n=== Bài tập 3: Đếm ngược bất đồng bộ ===")
    await run_countdowns()
    
    print("\n=== Bài tập 4: Xử lý lỗi bất đồng bộ ===")
    await fetch_with_error_handling([
        "https://httpbin.org/status/200",
        "https://httpbin.org/status/404",
        "https://httpbin.org/json"
    ])
    
    print("\n=== Bài tập 5: Đọc file bất đồng bộ ===")
    # Tạo file test trước khi chạy
    for i in range(1, 3):
        with open(f"test{i}.txt", "w", encoding="utf-8") as f:
            f.write(f"Đây là nội dung của test{i}.txt\n" * 100)
    await read_files_async(["test1.txt", "test2.txt", "not_exist.txt"])

if __name__ == "__main__":
    asyncio.run(main())
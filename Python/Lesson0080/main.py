import asyncio
import aiohttp
import time

# Ví dụ 1: Gọi nhiều API cùng lúc
async def fetch_data(session, url):
    print(f"Đang tải dữ liệu từ {url}")
    async with session.get(url) as response:
        result = await response.text()
        print(f"Đã tải xong từ {url}, độ dài: {len(result)} ký tự")
        return result

async def fetch_multiple_apis():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/json"
    ]
    async with aiohttp.ClientSession() as session:
        # Chạy tất cả các tác vụ cùng lúc
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Ví dụ 2: Tải đồng thời nhiều file
async def download_file(session, url, filename):
    print(f"Bắt đầu tải {filename}...")
    async with session.get(url) as response:
        content = await response.read()
        with open(filename, "wb") as f:
            f.write(content)
        print(f"Hoàn tất tải {filename}, kích thước: {len(content)} bytes")

async def download_multiple_files():
    files = [
        ("https://httpbin.org/bytes/1024", "file1.bin"),
        ("https://httpbin.org/bytes/2048", "file2.bin"),
        ("https://httpbin.org/bytes/512", "file3.bin")
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [
            download_file(session, url, filename)
            for url, filename in files
        ]
        await asyncio.gather(*tasks)

# Ví dụ 3: Xử lý tác vụ mô phỏng với thời gian chờ khác nhau
async def task_with_delay(name, delay):
    print(f"{name}: Bắt đầu")
    await asyncio.sleep(delay)
    print(f"{name}: Hoàn thành sau {delay} giây")
    return f"Kết quả từ {name}"

async def run_simulation():
    print("Bắt đầu mô phỏng 3 tác vụ bất đồng bộ")
    start_time = time.time()
    
    # Chạy song song 3 tác vụ
    results = await asyncio.gather(
        task_with_delay("Tác vụ 1", 2),
        task_with_delay("Tác vụ 2", 1),
        task_with_delay("Tác vụ 3", 3)
    )
    
    end_time = time.time()
    print(f"Tất cả tác vụ hoàn thành trong {end_time - start_time:.2f} giây")
    print("Kết quả:", results)

# Hàm chính để chạy các ví dụ
async def main():
    print("=== Ví dụ 1: Gọi nhiều API cùng lúc ===")
    await fetch_multiple_apis()
    
    print("\n=== Ví dụ 2: Tải đồng thời nhiều file ===")
    await download_multiple_files()
    
    print("\n=== Ví dụ 3: Mô phỏng tác vụ với thời gian chờ ===")
    await run_simulation()

# Chạy chương trình chính
if __name__ == "__main__":
    asyncio.run(main())
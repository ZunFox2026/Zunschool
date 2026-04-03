import asyncio
import aiohttp

# Ví dụ 1: Gọi API bất đồng bộ
async def fetch_url(session, url):
    async with session.get(url) as response:
        return f"{url}: {response.status}"

async def fetch_multiple_urls():
    urls = [
        'http://httpbin.org/status/200',
        'http://httpbin.org/status/201',
        'http://httpbin.org/status/404',
        'http://httpbin.org/status/500'
    ]
    async with aiohttp.ClientSession() as session:
        # Chạy nhiều tác vụ song song
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

# Ví dụ 2: Đọc nhiều file bất đồng bộ (mô phỏng)
async def read_file(filename):
    print(f"Đang đọc {filename}...")
    await asyncio.sleep(1)  # Mô phỏng thời gian đọc file
    return f"Nội dung từ {filename}"

async def read_all_files():
    filenames = [f"file_{i}.txt" for i in range(1, 6)]
    # Đọc song song
    contents = await asyncio.gather(*[read_file(name) for name in filenames])
    for content in contents:
        print(content)

# Ví dụ 3: async for và async with
class AsyncFibonacci:
    def __init__(self, max_n):
        self.max_n = max_n

    def __aiter__(self):
        self.a, self.b = 0, 1
        self.count = 0
        return self

    async def __anext__(self):
        if self.count >= self.max_n:
            raise StopAsyncIteration
        self.count += 1
        await asyncio.sleep(0.1)  # Mô phỏng I/O nhẹ
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current

async def use_async_for():
    print("Dãy Fibonacci (async):")
    async for num in AsyncFibonacci(10):
        print(num, end=' ')
    print()

# Context manager bất đồng bộ
class AsyncTimer:
    def __init__(self, name):
        self.name = name

    async def __aenter__(self):
        self.start = asyncio.get_event_loop().time()
        print(f"Bắt đầu đo: {self.name}")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.end = asyncio.get_event_loop().time()
        print(f"{self.name} hoàn tất trong {self.end - self.start:.2f} giây")

async def use_async_with():
    async with AsyncTimer("Thử nghiệm async"):
        await asyncio.sleep(2)

# Chạy các ví dụ
async def main():
    print("=== Ví dụ 1: Gọi nhiều API ===")
    await fetch_multiple_urls()

    print("\n=== Ví dụ 2: Đọc nhiều file ===")
    await read_all_files()

    print("\n=== Ví dụ 3: async for và async with ===")
    await use_async_for()
    await use_async_with()

# Chạy chương trình chính
def run_examples():
    asyncio.run(main())

if __name__ == "__main__":
    run_examples()
import asyncio
import aiohttp

# Ví dụ 1: Tải nhiều trang web song song
async def fetch_url(session, url):
    async with session.get(url) as response:
        content = await response.text()
        print(f"{url}: {len(content)} ký tự")
        return len(content)

async def fetch_multiple_urls():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1"
    ]
    async with aiohttp.ClientSession() as session:
        # Chạy song song các yêu cầu
        await asyncio.gather(
            *[fetch_url(session, url) for url in urls]
        )

# Ví dụ 2: Xử lý nhiều tác vụ I/O mô phỏng
async def slow_task(name, delay):
    print(f"Tác vụ {name} bắt đầu")
    await asyncio.sleep(delay)
    print(f"Tác vụ {name} hoàn thành sau {delay}s")

async def run_multiple_tasks():
    # Chạy 3 tác vụ chậm song song
    await asyncio.gather(
        slow_task("A", 2),
        slow_task("B", 1),
        slow_task("C", 3)
    )

# Ví dụ 3: Máy chủ TCP đơn giản với asyncio
async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    print(f"Nhận được: {message}")

    writer.write(data)
    await writer.drain()
    writer.close()

async def start_server():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    print("Máy chủ đang chạy tại 127.0.0.1:8888")
    async with server:
        await server.serve_forever()

# Hàm chính để chạy các ví dụ
async def main():
    print("=== Ví dụ 1: Tải nhiều URL song song ===")
    await fetch_multiple_urls()

    print("\n=== Ví dụ 2: Chạy nhiều tác vụ chậm song song ===")
    await run_multiple_tasks()

    print("\n=== Ví dụ 3: Máy chủ TCP (sẽ chạy 5s rồi dừng) ===")
    # Chạy máy chủ trong 5 giây rồi dừng
    server_task = asyncio.create_task(start_server())
    await asyncio.sleep(5)
    server_task.cancel()
    try:
        await server_task
    except asyncio.CancelledError:
        print("Máy chủ đã bị hủy.")

if __name__ == "__main__":
    asyncio.run(main())
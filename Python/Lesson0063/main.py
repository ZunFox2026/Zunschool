import asyncio
import aiohttp
import time

# Ví dụ 1: Chào hỏi không đồng bộ
async def say_hello(name):
    await asyncio.sleep(1)  # Tạm dừng 1 giây mà không chặn chương trình
    print(f"Xin chào, {name}!")

# Ví dụ 2: Tải nhiều trang web song song
async def fetch_url(session, url):
    async with session.get(url) as response:
        text = await response.text()
        print(f"Đã tải {url}, độ dài: {len(text)} ký tự")
        return len(text)

async def fetch_multiple_urls():
    urls = [
        "http://httpbin.org/delay/1",
        "http://httpbin.org/delay/2",
        "http://httpbin.org/json"
    ]
    async with aiohttp.ClientSession() as session:
        # Chạy song song các yêu cầu
        await asyncio.gather(*[fetch_url(session, url) for url in urls])

# Ví dụ 3: Đọc nhiều tệp bất đồng bộ
async def read_file(filename):
    # Dùng run_in_executor để đọc tệp trong luồng nền
    loop = asyncio.get_event_loop()
    try:
        content = await loop.run_in_executor(None, lambda: open(filename, 'r').read())
        print(f"Đọc xong {filename}, {len(content)} ký tự")
        return content
    except FileNotFoundError:
        print(f"Không tìm thấy tệp: {filename}")
        return None

async def read_files_async(filenames):
    await asyncio.gather(*[read_file(f) for f in filenames])

# Hàm chính để chạy các ví dụ
async def main():
    print("=== Ví dụ 1: Chào hỏi bất đồng bộ ===")
    await say_hello("An")

    print("\n=== Ví dụ 2: Tải nhiều URL song song ===")
    start = time.time()
    await fetch_multiple_urls()
    print(f"Thời gian tải: {time.time() - start:.2f} giây")

    print("\n=== Ví dụ 3: Đọc nhiều tệp bất đồng bộ ===")
    # Tạo tệp mẫu trước
    with open("file1.txt", "w") as f:
        f.write("Nội dung tệp 1 rất dài... " * 100)
    with open("file2.txt", "w") as f:
        f.write("Nội dung tệp 2 rất dài... " * 100)
    with open("file3.txt", "w") as f:
        f.write("Nội dung tệp 3 rất dài... " * 100)

    await read_files_async(["file1.txt", "file2.txt", "file3.txt"])

# Chạy chương trình
if __name__ == "__main__":
    asyncio.run(main())
import asyncio
import aiofiles  # Cần cài đặt: pip install aiofiles

# --- Ví dụ 1: Gọi nhiều API đồng thời ---
async def fetch_data(name, delay):
    """
    Mô phỏng việc gọi API với tên và độ trễ
    """
    print(f"[API] Bắt đầu tải dữ liệu: {name}")
    await asyncio.sleep(delay)  # Giả lập thời gian chờ mạng
    print(f"[API] Hoàn thành: {name}")
    return f"Dữ liệu từ {name}"

async def example_1():
    print("=== Ví dụ 1: Gọi nhiều API đồng thời ===")
    # Chạy 3 tác vụ bất đồng bộ cùng lúc
    results = await asyncio.gather(
        fetch_data("Dữ liệu người dùng", 2),
        fetch_data("Dữ liệu sản phẩm", 1),
        fetch_data("Dữ liệu đơn hàng", 3)
    )
    print("Tất cả dữ liệu đã nhận:")
    for result in results:
        print(result)

# --- Ví dụ 2: Đọc nhiều file bất đồng bộ ---
async def read_file_async(filename):
    """
    Đọc nội dung file một cách bất đồng bộ
    """
    try:
        async with aiofiles.open(filename, 'r', encoding='utf-8') as f:
            content = await f.read()
            print(f"[File] Đã đọc xong {filename}: {len(content)} ký tự")
            return content
    except FileNotFoundError:
        print(f"[Lỗi] Không tìm thấy file: {filename}")
        return None

async def example_2():
    print("\n=== Ví dụ 2: Đọc nhiều file bất đồng bộ ===")
    # Tạo 2 file mẫu để đọc
    sample_files = ["file1.txt", "file2.txt"]
    contents = ["Đây là nội dung file 1.\nDòng thứ hai.\n", "File 2 có nội dung khác.\nDòng mới.\n"]
    for fname, content in zip(sample_files, contents):
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Đọc bất đồng bộ
    results = await asyncio.gather(
        read_file_async("file1.txt"),
        read_file_async("file2.txt")
    )
    print("Hoàn thành đọc tất cả file.")

# --- Ví dụ 3: Mô phỏng máy in dùng hàng đợi bất đồng bộ ---
async def printer_task(queue):
    """
    Nhiệm vụ in: lấy tài liệu từ hàng đợi và in
    """
    while True:
        document = await queue.get()  # Lấy tài liệu từ queue
        if document is None:
            break  # Dừng nếu nhận được tín hiệu kết thúc
        print(f"🖨️  Đang in: '{document}'...")
        await asyncio.sleep(2)  # Thời gian in
        print(f"✅ In xong: '{document}'")
        queue.task_done()

async def user_submit(queue, user_name, doc_name):
    """
    Người dùng gửi tài liệu in
    """
    print(f"📤 {user_name} gửi in: '{doc_name}'")
    await queue.put(doc_name)

async def example_3():
    print("\n=== Ví dụ 3: Mô phỏng máy in bất đồng bộ ===")
    queue = asyncio.Queue()

    # Tạo tác vụ in (luôn chạy)
    printer = asyncio.create_task(printer_task(queue))

    # Người dùng gửi in
    await user_submit(queue, "An", "Báo cáo Q3.pdf")
    await user_submit(queue, "Bình", "Hợp đồng.txt")
    await user_submit(queue, "Chi", "Slide thuyết trình.pptx")

    # Đợi tất cả tài liệu được in xong
    await queue.join()

    # Dừng tác vụ in
    await queue.put(None)
    await printer

# Hàm chính chạy tất cả ví dụ
async def main():
    await example_1()
    await example_2()
    await example_3()

if __name__ == "__main__":
    asyncio.run(main())
# Bài học Python số 62: Xử lý bất đồng bộ với asyncio (Cấp độ nâng cao)

## Mục tiêu bài học
- Hiểu được khái niệm bất đồng bộ (asynchronous programming) và tại sao nó quan trọng.
- Nắm vững cách sử dụng thư viện `asyncio` để viết code bất đồng bộ.
- Biết cách định nghĩa và gọi hàm async, sử dụng `await`, `async for`, `async with`.
- Áp dụng `asyncio` vào các tác vụ thực tế như gọi API, xử lý file, mô phỏng I/O.

## Lý thuyết chi tiết

### 1. Bất đồng bộ là gì?
Trong lập trình đồng bộ (synchronous), các lệnh được thực thi tuần tự: lệnh này phải hoàn thành trước khi lệnh kia bắt đầu. Điều này gây lãng phí tài nguyên nếu có các tác vụ chờ đợi như gọi API, đọc file, kết nối mạng.

Lập trình bất đồng bộ cho phép chương trình tiếp tục thực hiện các công việc khác trong khi chờ một tác vụ hoàn tất. Python hỗ trợ bất đồng bộ thông qua mô hình **event loop** và từ khóa `async`/`await`.

### 2. Các khái niệm chính
- **`async def`**: Khai báo một hàm bất đồng bộ (gọi là *coroutine*).
- **`await`**: Dừng tạm thời việc thực thi hàm async cho đến khi một coroutine khác hoàn tất.
- **Event loop**: Vòng lặp sự kiện quản lý việc thực thi các coroutine.
- **`asyncio.run()`**: Hàm chính để chạy một coroutine ở cấp cao nhất.

### 3. Ưu điểm
- Tăng hiệu suất khi xử lý nhiều tác vụ I/O.
- Tiết kiệm tài nguyên so với đa luồng (threading) trong nhiều trường hợp.

### 4. Khi nào nên dùng?
- Gọi nhiều API cùng lúc.
- Đọc/ghi nhiều file.
- Xử lý nhiều yêu cầu mạng.

### 5. Ví dụ cơ bản
```python
import asyncio

async def say_hello():
    print("Bắt đầu...")
    await asyncio.sleep(1)  # Mô phỏng tác vụ I/O
    print("Xong sau 1 giây")

asyncio.run(say_hello())
```

## Ví dụ minh họa

### Ví dụ 1: Gọi API bất đồng bộ
Sử dụng `aiohttp` để gọi nhiều API cùng lúc.

### Ví dụ 2: Đọc nhiều file bất đồng bộ
Mô phỏng đọc file với `asyncio.sleep()`.

### Ví dụ 3: Sử dụng `async for` và `async with`
Tạo một async iterator và async context manager.

## Bài tập thực hành
1. Viết một hàm async kiểm tra trạng thái của nhiều URL.
2. Tạo một async generator để sinh số Fibonacci.
3. Viết chương trình tải về nội dung của 5 trang web song song.
4. Tạo một async context manager để đo thời gian thực thi.
5. Xử lý lỗi trong môi trường async.

## Tổng kết
`asyncio` là công cụ mạnh mẽ để xử lý các tác vụ I/O một cách hiệu quả. Việc sử dụng đúng cách `async`/`await` giúp chương trình nhanh hơn, đặc biệt khi làm việc với mạng hoặc file. Tuy nhiên, cần lưu ý rằng không phải mọi bài toán đều phù hợp với bất đồng bộ — các tác vụ tính toán nặng vẫn nên dùng đa tiến trình (multiprocessing).
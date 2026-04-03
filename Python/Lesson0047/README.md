# Bài học 47: Lập trình bất đồng bộ với asyncio (Nâng cao)

## Mục tiêu bài học
- Hiểu rõ khái niệm bất đồng bộ (asynchronous programming) và tại sao nó quan trọng.
- Nắm vững cách sử dụng `async` và `await` trong Python.
- Biết cách tạo và quản lý các tác vụ bất đồng bộ bằng `asyncio.Task`.
- Áp dụng kiến thức vào các tình huống thực tế như gọi API song song, xử lý I/O chậm.

## Lý thuyết chi tiết

### 1. Bất đồng bộ là gì?
Trong lập trình đồng bộ, các lệnh được thực thi tuần tự: lệnh này xong mới đến lệnh kia. Nếu một lệnh tốn thời gian (ví dụ: gọi API, đọc file lớn), chương trình sẽ bị **chặn** (blocking) cho đến khi xong.

Lập trình bất đồng bộ cho phép chương trình **tiếp tục làm việc khác** trong lúc chờ các thao tác chậm hoàn tất. Điều này rất hiệu quả khi xử lý nhiều tác vụ I/O.

### 2. async và await
- `async def` định nghĩa một **hàm bất đồng bộ** (coroutine).
- `await` dùng để **chờ** một coroutine hoàn thành, nhưng **không chặn toàn bộ chương trình**.

```python
async def ham_bat_dong_bo():
    await asyncio.sleep(1)  # mô phỏng thao tác chậm
    print("Hoàn thành!")
```

### 3. Event Loop và asyncio
- `asyncio` là thư viện chuẩn của Python để xử lý bất đồng bộ.
- **Event loop** là trái tim của asyncio: nó quản lý và chạy các coroutine.
- Dùng `asyncio.run()` để chạy một coroutine chính.

### 4. Task và gather
- `asyncio.create_task()` tạo một task chạy nền.
- `asyncio.gather()` chạy nhiều coroutine song song và chờ tất cả hoàn thành.

---

## Ví dụ minh họa

### Ví dụ 1: Gọi API song song
Giả sử bạn cần lấy dữ liệu từ 3 API. Nếu gọi tuần tự, mất 3 giây. Nếu bất đồng bộ, chỉ mất ~1 giây.

### Ví dụ 2: Xử lý nhiều file cùng lúc
Đọc nhiều file lớn mà không chặn chương trình.

### Ví dụ 3: Máy chủ phản hồi nhanh hơn với bất đồng bộ
Dùng trong web server (FastAPI) hoặc bot (Discord bot), nơi cần xử lý nhiều yêu cầu.

---

## Bài tập thực hành
1. Viết hàm bất đồng bộ `tai_xuong(url)` mô phỏng tải một file từ URL.
2. Dùng `asyncio.gather()` để tải 5 URL cùng lúc.
3. Tạo 3 task bất đồng bộ: một ngủ 1s, một ngủ 2s, một in "Bắt đầu", rồi in tổng thời gian thực thi.
4. Viết hàm `thuc_hien_song_song(danh_sach_ham)` nhận danh sách các coroutine và chạy song song.
5. Xử lý lỗi trong coroutine: dùng `try/except` trong `async def`.

**Gợi ý:**
- Dùng `asyncio.sleep()` để mô phỏng độ trễ.
- Dùng `asyncio.create_task()` để chạy song song.
- Đo thời gian với `time.time()`.

---

## Tổng kết
- Lập trình bất đồng bộ giúp tối ưu hiệu suất khi xử lý I/O.
- `async/await` là công cụ mạnh, nhưng chỉ hiệu quả khi dùng đúng ngữ cảnh (không dùng cho xử lý CPU nặng).
- `asyncio.gather()` giúp chạy nhiều tác vụ song song dễ dàng.
- Luôn nhớ: **chỉ `await` trong hàm `async`**, và dùng `asyncio.run()` để khởi chạy chương trình.

Kiến thức này cực kỳ quan trọng khi làm việc với web scraping, API, server, game, hoặc bất kỳ ứng dụng nào cần phản hồi nhanh.
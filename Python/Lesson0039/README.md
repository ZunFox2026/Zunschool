# Bài học Python số 39 - Cấp độ Trung cấp

## Chủ đề: Làm việc với `datetime` và xử lý ngày giờ trong Python

Trong thế giới lập trình, việc xử lý ngày giờ là một nhu cầu rất phổ biến: từ việc ghi log, lập lịch công việc, tính toán thời gian trôi qua, đến hiển thị giờ theo múi giờ khác nhau. Python cung cấp module `datetime` mạnh mẽ để giúp chúng ta làm việc với ngày, giờ một cách dễ dàng và chính xác.

Bài học này sẽ giúp bạn nắm vững cách sử dụng module `datetime`, làm việc với múi giờ (timezone), định dạng ngày giờ và giải quyết các vấn đề thực tế liên quan đến thời gian.

---

## Mục tiêu bài học

- Hiểu được cấu trúc và các lớp cơ bản trong module `datetime`.
- Biết cách tạo, truy xuất và định dạng ngày giờ.
- Xử lý khoảng thời gian với `timedelta`.
- Làm việc với múi giờ (timezone-aware datetime).
- Ứng dụng vào các tình huống thực tế như tính tuổi, lập lịch, chuyển đổi múi giờ.

---

## Lý thuyết chi tiết

### 1. Các lớp chính trong `datetime`

- `datetime.date`: đại diện cho một ngày (năm, tháng, ngày).
- `datetime.time`: đại diện cho một thời điểm trong ngày (giờ, phút, giây, microsecond).
- `datetime.datetime`: kết hợp cả ngày và giờ.
- `datetime.timedelta`: đại diện cho khoảng thời gian (ví dụ: 5 ngày, 3 giờ).
- `datetime.timezone`: hỗ trợ làm việc với múi giờ.

### 2. Tạo đối tượng ngày giờ

```python
from datetime import datetime, date, time, timedelta, timezone

# Lấy thời gian hiện tại
now = datetime.now()

# Tạo datetime cụ thể
dt = datetime(2025, 7, 15, 14, 30, 0)

# Tạo ngày
d = date(2025, 7, 15)

# Tạo thời gian
t = time(14, 30, 0)
```

### 3. Định dạng và chuyển đổi chuỗi

Dùng `.strftime()` để chuyển `datetime` thành chuỗi, `.strptime()` để chuyển chuỗi thành `datetime`.

```python
# Định dạng thành chuỗi
dt.strftime("%d/%m/%Y %H:%M")

# Chuyển từ chuỗi sang datetime
datetime.strptime("15/07/2025 14:30", "%d/%m/%Y %H:%M")
```

### 4. Tính toán với `timedelta`

```python
# Cộng/trừ thời gian
ngay_hom_qua = now - timedelta(days=1)
5_ngay_sau = now + timedelta(days=5)
```

### 5. Làm việc với múi giờ

```python
# Tạo datetime có múi giờ
tz_hcm = timezone(timedelta(hours=7))
dt_hcm = datetime(2025, 7, 15, 14, 30, tzinfo=tz_hcm)
```

---

## Ví dụ minh họa

### Ví dụ 1: Tính tuổi từ ngày sinh

Tính tuổi chính xác theo năm, tháng, ngày.

### Ví dụ 2: Chuyển đổi múi giờ

Chuyển thời gian từ múi giờ Việt Nam (UTC+7) sang múi giờ New York (UTC-4).

### Ví dụ 3: Lập lịch nhắc nhở

Tạo chương trình nhắc nhở một sự kiện sau một khoảng thời gian nhất định.

---

## Bài tập thực hành

1. Viết hàm tính số ngày còn lại đến Tết Dương lịch 2026.
2. Viết hàm kiểm tra một ngày có phải cuối tuần không.
3. Viết chương trình tính thời gian làm việc giữa hai thời điểm (trừ giờ nghỉ).
4. Chuyển đổi một chuỗi thời gian từ định dạng "15-07-2025 20:30" sang đối tượng datetime.
5. Viết hàm trả về thời gian hiện tại ở 3 múi giờ khác nhau: Việt Nam, London, Tokyo.

---

## Tổng kết

Module `datetime` là một công cụ thiết yếu trong Python để xử lý ngày giờ. Việc nắm vững cách tạo, định dạng, tính toán và làm việc với múi giờ sẽ giúp bạn xử lý nhiều bài toán thực tế như lập lịch, thống kê, ghi log hay xây dựng ứng dụng theo dõi thời gian. Hãy luyện tập thường xuyên để thuần thục các thao tác với `datetime`.

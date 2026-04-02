# Tìm chữ cái thường
## Giới thiệu
Bài học này旨在 giúp bạn hiểu cách tìm và xử lý chữ cái thường trong Python. Chữ cái thường là những ký tự được sử dụng để đại diện cho âm thanh hoặc hình dạng trong ngôn ngữ. Trong Python, chúng ta có thể dễ dàng tìm và xử lý chữ cái thường bằng cách sử dụng các phương thức và hàm có sẵn.

## Lý thuyết
Trong Python, chúng ta có thể sử dụng phương thức `islower()` để kiểm tra xem một ký tự có phải là chữ cái thường hay không. Phương thức này trả về `True` nếu ký tự là chữ cái thường và `False` otherwise.

Ví dụ:
- 'a' là chữ cái thường vì nó là một ký tự đại diện cho âm thanh trong ngôn ngữ.
- 'A' không phải là chữ cái thường vì nó là một ký tự in hoa.

Chúng ta cũng có thể sử dụng hàm `lower()` để chuyển đổi một chuỗi chữ cái thành chữ cái thường.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách tìm và xử lý chữ cái thường trong Python:
- Kiểm tra xem một ký tự có phải là chữ cái thường hay không:
  - `print('a'.islower())` sẽ trả về `True`.
  - `print('A'.islower())` sẽ trả về `False`.
- Chuyển đổi một chuỗi chữ cái thành chữ cái thường:
  - `print('ABC'.lower())` sẽ trả về `'abc'`.
- Tìm tất cả các chữ cái thường trong một chuỗi:
  - `chuoi = 'Hello World'`
  - `chu_cai_thuong = [ky_tu for ky_tu in chuoi if ky_tu.islower()]`
  - `print(chu_cai_thuong)` sẽ trả về `['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']`.

## Bài tập
Bài tập này yêu cầu bạn viết một chương trình Python để tìm tất cả các chữ cái thường trong một chuỗi nhập vào từ người dùng.
- Yêu cầu người dùng nhập vào một chuỗi.
- Sử dụng phương thức `islower()` để kiểm tra xem mỗi ký tự trong chuỗi có phải là chữ cái thường hay không.
- In ra tất cả các chữ cái thường tìm thấy trong chuỗi.
- Chuyển đổi toàn bộ chuỗi thành chữ cái thường và in ra kết quả.
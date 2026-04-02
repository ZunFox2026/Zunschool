# Làm quen với thư viện Tkinter

## Giới thiệu
Tkinter là một thư viện GUI (Graphical User Interface) được tích hợp sẵn trong Python, cho phép bạn tạo các ứng dụng giao diện người dùng đồ họa. Với Tkinter, bạn có thể tạo các ứng dụng đơn giản như máy tính, chương trình ghi chú, đến các ứng dụng phức tạp hơn như trình duyệt web, trò chơi. Tkinter cung cấp các công cụ cần thiết để tạo và quản lý giao diện người dùng, bao gồm các nút bấm, ô nhập liệu, hộp thoại, v.v.

## Lý thuyết
Để bắt đầu với Tkinter, bạn cần tạo một cửa sổ chính (root window) bằng cách gọi hàm `Tk()`. Từ đó, bạn có thể tạo các widget (các thành phần giao diện người dùng) như `Label`, `Button`, `Entry`, v.v. và thêm chúng vào cửa sổ chính. Tkinter cũng cung cấp các phương thức để quản lý sự kiện, chẳng hạn như khi người dùng nhấp vào nút bấm hoặc nhập liệu vào ô nhập liệu.

Ví dụ, để tạo một nút bấm với nội dung "Xin chào", bạn có thể sử dụng đoạn mã sau:
```python
import tkinter as tk

root = tk.Tk()
button = tk.Button(root, text="Xin chào")
button.pack()
root.mainloop()
```

## Ví dụ
Dưới đây là một ví dụ minh họa về việc tạo một ứng dụng đơn giản với Tkinter. Ứng dụng này sẽ có một ô nhập liệu để người dùng nhập tên, và một nút bấm để chào hỏi người dùng.
```python
import tkinter as tk

def chao_hoi():
    ten = entry.get()
    label.config(text=f"Xin chào, {ten}!")

root = tk.Tk()
root.title("Ứng dụng chào hỏi")

label = tk.Label(root, text="Nhập tên của bạn:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Chào hỏi", command=chao_hoi)
button.pack()

root.mainloop()
```
Khi người dùng nhập tên vào ô nhập liệu và nhấp vào nút bấm, ứng dụng sẽ hiển thị lời chào hỏi với tên của người dùng.

## Bài tập
Bài tập cho bạn là tạo một ứng dụng đơn giản với Tkinter, bao gồm:
* Một ô nhập liệu để người dùng nhập tuổi
* Một nút bấm để hiển thị thông báo "Bạn đã trưởng thành" nếu người dùng nhập tuổi từ 18 trở lên, và "Bạn chưa trưởng thành" nếu người dùng nhập tuổi dưới 18
* Một nút bấm để thoát khỏi ứng dụng

Hãy thử tạo ứng dụng này và xem kết quả!
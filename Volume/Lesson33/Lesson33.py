# Import thư viện tkinter
from tkinter import *

# Tạo cửa sổ chính
root = Tk()
root.title("Làm quen với thư viện tkinter")

# Thêm tiêu đề cho cửa sổ
label = Label(root, text="Xin chào, tôi là cửa sổ tkinter!", font=("Arial", 24))
label.pack(pady=20)

# Thêm nút bấm
def click():
    # In thông báo khi nút được bấm
    print("Nút đã được bấm!")

button = Button(root, text="Bấm vào đây", command=click)
button.pack(pady=10)

# Thêm trường nhập liệu
def submit():
    # In giá trị nhập vào khi nút được bấm
    print("Bạn đã nhập:", entry.get())

entry = Entry(root, width=50)
entry.pack(pady=10)

submit_button = Button(root, text="Gửi", command=submit)
submit_button.pack(pady=10)

# Chạy cửa sổ
root.mainloop()
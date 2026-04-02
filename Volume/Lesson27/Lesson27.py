# Bài 27: Làm quen với thư viện Requests

# Thư viện Requests giúp chúng ta gửi các yêu cầu HTTP đến một trang web
import requests

# Gửi yêu cầu GET đến trang web
def gui_yeu_cau_get(url):
    # Sử dụng phương thức get() để gửi yêu cầu GET
    response = requests.get(url)
    
    # Kiểm tra trạng thái của yêu cầu
    if response.status_code == 200:
        # Nếu yêu cầu thành công, in ra nội dung của trang web
        print("Yêu cầu thành công!")
        print(response.text)
    else:
        # Nếu yêu cầu không thành công, in ra thông báo lỗi
        print("Yêu cầu không thành công!")

# Gửi yêu cầu POST đến trang web
def gui_yeu_cau_post(url, data):
    # Sử dụng phương thức post() để gửi yêu cầu POST
    response = requests.post(url, data=data)
    
    # Kiểm tra trạng thái của yêu cầu
    if response.status_code == 200:
        # Nếu yêu cầu thành công, in ra nội dung của trang web
        print("Yêu cầu thành công!")
        print(response.text)
    else:
        # Nếu yêu cầu không thành công, in ra thông báo lỗi
        print("Yêu cầu không thành công!")

# Ví dụ sử dụng
url = "https://www.google.com"
gui_yeu_cau_get(url)

url_post = "https://httpbin.org/post"
data = {"key": "value"}
gui_yeu_cau_post(url_post, data)
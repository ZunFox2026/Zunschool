# Bài 25: Làm quen với thư viện Requests

# Thư viện requests giúp chúng ta gửi các yêu cầu HTTP đến server và nhận lại phản hồi
import requests

# Gửi yêu cầu GET đến địa chỉ URL
def gui_yeu_cau_get():
    # Địa chỉ URL mà chúng ta muốn gửi yêu cầu đến
    url = "https://www.google.com"
    
    # Gửi yêu cầu GET
    response = requests.get(url)
    
    # In ra trạng thái của yêu cầu (200 là thành công)
    print("Trạng thái yêu cầu:", response.status_code)
    
    # In ra nội dung phản hồi từ server
    print("Nội dung phản hồi:\n", response.text)

# Gửi yêu cầu POST đến địa chỉ URL
def gui_yeu_cau_post():
    # Địa chỉ URL mà chúng ta muốn gửi yêu cầu đến
    url = "https://httpbin.org/post"
    
    # Dữ liệu mà chúng ta muốn gửi đi
    data = {"key": "value"}
    
    # Gửi yêu cầu POST
    response = requests.post(url, data=data)
    
    # In ra trạng thái của yêu cầu (200 là thành công)
    print("Trạng thái yêu cầu:", response.status_code)
    
    # In ra nội dung phản hồi từ server
    print("Nội dung phản hồi:\n", response.text)

# Ví dụ sử dụng
if __name__ == "__main__":
    # Gửi yêu cầu GET
    gui_yeu_cau_get()
    
    # Gửi yêu cầu POST
    gui_yeu_cau_post()
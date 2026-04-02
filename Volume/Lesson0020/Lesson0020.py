# Import thư viện requests
import requests

# Gửi yêu cầu GET đến địa chỉ https://www.google.com
def gui_yeu_cau_get():
    url = "https://www.google.com"
    # Sử dụng requests.get để gửi yêu cầu GET
    response = requests.get(url)
    
    # In mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In nội dung của yêu cầu
    print("Nội dung:", response.text)

# Gửi yêu cầu POST đến địa chỉ https://httpbin.org/post
def gui_yeu_cau_post():
    url = "https://httpbin.org/post"
    # Dữ liệu sẽ được gửi trong yêu cầu POST
    data = {"key": "value"}
    
    # Sử dụng requests.post để gửi yêu cầu POST
    response = requests.post(url, data=data)
    
    # In mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In nội dung của yêu cầu
    print("Nội dung:", response.text)

# Gửi yêu cầu GET với tham số đến địa chỉ https://httpbin.org/get
def gui_yeu_cau_get_voi_tham_so():
    url = "https://httpbin.org/get"
    # Dữ liệu sẽ được gửi trong yêu cầu GET
    params = {"key": "value"}
    
    # Sử dụng requests.get để gửi yêu cầu GET với tham số
    response = requests.get(url, params=params)
    
    # In mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In nội dung của yêu cầu
    print("Nội dung:", response.text)

# Gọi các hàm để minh họa
gui_yeu_cau_get()
gui_yeu_cau_post()
gui_yeu_cau_get_voi_tham_so()
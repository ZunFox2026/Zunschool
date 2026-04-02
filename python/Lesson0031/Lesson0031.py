# Bài 31: Làm quen với thư viện requests

# Import thư viện requests
import requests

# Gửi yêu cầu GET đến địa chỉ URL
def gui_yeu_cau_get():
    # Địa chỉ URL
    url = "https://www.google.com"
    
    # Gửi yêu cầu GET
    response = requests.get(url)
    
    # In mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In nội dung của yêu cầu
    print("Nội dung:", response.text)

# Gửi yêu cầu POST đến địa chỉ URL
def gui_yeu_cau_post():
    # Địa chỉ URL
    url = "https://httpbin.org/post"
    
    # Dữ liệu được gửi đi
    data = {"key": "value"}
    
    # Gửi yêu cầu POST
    response = requests.post(url, data=data)
    
    # In mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In nội dung của yêu cầu
    print("Nội dung:", response.text)

# Gửi yêu cầu GET với tham số đến địa chỉ URL
def gui_yeu_cau_get_voi_tham_so():
    # Địa chỉ URL
    url = "https://httpbin.org/get"
    
    # Tham số
    params = {"key": "value"}
    
    # Gửi yêu cầu GET
    response = requests.get(url, params=params)
    
    # In mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In nội dung của yêu cầu
    print("Nội dung:", response.text)

# Gửi yêu cầu HEAD đến địa chỉ URL
def gui_yeu_cau_head():
    # Địa chỉ URL
    url = "https://www.google.com"
    
    # Gửi yêu cầu HEAD
    response = requests.head(url)
    
    # In mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In headers của yêu cầu
    print("Headers:", response.headers)

# Gửi yêu cầu OPTIONS đến địa chỉ URL
def gui_yeu_cau_options():
    # Địa chỉ URL
    url = "https://httpbin.org/options"
    
    # Gửi yêu cầu OPTIONS
    response = requests.options(url)
    
    # In mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In headers của yêu cầu
    print("Headers:", response.headers)

# Gửi yêu cầu PUT đến địa chỉ URL
def gui_yeu_cau_put():
    # Địa chỉ URL
    url = "https://httpbin.org/put"
    
    # Dữ liệu được gửi đi
    data = {"key": "value"}
    
    # Gửi yêu cầu PUT
    response = requests.put(url, data=data)
    
    # In mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In nội dung của yêu cầu
    print("Nội dung:", response.text)

# Gửi yêu cầu DELETE đến địa chỉ URL
def gui_yeu_cau_delete():
    # Địa chỉ URL
    url = "https://httpbin.org/delete"
    
    # Gửi yêu cầu DELETE
    response = requests.delete(url)
    
    # In mã trạng thái của yêu cầu
    print("Mã trạng thái:", response.status_code)
    
    # In nội dung của yêu cầu
    print("Nội dung:", response.text)

# Chạy các hàm
gui_yeu_cau_get()
gui_yeu_cau_post()
gui_yeu_cau_get_voi_tham_so()
gui_yeu_cau_head()
gui_yeu_cau_options()
gui_yeu_cau_put()
gui_yeu_cau_delete()
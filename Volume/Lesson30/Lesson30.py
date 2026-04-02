# Bài 30: Làm quen với thư viện Requests

# Thư viện Requests được sử dụng để gửi HTTP request từ Python
import requests

# Gửi GET request đến địa chỉ https://www.google.com
def gui_get_request():
    url = "https://www.google.com"
    response = requests.get(url)
    
    # Kiểm tra xem request có thành công không
    if response.status_code == 200:
        print("GET request thành công!")
        print("Nội dung response:", response.text)
    else:
        print("GET request thất bại!")

# Gửi POST request đến địa chỉ https://httpbin.org/post
def gui_post_request():
    url = "https://httpbin.org/post"
    data = {"key": "value"}
    response = requests.post(url, data=data)
    
    # Kiểm tra xem request có thành công không
    if response.status_code == 200:
        print("POST request thành công!")
        print("Nội dung response:", response.json())
    else:
        print("POST request thất bại!")

# Gửi PUT request đến địa chỉ https://httpbin.org/put
def gui_put_request():
    url = "https://httpbin.org/put"
    data = {"key": "value"}
    response = requests.put(url, data=data)
    
    # Kiểm tra xem request có thành công không
    if response.status_code == 200:
        print("PUT request thành công!")
        print("Nội dung response:", response.json())
    else:
        print("PUT request thất bại!")

# Gửi DELETE request đến địa chỉ https://httpbin.org/delete
def gui_delete_request():
    url = "https://httpbin.org/delete"
    response = requests.delete(url)
    
    # Kiểm tra xem request có thành công không
    if response.status_code == 200:
        print("DELETE request thành công!")
        print("Nội dung response:", response.json())
    else:
        print("DELETE request thất bại!")

# Chạy các hàm để gửi request
if __name__ == "__main__":
    gui_get_request()
    gui_post_request()
    gui_put_request()
    gui_delete_request()
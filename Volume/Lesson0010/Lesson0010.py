# Thư viện requests cho phép gửi HTTP request và nhận response
import requests

# Gửi HTTP GET request đến trang web cụ thể
def gui_get_request():
    # URL của trang web cần gửi request
    url = "https://www.google.com"
    
    # Gửi GET request
    response = requests.get(url)
    
    # In ra trạng thái của response (200 là thành công)
    print("Trạng thái response:", response.status_code)
    
    # In ra nội dung của response
    print("Nội dung response:\n", response.text)

# Gửi HTTP POST request đến trang web cụ thể
def gui_post_request():
    # URL của trang web cần gửi request
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Dữ liệu cần gửi trong POST request
    data = {
        "title": "Bài viết mới",
        "body": "Nội dung bài viết",
        "userId": 1
    }
    
    # Gửi POST request
    response = requests.post(url, json=data)
    
    # In ra trạng thái của response (201 là tạo mới thành công)
    print("Trạng thái response:", response.status_code)
    
    # In ra nội dung của response
    print("Nội dung response:\n", response.json())

# Chương trình chính
if __name__ == "__main__":
    # Gọi hàm gửi GET request
    gui_get_request()
    
    # Gọi hàm gửi POST request
    gui_post_request()
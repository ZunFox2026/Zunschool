import requests

# Gửi yêu cầu GET đến trang web
def guiyeucau_get(url):
    try:
        # Gửi yêu cầu và lưu trữ kết quả
        response = requests.get(url)
        # Kiểm tra trạng thái của yêu cầu
        if response.status_code == 200:
            print("Yêu cầu thành công!")
            # In nội dung của trang web
            print(response.text)
        else:
            print("Yêu cầu không thành công!")
            print("Trạng thái:", response.status_code)
    except Exception as e:
        print("Lỗi:", str(e))

# Gửi yêu cầu POST đến trang web
def guiyeucau_post(url, data):
    try:
        # Gửi yêu cầu và lưu trữ kết quả
        response = requests.post(url, data=data)
        # Kiểm tra trạng thái của yêu cầu
        if response.status_code == 200:
            print("Yêu cầu thành công!")
            # In nội dung của trang web
            print(response.text)
        else:
            print("Yêu cầu không thành công!")
            print("Trạng thái:", response.status_code)
    except Exception as e:
        print("Lỗi:", str(e))

# Ví dụ sử dụng
url = "http://httpbin.org/get"
guiyeucau_get(url)

url = "http://httpbin.org/post"
data = {"key": "value"}
guiyeucau_post(url, data)
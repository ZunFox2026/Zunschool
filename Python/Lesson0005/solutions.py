# solutions.py - Lời giải Bài 5

# Bài 1: In người đầu và người cuối trong danh sách bạn bè
def bai_1():
    friends = ["An", "Bình", "Châu", "Dũng"]
    print("Bạn đầu tiên:", friends[0])
    print("Bạn cuối cùng:", friends[-1])

# Bài 2: Quản lý danh sách món ăn yêu thích
def bai_2():
    favorite_foods = ["gỏi cuốn", "phở"]
    # Thêm 3 món ăn mới
    favorite_foods.append("bánh xèo")
    favorite_foods.append("hủ tiếu")
    favorite_foods.append("bún bò")
    # Xóa món "phở"
    if "phở" in favorite_foods:
        favorite_foods.remove("phở")
    # In danh sách cuối
    print("Danh sách món ăn yêu thích:", favorite_foods)

# Bài 3: Nhập 5 số và tính tổng
def bai_3():
    numbers = []
    print("Nhập 5 số nguyên:")
    for i in range(5):
        num = int(input(f"Số thứ {i+1}: "))
        numbers.append(num)
    total = sum(numbers)
    print("Tổng 5 số là:", total)

# Bài 4: Đếm số lần xuất hiện của một giá trị
def bai_4():
    items = ["táo", "cam", "táo", "chuối", "cam", "táo"]
    item_to_count = "táo"
    count = 0
    for item in items:
        if item == item_to_count:
            count += 1
    print(f"'{item_to_count}' xuất hiện {count} lần.")

# Bài 5: Đảo ngược list không dùng reverse()
def bai_5():
    original = [1, 2, 3, 4, 5]
    reversed_list = []
    # Duyệt list từ cuối về đầu
    for i in range(len(original) - 1, -1, -1):
        reversed_list.append(original[i])
    print("Danh sách ban đầu:", original)
    print("Danh sách đảo ngược:", reversed_list)

# Gọi các hàm để kiểm tra
bai_1()
bai_2()
bai_3()
bai_4()
bai_5()

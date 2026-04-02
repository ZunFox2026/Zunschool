# Xử lý chuỗi
## Giới thiệu
Xử lý chuỗi là một phần quan trọng trong lập trình, nó cho phép chúng ta thao tác và thay đổi nội dung của các chuỗi ký tự. Trong C++, chuỗi được biểu diễn dưới dạng một mảng các ký tự, kết thúc bởi ký tự null ('\0'). Bài viết này sẽ giới thiệu về các phương pháp xử lý chuỗi cơ bản trong C++.

## Lý thuyết
Trong C++, chúng ta có thể sử dụng thư viện `<string>` để làm việc với chuỗi. Thư viện này cung cấp nhiều hàm và phương thức giúp chúng ta dễ dàng thao tác với chuỗi. Một số phương thức phổ biến bao gồm:
- `length()`: Trả về độ dài của chuỗi.
- `substr()`: Trả về một đoạn con của chuỗi.
- `find()`: Tìm kiếm một chuỗi con trong chuỗi.
- `replace()`: Thay thế một đoạn con của chuỗi bằng một chuỗi khác.

Ví dụ:
```cpp
#include <iostream>
#include <string>

int main() {
    std::string str = "Hello, World!";
    std::cout << "Độ dài của chuỗi: " << str.length() << std::endl;
    std::cout << "Đoạn con từ vị trí 7: " << str.substr(7) << std::endl;
    std::cout << "Vị trí của ',': " << str.find(',') << std::endl;
    str.replace(7, 5, "Vietnam");
    std::cout << "Chuỗi sau khi thay thế: " << str << std::endl;
    return 0;
}
```

## Ví dụ
Chúng ta có thể sử dụng các phương thức trên để giải quyết các vấn đề liên quan đến xử lý chuỗi. Ví dụ, chúng ta muốn viết một chương trình để đếm số lần xuất hiện của một từ trong một chuỗi:

```cpp
#include <iostream>
#include <string>

int demSoLanXuatHien(const std::string& str, const std::string& tu) {
    int dem = 0;
    size_t viTri = str.find(tu);
    while (viTri != std::string::npos) {
        dem++;
        viTri = str.find(tu, viTri + 1);
    }
    return dem;
}

int main() {
    std::string str = "Toi yeu lap trinh, lap trinh rat hay, lap trinh la mot mon hoc rat bao dong";
    std::string tu = "lap trinh";
    std::cout << "So lan xuat hien cua '" << tu << "' trong chuoi: " << demSoLanXuatHien(str, tu) << std::endl;
    return 0;
}
```

## Bài tập
Để luyện tập kỹ năng xử lý chuỗi, bạn có thể tự giải các bài tập sau:
- Viết chương trình để kiểm tra xem một chuỗi có phải là palindrome hay không.
- Viết chương trình để tìm kiếm và thay thế tất cả các lần xuất hiện của một từ trong một chuỗi bằng một từ khác.
- Viết chương trình để đếm số từ trong một chuỗi.
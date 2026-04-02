# Xử lý tệp
## Giới thiệu
Xử lý tệp là một phần quan trọng trong lập trình, cho phép bạn lưu trữ và truy xuất dữ liệu từ các tệp trên hệ thống. Trong C++, bạn có thể sử dụng các lớp và hàm trong thư viện chuẩn để thực hiện việc này. Bài viết này sẽ giới thiệu về các khái niệm cơ bản và cách sử dụng các lớp và hàm trong C++ để xử lý tệp.

## Lý thuyết
Trong C++, có hai loại tệp chính: tệp văn bản (text file) và tệp nhị phân (binary file). Tệp văn bản chứa dữ liệu dưới dạng văn bản, trong khi tệp nhị phân chứa dữ liệu dưới dạng nhị phân. Để xử lý tệp, bạn cần sử dụng các lớp và hàm sau:
- `ifstream`: lớp này cho phép bạn đọc dữ liệu từ một tệp.
- `ofstream`: lớp này cho phép bạn ghi dữ liệu vào một tệp.
- `fstream`: lớp này cho phép bạn đọc và ghi dữ liệu vào một tệp.

Ví dụ, để mở một tệp văn bản và đọc dữ liệu từ nó, bạn có thể sử dụng lớp `ifstream` như sau:
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::ifstream file("example.txt");
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            std::cout << line << std::endl;
        }
        file.close();
    } else {
        std::cout << "Không thể mở tệp.";
    }
    return 0;
}
```

## Ví dụ
Để minh họa việc sử dụng các lớp và hàm trong C++ để xử lý tệp, hãy xem xét ví dụ sau. Giả sử bạn muốn tạo một chương trình để quản lý danh sách sinh viên, và bạn muốn lưu trữ thông tin sinh viên trong một tệp văn bản. Bạn có thể sử dụng lớp `ofstream` để ghi dữ liệu vào tệp và lớp `ifstream` để đọc dữ liệu từ tệp.

Ví dụ:
```cpp
#include <fstream>
#include <iostream>
#include <string>

struct SinhVien {
    std::string ten;
    int tuoi;
};

int main() {
    // Ghi dữ liệu vào tệp
    std::ofstream fileGhi("sinh_vien.txt");
    if (fileGhi.is_open()) {
        SinhVien sv1 = {"Nguyen Van A", 20};
        fileGhi << sv1.ten << " " << sv1.tuoi << std::endl;
        fileGhi.close();
    } else {
        std::cout << "Không thể mở tệp để ghi.";
    }

    // Đọc dữ liệu từ tệp
    std::ifstream fileDoc("sinh_vien.txt");
    if (fileDoc.is_open()) {
        std::string ten;
        int tuoi;
        while (fileDoc >> ten >> tuoi) {
            std::cout << "Tên: " << ten << ", Tuổi: " << tuoi << std::endl;
        }
        fileDoc.close();
    } else {
        std::cout << "Không thể mở tệp để đọc.";
    }
    return 0;
}
```

## Bài tập
Để thực hành việc xử lý tệp trong C++, bạn có thể thực hiện các bài tập sau:
- Tạo một chương trình để ghi dữ liệu vào một tệp văn bản và sau đó đọc dữ liệu từ tệp đó.
- Tạo một chương trình để quản lý danh sách sách trong một thư viện, cho phép người dùng thêm, xóa, sửa thông tin sách và lưu trữ thông tin vào một tệp.
- Tạo một chương trình để quản lý danh sách nhân viên, cho phép người dùng thêm, xóa, sửa thông tin nhân viên và lưu trữ thông tin vào một tệp.
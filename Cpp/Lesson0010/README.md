# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp trên đĩa cứng. Trong C++, bạn có thể làm việc với tệp bằng cách sử dụng các hàm và đối tượng trong thư viện `<fstream>`. Bài viết này sẽ giới thiệu đến bạn cách làm việc với tệp trong C++.

## Lý thuyết
Để làm việc với tệp trong C++, bạn cần bao gồm thư viện `<fstream>` vào chương trình của mình. Thư viện này cung cấp các hàm và đối tượng để đọc và viết tệp. Có hai loại tệp chính trong C++: tệp văn bản (`std::ifstream` và `std::ofstream`) và tệp nhị phân (`std::ifstream` và `std::ofstream` với chế độ nhị phân).

Các chế độ mở tệp trong C++ bao gồm:
- `ios::in`: Mở tệp để đọc.
- `ios::out`: Mở tệp để viết.
- `ios::app`: Mở tệp để thêm vào cuối tệp.
- `ios::trunc`: Mở tệp và xóa nội dung hiện tại.
- `ios::binary`: Mở tệp ở chế độ nhị phân.

Ví dụ, để mở một tệp văn bản để đọc, bạn có thể sử dụng:
```cpp
std::ifstream file("example.txt");
```
Để kiểm tra xem tệp đã được mở thành công hay không, bạn có thể sử dụng toán tử `!`:
```cpp
if (!file) {
    std::cout << "Không thể mở tệp!" << std::endl;
    return 1;
}
```
## Ví dụ
Dưới đây là một ví dụ đơn giản về cách đọc và viết tệp trong C++:
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Mở tệp để viết
    std::ofstream outFile("example.txt");
    if (!outFile) {
        std::cout << "Không thể mở tệp để viết!" << std::endl;
        return 1;
    }

    // Viết vào tệp
    outFile << "Xin chào, thế giới!" << std::endl;
    outFile.close();

    // Mở tệp để đọc
    std::ifstream inFile("example.txt");
    if (!inFile) {
        std::cout << "Không thể mở tệp để đọc!" << std::endl;
        return 1;
    }

    // Đọc từ tệp
    std::string line;
    while (std::getline(inFile, line)) {
        std::cout << line << std::endl;
    }
    inFile.close();

    return 0;
}
```
## Bài tập
Bài tập 1: Viết một chương trình C++ để tạo một tệp văn bản mới có tên "hello.txt" và viết vào đó dòng chữ "Xin chào, thế giới!".

Bài tập 2: Viết một chương trình C++ để đọc nội dung của tệp "hello.txt" và in ra màn hình.

Bài tập 3: Viết một chương trình C++ để thêm vào cuối tệp "hello.txt" dòng chữ "Đây là dòng thêm vào!".

Bài tập 4: Viết một chương trình C++ để đọc và hiển thị nội dung của tệp "hello.txt" sau khi thực hiện bài tập 3.
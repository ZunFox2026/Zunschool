# Xử lý tệp tin
## Giới thiệu
Xử lý tệp tin là một phần quan trọng trong lập trình, giúp chúng ta lưu trữ và đọc dữ liệu từ tệp tin. Trong C++, chúng ta có thể xử lý tệp tin bằng cách sử dụng các thư viện và hàm đặc biệt. Bài viết này sẽ giới thiệu về cách xử lý tệp tin trong C++.

## Lý thuyết
Để xử lý tệp tin trong C++, chúng ta cần sử dụng thư viện `fstream`. Thư viện này cung cấp các hàm và lớp để đọc và ghi dữ liệu vào tệp tin. Có ba loại tệp tin chính trong C++: 
- `ifstream` (đọc tệp tin)
- `ofstream` (ghi tệp tin)
- `fstream` (đọc và ghi tệp tin)

Chúng ta có thể mở tệp tin bằng cách sử dụng hàm `open()` và đóng tệp tin bằng cách sử dụng hàm `close()`. Để đọc dữ liệu từ tệp tin, chúng ta có thể sử dụng toán tử `>>` hoặc hàm `getline()`. Để ghi dữ liệu vào tệp tin, chúng ta có thể sử dụng toán tử `<<`.

Ví dụ về cách mở và đóng tệp tin:
```cpp
#include <fstream>

int main() {
    std::ifstream file("example.txt");
    if (file.is_open()) {
        // đọc dữ liệu từ tệp tin
        file.close();
    } else {
        std::cout << "Không thể mở tệp tin";
    }
    return 0;
}
```

## Ví dụ
Dưới đây là ví dụ về cách đọc và ghi dữ liệu vào tệp tin:
```cpp
#include <fstream>
#include <string>

int main() {
    // Ghi dữ liệu vào tệp tin
    std::ofstream outFile("example.txt");
    if (outFile.is_open()) {
        outFile << "Xin chào thế giới!" << std::endl;
        outFile.close();
    } else {
        std::cout << "Không thể mở tệp tin";
    }

    // Đọc dữ liệu từ tệp tin
    std::ifstream inFile("example.txt");
    if (inFile.is_open()) {
        std::string line;
        while (std::getline(inFile, line)) {
            std::cout << line << std::endl;
        }
        inFile.close();
    } else {
        std::cout << "Không thể mở tệp tin";
    }
    return 0;
}
```

## Bài tập
Bài tập 1: Tạo một chương trình C++ để ghi dữ liệu vào tệp tin. Dữ liệu bao gồm tên và tuổi của người dùng.

Bài tập 2: Tạo một chương trình C++ để đọc dữ liệu từ tệp tin. Dữ liệu bao gồm tên và tuổi của người dùng.

Bài tập 3: Tạo một chương trình C++ để copy dữ liệu từ tệp tin này sang tệp tin khác.

Hy vọng những thông tin trên sẽ giúp bạn hiểu rõ hơn về cách xử lý tệp tin trong C++. Hãy thực hành và làm các bài tập để cải thiện kỹ năng của mình.
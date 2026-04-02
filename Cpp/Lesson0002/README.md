# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và đọc dữ liệu từ các tệp. Trong C++, chúng ta có thể sử dụng các thư viện như `fstream` để thực hiện các操作 này. Bài viết này sẽ giới thiệu về cách làm việc với tệp trong C++, bao gồm cả lý thuyết và ví dụ.

## Lý thuyết
Trong C++, chúng ta có thể sử dụng các lớp `ifstream`, `ofstream` và `fstream` để làm việc với tệp. 
- `ifstream` cho phép chúng ta đọc dữ liệu từ một tệp.
- `ofstream` cho phép chúng ta ghi dữ liệu vào một tệp.
- `fstream` cho phép chúng ta cả đọc và ghi dữ liệu từ/into một tệp.

Để mở một tệp, chúng ta sử dụng hàm `open()` và để đóng một tệp, chúng ta sử dụng hàm `close()`. Ngoài ra, chúng ta còn có thể sử dụng các hàm như `eof()` để kiểm tra xem tệp đã được đọc hết hay chưa, `fail()` để kiểm tra xem có lỗi khi đọc/ghi tệp hay không.

Ví dụ về cách mở và đóng một tệp:
```cpp
#include <fstream>

int main() {
    std::ifstream file("example.txt");
    if (file.is_open()) {
        // Đọc dữ liệu từ tệp
        file.close();
    } else {
        std::cout << "Không thể mở tệp.";
    }
    return 0;
}
```

## Ví dụ
Dưới đây là ví dụ về cách đọc và ghi dữ liệu từ/into một tệp:
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Ghi dữ liệu vào tệp
    std::ofstream outfile("example.txt");
    if (outfile.is_open()) {
        outfile << "Xin chào, thế giới!";
        outfile.close();
    } else {
        std::cout << "Không thể mở tệp.";
    }

    // Đọc dữ liệu từ tệp
    std::ifstream infile("example.txt");
    if (infile.is_open()) {
        std::string line;
        while (std::getline(infile, line)) {
            std::cout << line << std::endl;
        }
        infile.close();
    } else {
        std::cout << "Không thể mở tệp.";
    }
    return 0;
}
```

## Bài tập
Bài tập này yêu cầu bạn thực hiện các bước sau:
- Tạo một tệp tên là `user.txt` và ghi vào đó tên và tuổi của một người dùng.
- Đọc dữ liệu từ tệp `user.txt` và hiển thị thông tin người dùng ra màn hình.
- Thêm một dòng mới vào tệp `user.txt` với nội dung là địa chỉ của người dùng.

Hãy thử thực hiện bài tập này và xem kết quả!
# Tìm hiểu về xử lý ngoại lệ trong C++
## Giới thiệu
Xử lý ngoại lệ là một phần quan trọng trong lập trình C++, giúp chương trình có thể xử lý và phục hồi từ các tình huống không mong muốn. Trong bài này, chúng ta sẽ tìm hiểu về cơ bản của xử lý ngoại lệ trong C++ và cách áp dụng nó vào chương trình.

## Lý thuyết
Xử lý ngoại lệ trong C++ được thực hiện thông qua các từ khóa `try`, `catch` và `throw`. Từ khóa `try` được sử dụng để bao quanh mã code có thể gây ra ngoại lệ, từ khóa `catch` được sử dụng để bắt và xử lý ngoại lệ, và từ khóa `throw` được sử dụng để ném ngoại lệ. Khi một ngoại lệ được ném, chương trình sẽ tìm kiếm một khối `catch` phù hợp để xử lý nó. Nếu không tìm thấy, chương trình sẽ终止.

Ví dụ về việc sử dụng `try`, `catch` và `throw`:
```cpp
void chia(int a, int b) {
    if (b == 0) {
        throw "Lỗi chia cho 0";
    }
    int ketQua = a / b;
    std::cout << "Kết quả: " << ketQua << std::endl;
}

int main() {
    try {
        chia(10, 0);
    } catch (const char* e) {
        std::cout << "Xảy ra lỗi: " << e << std::endl;
    }
    return 0;
}
```
Trong ví dụ trên, khi hàm `chia` nhận được tham số `b` là 0, nó sẽ ném một ngoại lệ với thông điệp "Lỗi chia cho 0". Khối `catch` trong hàm `main` sẽ bắt và xử lý ngoại lệ này.

## Ví dụ
Một ví dụ khác về xử lý ngoại lệ trong C++ là khi làm việc với file. Nếu chương trình không thể mở file, nó sẽ ném một ngoại lệ.

Ví dụ:
```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ifstream file("file.txt");
    try {
        if (!file.is_open()) {
            throw "Lỗi mở file";
        }
        // Đọc nội dung file
        std::string line;
        while (std::getline(file, line)) {
            std::cout << line << std::endl;
        }
        file.close();
    } catch (const char* e) {
        std::cout << "Xảy ra lỗi: " << e << std::endl;
    }
    return 0;
}
```
Trong ví dụ trên, nếu file "file.txt" không tồn tại, chương trình sẽ ném một ngoại lệ với thông điệp "Lỗi mở file".

## Bài tập
Bài tập 1: Viết chương trình xử lý ngoại lệ khi chia hai số. Nếu số chia là 0, chương trình sẽ ném một ngoại lệ với thông điệp "Lỗi chia cho 0".

Bài tập 2: Viết chương trình đọc nội dung file và xử lý ngoại lệ nếu file không tồn tại. Nếu file không tồn tại, chương trình sẽ ném một ngoại lệ với thông điệp "Lỗi mở file".
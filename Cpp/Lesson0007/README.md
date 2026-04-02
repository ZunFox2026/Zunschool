# Xử lý tệp tin
## Giới thiệu
Xử lý tệp tin là một phần quan trọng trong lập trình, nó cho phép chúng ta lưu trữ và truy xuất dữ liệu từ các tệp tin. Trong C++, chúng ta có thể sử dụng các lớp và hàm trong thư viện `<fstream>` để thực hiện các tác vụ này. Bài viết này sẽ giới thiệu về cách xử lý tệp tin trong C++, bao gồm cả lý thuyết và ví dụ.

## Lý thuyết
Trong C++, chúng ta có thể sử dụng các lớp sau để xử lý tệp tin:
- `ifstream`: lớp này cho phép chúng ta đọc dữ liệu từ một tệp tin.
- `ofstream`: lớp này cho phép chúng ta ghi dữ liệu vào một tệp tin.
- `fstream`: lớp này cho phép chúng ta đọc và ghi dữ liệu vào một tệp tin.

Để mở một tệp tin, chúng ta sử dụng hàm `open()` và để đóng một tệp tin, chúng ta sử dụng hàm `close()`. Chúng ta cũng có thể sử dụng toán tử `>>` để đọc dữ liệu từ tệp tin và toán tử `<<` để ghi dữ liệu vào tệp tin.

Ví dụ:
```cpp
#include <fstream>
using namespace std;

int main() {
    // Mở tệp tin để ghi dữ liệu
    ofstream file("example.txt");
    if (file.is_open()) {
        // Ghi dữ liệu vào tệp tin
        file << "Xin chào, thế giới!";
        file.close();
    }

    // Mở tệp tin để đọc dữ liệu
    ifstream file2("example.txt");
    if (file2.is_open()) {
        string line;
        // Đọc dữ liệu từ tệp tin
        getline(file2, line);
        cout << line << endl;
        file2.close();
    }

    return 0;
}
```

## Ví dụ
Chúng ta có thể sử dụng các lớp và hàm trong thư viện `<fstream>` để thực hiện các tác vụ xử lý tệp tin khác nhau. Ví dụ, chúng ta có thể đọc và ghi dữ liệu vào một tệp tin theo dòng, hoặc đọc và ghi dữ liệu vào một tệp tin theo byte.

Ví dụ về đọc và ghi dữ liệu vào một tệp tin theo dòng:
```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    // Mở tệp tin để ghi dữ liệu
    ofstream file("example.txt");
    if (file.is_open()) {
        // Ghi dữ liệu vào tệp tin
        file << "Xin chào, thế giới!" << endl;
        file << "Đây là dòng thứ hai." << endl;
        file.close();
    }

    // Mở tệp tin để đọc dữ liệu
    ifstream file2("example.txt");
    if (file2.is_open()) {
        string line;
        // Đọc dữ liệu từ tệp tin
        while (getline(file2, line)) {
            cout << line << endl;
        }
        file2.close();
    }

    return 0;
}
```

## Bài tập
Bài tập 1: Tạo một chương trình C++ để ghi dữ liệu vào một tệp tin. Dữ liệu bao gồm tên, tuổi và địa chỉ của một người.

Bài tập 2: Tạo một chương trình C++ để đọc dữ liệu từ một tệp tin. Dữ liệu bao gồm tên, tuổi và địa chỉ của một người.

Bài tập 3: Tạo một chương trình C++ để thực hiện các tác vụ sau:
- Ghi dữ liệu vào một tệp tin.
- Đọc dữ liệu từ tệp tin.
- Xóa dữ liệu trong tệp tin.
- Thêm dữ liệu mới vào tệp tin.
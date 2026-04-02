# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và đọc dữ liệu từ các tệp tin. Trong C++, chúng ta có thể sử dụng các hàm và lớp để thực hiện các hoạt động này. Bài viết này sẽ giới thiệu về cách làm việc với tệp trong C++.

## Lý thuyết
Để làm việc với tệp trong C++, chúng ta cần sử dụng thư viện `fstream`. Thư viện này cung cấp các lớp `ifstream`, `ofstream` và `fstream` để đọc, viết và đọc/ghi tệp tin. 

- `ifstream` (Input File Stream): để đọc tệp tin.
- `ofstream` (Output File Stream): để viết tệp tin.
- `fstream` (File Stream): để đọc và viết tệp tin.

Chúng ta cũng cần sử dụng các hàm như `open()`, `close()`, `read()`, `write()` để thực hiện các hoạt động trên tệp tin.

Ví dụ, để mở một tệp tin và đọc nội dung của nó, chúng ta có thể sử dụng câu lệnh sau:
```cpp
ifstream file("ten_tep.txt");
if (file.is_open()) {
    string line;
    while (getline(file, line)) {
        cout << line << endl;
    }
    file.close();
} else {
    cout << "Không thể mở tệp tin." << endl;
}
```

## Ví dụ
Dưới đây là một ví dụ đơn giản về việc viết và đọc tệp tin trong C++:
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Tạo một tệp tin và viết nội dung vào đó
    ofstreamoutfile("example.txt");
    if (outfile.is_open()) {
        outfile << "Xin chào, thế giới!" << endl;
        outfile.close();
    } else {
        cout << "Không thể tạo tệp tin." << endl;
    }

    // Đọc nội dung từ tệp tin
    ifstream infile("example.txt");
    if (infile.is_open()) {
        string line;
        while (getline(infile, line)) {
            cout << line << endl;
        }
        infile.close();
    } else {
        cout << "Không thể mở tệp tin." << endl;
    }

    return 0;
}
```
Trong ví dụ trên, chúng ta tạo một tệp tin `example.txt` và viết nội dung vào đó. Sau đó, chúng ta đọc nội dung từ tệp tin và in ra màn hình.

## Bài tập
Bài tập cho bạn:

- Tạo một chương trình C++ để ghi danh sách các sinh viên vào một tệp tin.
- Chương trình sẽ yêu cầu người dùng nhập thông tin về sinh viên (họ tên, tuổi, giới tính) và ghi vào tệp tin.
- Sau đó, chương trình sẽ đọc nội dung từ tệp tin và in ra màn hình.

Gợi ý: Sử dụng các lớp và hàm trong thư viện `fstream` để thực hiện các hoạt động trên tệp tin.
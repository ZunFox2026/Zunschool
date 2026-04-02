# Tìm hiểu về đa luồng trong C++
## Giới thiệu
Đa luồng (Multithreading) là một kỹ thuật trong lập trình cho phép một chương trình thực hiện nhiều tác vụ đồng thời, giúp tăng tốc độ xử lý và cải thiện hiệu suất của chương trình. Trong C++, đa luồng được hỗ trợ thông qua thư viện `<thread>`. Bài viết này sẽ giới thiệu về đa luồng trong C++ và cách sử dụng nó trong các chương trình.

## Lý thuyết
Trong C++, một luồng (thread) là một đơn vị thực hiện công việc độc lập. Mỗi luồng có thể thực hiện một tác vụ riêng biệt, và chúng có thể chạy đồng thời với nhau. Để tạo một luồng trong C++, bạn cần sử dụng lớp `std::thread` và truyền cho nó một hàm hoặc một đối tượng có thể gọi được. Khi một luồng được tạo, nó sẽ bắt đầu thực hiện công việc ngay lập tức.

Ví dụ, bạn có thể tạo một luồng như sau:
```cpp
#include <thread>
#include <iostream>

void inThongDiep() {
    std::cout << "Xin chào từ luồng mới!" << std::endl;
}

int main() {
    std::thread luongMoi(inThongDiep);
    luongMoi.join();
    return 0;
}
```
Trong ví dụ trên, chúng ta tạo một luồng mới bằng cách gọi hàm `std::thread` và truyền cho nó hàm `inThongDiep`. Sau đó, chúng ta gọi hàm `join()` để chờ cho luồng mới hoàn thành công việc.

## Ví dụ
Dưới đây là một ví dụ minh họa về đa luồng trong C++:
```cpp
#include <thread>
#include <iostream>

void inSoChan() {
    for (int i = 0; i < 10; i++) {
        if (i % 2 == 0) {
            std::cout << i << std::endl;
        }
    }
}

void inSoLe() {
    for (int i = 0; i < 10; i++) {
        if (i % 2 != 0) {
            std::cout << i << std::endl;
        }
    }
}

int main() {
    std::thread luong1(inSoChan);
    std::thread luong2(inSoLe);
    luong1.join();
    luong2.join();
    return 0;
}
```
Trong ví dụ này, chúng ta tạo hai luồng: một luồng in ra các số chẵn và một luồng in ra các số lẻ. Cả hai luồng đều chạy đồng thời và in ra kết quả.

## Bài tập
Bài tập cho bạn đọc:

* Tạo một chương trình đa luồng để tính tổng và tích của một mảng số nguyên.
* Tạo một chương trình đa luồng để tìm kiếm một phần tử trong một mảng số nguyên.
* Tạo một chương trình đa luồng để thực hiện các công việc khác nhau, chẳng hạn như đọc và ghi file, thực hiện các phép tính toán học, v.v.

Hy vọng bài viết này đã giúp bạn hiểu rõ hơn về đa luồng trong C++ và cách sử dụng nó trong các chương trình. Chúc bạn thành công trong việc lập trình đa luồng!
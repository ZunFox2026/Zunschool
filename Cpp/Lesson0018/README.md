# Làm quen với đa luồng
## Giới thiệu
Đa luồng (multithreading) là một kỹ thuật cho phép chương trình thực hiện nhiều tác vụ đồng thời, giúp tăng hiệu suất và tốc độ xử lý của chương trình. Trong C++, đa luồng được hỗ trợ thông qua thư viện `<thread>`. Trong bài này, chúng ta sẽ tìm hiểu về cơ bản của đa luồng và cách sử dụng nó trong chương trình C++.

## Lý thuyết
Một chương trình đa luồng bao gồm nhiều luồng (thread) chạy đồng thời. Mỗi luồng thực hiện một tác vụ riêng biệt và có thể chạy độc lập với các luồng khác. Để tạo một luồng trong C++, chúng ta sử dụng lớp `std::thread` và truyền cho nó một hàm sẽ được thực hiện trong luồng đó. Ví dụ:
```cpp
#include <thread>
#include <iostream>

void inThongTin() {
    std::cout << "Xin chào từ luồng con!" << std::endl;
}

int main() {
    std::thread luongCon(inThongTin);
    luongCon.join();
    return 0;
}
```
Trong ví dụ trên, chúng ta tạo một luồng con thực hiện hàm `inThongTin()` và in ra màn hình "Xin chào từ luồng con!". Hàm `join()` được sử dụng để chờ cho luồng con kết thúc trước khi chương trình chính kết thúc.

## Ví dụ
Dưới đây là một ví dụ minh họa việc sử dụng đa luồng trong C++:
```cpp
#include <thread>
#include <iostream>

void tinhTong(int* arr, int n) {
    int tong = 0;
    for (int i = 0; i < n; i++) {
        tong += arr[i];
    }
    std::cout << "Tổng các phần tử trong mảng: " << tong << std::endl;
}

void inMang(int* arr, int n) {
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    std::thread luong1(tinhTong, arr, n);
    std::thread luong2(inMang, arr, n);

    luong1.join();
    luong2.join();

    return 0;
}
```
Trong ví dụ này, chúng ta tạo hai luồng: một luồng tính tổng các phần tử trong mảng và một luồng in ra màn hình các phần tử trong mảng.

## Bài tập
Bài tập: Viết một chương trình C++ sử dụng đa luồng để thực hiện hai tác vụ sau:
- Tính tổng các phần tử trong một mảng.
- In ra màn hình các phần tử trong mảng.
Chương trình sẽ nhận vào từ người dùng kích thước của mảng và các phần tử trong mảng. Sau đó, chương trình sẽ tạo hai luồng để thực hiện hai tác vụ trên và chờ cho cả hai luồng kết thúc trước khi kết thúc.
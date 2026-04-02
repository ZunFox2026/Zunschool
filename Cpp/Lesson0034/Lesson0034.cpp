#include <iostream>
#include <thread>

// Hàm này sẽ được thực hiện bởi một luồng khác
void hamKhac() {
    // In ra thông báo từ luồng khác
    std::cout << "Xin chào từ luồng khác!" << std::endl;
}

int main() {
    // Tạo một luồng mới
    std::thread luongKhac(hamKhac);
    
    // In ra thông báo từ luồng chính
    std::cout << "Xin chào từ luồng chính!" << std::endl;
    
    // Chờ cho luồng khác kết thúc
    luongKhac.join();
    
    return 0;
}
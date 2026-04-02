#include <iostream>
#include <thread>
#include <chrono>

// Hàm này sẽ được thực hiện bởi một luồng riêng biệt
void hamLuongRieng() {
    // In thông điệp từ luồng riêng biệt
    std::cout << "Xin chào từ luồng riêng biệt!" << std::endl;
    // Dừng luồng trong 2 giây
    std::this_thread::sleep_for(std::chrono::seconds(2));
    // In thông điệp sau khi dừng
    std::cout << "Luồng riêng biệt vừa dừng lại." << std::endl;
}

int main() {
    // Tạo một luồng mới và gán hàm hamLuongRieng cho nó
    std::thread luongRieng(hamLuongRieng);
    // In thông điệp từ luồng chính
    std::cout << "Xin chào từ luồng chính!" << std::endl;
    // Dừng luồng chính trong 1 giây
    std::this_thread::sleep_for(std::chrono::seconds(1));
    // In thông điệp sau khi dừng
    std::cout << "Luồng chính vừa dừng lại." << std::endl;
    // Đợi cho luồng riêng biệt kết thúc
    luongRieng.join();
    return 0;
}
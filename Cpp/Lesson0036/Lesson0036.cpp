#include <iostream>
#include <fstream>
#include <string>

// Hàm main để kiểm tra chương trình
int main() {
    // Tạo tệp mới
    std::ofstream tep("example.txt");
    if (tep.is_open()) {
        // Ghi dữ liệu vào tệp
        tep << "Xin chào, thế giới!" << std::endl;
        tep.close();
    } else {
        std::cout << "Không thể tạo tệp." << std::endl;
    }

    // Đọc từ tệp
    std::ifstream doc("example.txt");
    if (doc.is_open()) {
        std::string line;
        while (std::getline(doc, line)) {
            // In ra màn hình
            std::cout << line << std::endl;
        }
        doc.close();
    } else {
        std::cout << "Không thể đọc tệp." << std::endl;
    }

    return 0;
}
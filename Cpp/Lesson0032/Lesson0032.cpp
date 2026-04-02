#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// Hàm main để chạy chương trình
int main() {
    // Tạo một tệp tin mới tên là "example.txt"
    ofstream outFile("example.txt");
    
    // Kiểm tra nếu tệp tin được mở thành công
    if (outFile.is_open()) {
        // Viết dữ liệu vào tệp tin
        outFile << "Xin chào, thế giới!\n";
        outFile << "Đây là một ví dụ về việc ghi dữ liệu vào tệp tin.";
        
        // Đóng tệp tin
        outFile.close();
        cout << "Dữ liệu đã được ghi vào tệp tin thành công.\n";
    } else {
        cout << "Không thể mở tệp tin để ghi dữ liệu.\n";
    }

    // Mở tệp tin để đọc dữ liệu
    ifstream inFile("example.txt");
    
    // Kiểm tra nếu tệp tin được mở thành công
    if (inFile.is_open()) {
        // Đọc dữ liệu từ tệp tin
        string line;
        while (getline(inFile, line)) {
            cout << line << endl;
        }
        
        // Đóng tệp tin
        inFile.close();
        cout << "Dữ liệu đã được đọc từ tệp tin thành công.\n";
    } else {
        cout << "Không thể mở tệp tin để đọc dữ liệu.\n";
    }

    return 0;
}
#include <iostream>
#include <fstream> // Thư viện cần thiết để làm việc với tệp tin
#include <string>

using namespace std;

int main() {
    // Tạo một tệp tin mới và ghi dữ liệu vào tệp tin
    ofstream tepTin("example.txt"); // Tạo một tệp tin mới tên là example.txt
    if (tepTin.is_open()) { // Kiểm tra xem tệp tin đã được mở thành công chưa
        tepTin << "Xin chào, thế giới!\n"; // Ghi chuỗi "Xin chào, thế giới!" vào tệp tin
        tepTin << "Đây là một chương trình làm việc với tệp tin.\n"; // Ghi tiếp một chuỗi khác vào tệp tin
        tepTin.close(); // Đóng tệp tin
        cout << "Ghi dữ liệu vào tệp tin thành công!\n";
    } else {
        cout << "Không thể mở tệp tin!\n";
    }

    // Đọc dữ liệu từ tệp tin
    ifstream doc TepTin("example.txt"); // Mở tệp tin để đọc dữ liệu
    if (doc.is_open()) { // Kiểm tra xem tệp tin đã được mở thành công chưa
        string dong; // Biến để lưu trữ mỗi dòng dữ liệu đọc từ tệp tin
        while (getline(doc, dong)) { // Đọc từng dòng dữ liệu từ tệp tin
            cout << dong << endl; // In ra màn hình mỗi dòng dữ liệu đọc được
        }
        doc.close(); // Đóng tệp tin
    } else {
        cout << "Không thể mở tệp tin!\n";
    }

    return 0;
}
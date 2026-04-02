#include <iostream>
#include <fstream> // thư viện cần thiết để làm việc với tệp

using namespace std;

int main() {
    // Tạo tệp mới và ghi dữ liệu vào tệp
    ofstream tepGhi("example.txt"); // tạo tệp example.txt
    if (tepGhi.is_open()) { // kiểm tra nếu tệp đã được mở
        tepGhi << "Xin chào, thế giới!\n"; // ghi dữ liệu vào tệp
        tepGhi << "Đây là ví dụ về việc ghi dữ liệu vào tệp.";
        tepGhi.close(); // đóng tệp
        cout << "Đã ghi dữ liệu vào tệp thành công!" << endl;
    } else {
        cout << "Không thể mở tệp!" << endl;
    }

    // Đọc dữ liệu từ tệp
    ifstream tepDoc("example.txt"); // mở tệp example.txt để đọc
    if (tepDoc.is_open()) { // kiểm tra nếu tệp đã được mở
        string dong; // biến để lưu trữ mỗi dòng trong tệp
        while (getline(tepDoc, dong)) { // đọc từng dòng trong tệp
            cout << dong << endl; // in ra màn hình
        }
        tepDoc.close(); // đóng tệp
        cout << "Đã đọc dữ liệu từ tệp thành công!" << endl;
    } else {
        cout << "Không thể mở tệp!" << endl;
    }

    return 0;
}
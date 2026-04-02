#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // Tạo tệp tin mới
    ofstream tepTinMoi("example.txt");
    if (tepTinMoi.is_open()) {
        // Ghi dữ liệu vào tệp tin
        tepTinMoi << "Xin chào, thế giới!" << endl;
        tepTinMoi.close();
        cout << "Tạo tệp tin thành công!" << endl;
    } else {
        cout << "Không thể tạo tệp tin!" << endl;
    }

    // Đọc tệp tin
    ifstream tepTin("example.txt");
    if (tepTin.is_open()) {
        string dong;
        while (getline(tepTin, dong)) {
            // In dữ liệu từ tệp tin
            cout << dong << endl;
        }
        tepTin.close();
    } else {
        cout << "Không thể mở tệp tin!" << endl;
    }

    return 0;
}
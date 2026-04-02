#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // Tạo một tệp tin mới
    ofstream tepTin("example.txt");
    if (tepTin.is_open()) {
        // Ghi nội dung vào tệp tin
        tepTin << "Xin chào, thế giới!";
        tepTin.close();
        cout << "Tạo tệp tin thành công!" << endl;
    } else {
        cout << "Không thể tạo tệp tin!" << endl;
    }

    // Đọc nội dung từ tệp tin
    ifstream doc TepTin("example.txt");
    if (doc.is_open()) {
        string dong;
        while (getline(doc, dong)) {
            cout << "Nội dung tệp tin: " << dong << endl;
        }
        doc.close();
    } else {
        cout << "Không thể đọc tệp tin!" << endl;
    }

    return 0;
}
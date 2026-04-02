#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // Tạo một tệp tin mới
    ofstream tepTin("example.txt");
    
    // Nếu tệp tin được tạo thành công
    if (tepTin.is_open()) {
        // Ghi nội dung vào tệp tin
        tepTin << "Xin chào, thế giới!" << endl;
        
        // Đóng tệp tin
        tepTin.close();
        
        // Thông báo thành công
        cout << "Tệp tin đã được tạo thành công!" << endl;
    } else {
        // Thông báo thất bại
        cout << "Không thể tạo tệp tin!" << endl;
    }

    // Mở tệp tin để đọc
    ifstream docTeppTin("example.txt");
    
    // Nếu tệp tin được mở thành công
    if (docTeppTin.is_open()) {
        // Biến để lưu trữ nội dung của tệp tin
        string noiDung;
        
        // Đọc nội dung của tệp tin
        while (getline(docTeppTin, noiDung)) {
            // In nội dung ra màn hình
            cout << noiDung << endl;
        }
        
        // Đóng tệp tin
        docTeppTin.close();
    } else {
        // Thông báo thất bại
        cout << "Không thể mở tệp tin!" << endl;
    }

    return 0;
}
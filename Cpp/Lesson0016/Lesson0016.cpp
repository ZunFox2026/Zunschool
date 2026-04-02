#include <iostream>
#include <fstream> // Thư viện xử lý tệp
#include <string>

using namespace std;

int main() {
    // Tạo tệp tin mới và ghi dữ liệu vào tệp
    ofstream tep_tin("example.txt"); // Tạo tệp tin mới tên là example.txt
    if (tep_tin.is_open()) { // Kiểm tra xem tệp đã được mở chưa
        tep_tin << "Xin chào, thế giới!";
        tep_tin.close(); // Đóng tệp tin
        cout << "Tạo tệp tin thành công!" << endl;
    } else {
        cout << "Không thể tạo tệp tin!" << endl;
    }

    // Đọc dữ liệu từ tệp tin
    ifstream doc_tep("example.txt"); // Mở tệp tin example.txt để đọc
    if (doc_tep.is_open()) {
        string line;
        while (getline(doc_tep, line)) { // Đọc từng dòng trong tệp tin
            cout << line << endl;
        }
        doc_tep.close(); // Đóng tệp tin
    } else {
        cout << "Không thể mở tệp tin!" << endl;
    }

    return 0;
}
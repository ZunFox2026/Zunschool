#include <iostream>
#include <fstream> // Thư viện để làm việc với tệp
#include <string> // Thư viện để sử dụng chuỗi trong C++

using namespace std;

int main() {
    // Tạo tệp tin và ghi dữ liệu vào tệp
    ofstream tep_tin("example.txt"); // Tạo tệp tin với tên là example.txt
    if (tep_tin.is_open()) { // Kiểm tra xem tệp đã được mở chưa
        tep_tin << "Xin chào, thế giới!" << endl; // Ghi dữ liệu vào tệp
        tep_tin << "Đây là một ví dụ về việc làm việc với tệp tin trong C++." << endl;
        tep_tin.close(); // Đóng tệp tin
        cout << "Đã tạo tệp tin và ghi dữ liệu thành công!" << endl;
    } else {
        cout << "Không thể tạo tệp tin!" << endl;
    }

    // Đọc dữ liệu từ tệp
    ifstream doc_tep("example.txt"); // Mở tệp tin để đọc
    if (doc_tep.is_open()) { // Kiểm tra xem tệp đã được mở chưa
        string dong; // Chuỗi để chứa từng dòng của tệp
        while (getline(doc_tep, dong)) { // Đọc từng dòng của tệp
            cout << dong << endl; // In ra màn hình
        }
        doc_tep.close(); // Đóng tệp tin
    } else {
        cout << "Không thể đọc tệp tin!" << endl;
    }

    return 0;
}
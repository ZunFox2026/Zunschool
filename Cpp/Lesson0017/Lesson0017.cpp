#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // Tạo tệp tin và ghi dữ liệu
    ofstream tep_tin("data.txt");
    if (tep_tin.is_open()) {
        // Ghi dữ liệu vào tệp tin
        tep_tin << "Xin chào, thế giới!" << endl;
        tep_tin << "Đây là một chương trình mẫu về làm việc với tệp tin." << endl;
        tep_tin.close();
        cout << "Đã tạo tệp tin và ghi dữ liệu thành công!" << endl;
    } else {
        cout << "Không thể tạo tệp tin!" << endl;
    }

    // Đọc dữ liệu từ tệp tin
    ifstream doc_tep_tin("data.txt");
    if (doc_tep_tin.is_open()) {
        char line[100];
        while (doc_tep_tin.getline(line, 100)) {
            // In dữ liệu đọc từ tệp tin
            cout << line << endl;
        }
        doc_tep_tin.close();
        cout << "Đã đọc dữ liệu từ tệp tin thành công!" << endl;
    } else {
        cout << "Không thể đọc tệp tin!" << endl;
    }

    return 0;
}
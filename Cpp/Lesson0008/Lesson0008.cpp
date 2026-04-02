#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // Tạo tệp tin và ghi dữ liệu vào tệp
    ofstream tep_tin("xu_ly_tep.txt");
    if (tep_tin.is_open()) {
        // Ghi dữ liệu vào tệp
        tep_tin << "Đây là dữ liệu trong tệp tin.\n";
        tep_tin << "Tệp tin được tạo và ghi dữ liệu thành công.\n";
        tep_tin.close();
        cout << "Tạo và ghi tệp tin thành công.\n";
    } else {
        cout << "Không thể tạo tệp tin.\n";
    }

    // Đọc dữ liệu từ tệp
    ifstream doc_tep("xu_ly_tep.txt");
    if (doc_tep.is_open()) {
        string dong;
        while (getline(doc_tep, dong)) {
            // In từng dòng trong tệp
            cout << dong << endl;
        }
        doc_tep.close();
        cout << "Đọc tệp tin thành công.\n";
    } else {
        cout << "Không thể đọc tệp tin.\n";
    }

    return 0;
}
#include <iostream>
#include <fstream> // Thư viện để làm việc với file

using namespace std;

int main() {
    // Tạo một file mới tên là "example.txt" trong chế độ viết (write)
    ofstream outFile("example.txt");
    
    // Kiểm tra nếu file được mở thành công
    if (outFile.is_open()) {
        // Viết nội dung vào file
        outFile << "Xin chào, đây là nội dung trong file example.txt" << endl;
        
        // Đóng file
        outFile.close();
        cout << "Nội dung đã được ghi vào file example.txt thành công!" << endl;
    } else {
        cout << "Không thể mở file!" << endl;
    }

    // Tạo một file mới tên là "example.txt" trong chế độ đọc (read)
    ifstream inFile("example.txt");
    
    // Kiểm tra nếu file được mở thành công
    if (inFile.is_open()) {
        // Đọc nội dung từ file
        string line;
        while (getline(inFile, line)) {
            cout << "Nội dung trong file: " << line << endl;
        }
        
        // Đóng file
        inFile.close();
    } else {
        cout << "Không thể mở file!" << endl;
    }

    return 0;
}
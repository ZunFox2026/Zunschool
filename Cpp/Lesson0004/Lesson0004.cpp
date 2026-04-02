#include <iostream>
#include <string>
using namespace std;

int main() {
    // Khai báo biến chuỗi
    string chuoi;

    // Nhập chuỗi từ người dùng
    cout << "Nhap mot chuoi: ";
    getline(cin, chuoi);

    // In ra chuỗi vừa nhập
    cout << "Chuoi vua nhap: " << chuoi << endl;

    // Lấy độ dài của chuỗi
    int doDai = chuoi.length();
    cout << "Do dai cua chuoi: " << doDai << endl;

    // Lấy ký tự tại vị trí nhất định trong chuỗi
    cout << "Nhap vi tri ky tu (0-" << doDai - 1 << "): ";
    int viTri;
    cin >> viTri;
    cin.ignore(); // Bỏ dấu newline trong buffer
    if (viTri >= 0 && viTri < doDai) {
        cout << "Ky tu tai vi tri " << viTri << ": " << chuoi[viTri] << endl;
    } else {
        cout << "Vi tri khong hop le!" << endl;
    }

    // Tìm kiếm chuỗi con trong chuỗi
    cout << "Nhap chuoi con can tim: ";
    string chuoiCon;
    getline(cin, chuoiCon);
    if (chuoi.find(chuoiCon) != string::npos) {
        cout << "Chuoi con " << chuoiCon << " co trong chuoi!" << endl;
    } else {
        cout << "Chuoi con " << chuoiCon << " khong co trong chuoi!" << endl;
    }

    // Thay thế chuỗi con trong chuỗi
    cout << "Nhap chuoi con can thay the: ";
    string chuoiConThayThe;
    getline(cin, chuoiConThayThe);
    cout << "Nhap chuoi moi: ";
    string chuoiMoi;
    getline(cin, chuoiMoi);
    size_t viTriThayThe = chuoi.find(chuoiConThayThe);
    if (viTriThayThe != string::npos) {
        chuoi.replace(viTriThayThe, chuoiConThayThe.length(), chuoiMoi);
        cout << "Chuoi sau khi thay the: " << chuoi << endl;
    } else {
        cout << "Chuoi con " << chuoiConThayThe << " khong co trong chuoi!" << endl;
    }

    return 0;
}
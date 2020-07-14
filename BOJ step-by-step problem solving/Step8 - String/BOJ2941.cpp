#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void) {
    vector<string> croatia = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    int index;
    string str;

    cin >> str;
    for(int i = 0; i < croatia.size(); i++) {
        while (true) {
            index = str.find(croatia[i]);
            if (index == string::npos) // find를 통해 찾았는데 없으면 npos를 리턴하게됨.
                break;
            str.replace(index, croatia[i].length(), "*");
        }
    }
    cout << str.length();
}

// 참조 : https://cryptosalamander.tistory.com/15

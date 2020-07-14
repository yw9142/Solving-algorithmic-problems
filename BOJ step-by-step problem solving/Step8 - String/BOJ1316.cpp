#include <iostream>
#include <string>

using namespace std;

bool Check(string str) {
    bool alphabet[26] = {false};

    for (int i = 0; i < str.length(); i++) {
        if (alphabet[str[i] - 97] == true)
            return false;
        else {
            char temp = str[i];
            alphabet[str[i] - 97] = true;

            while (true) {
                if (temp != str[++i]) {
                    i--;
                    break;
                }
            }
        }
    }
    return true;
}

int main(void) {
    int N;
    int count = 0;
    string str;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> str;
        if (Check(str))
            count++;
    }
    cout << count;
    return (0);
}

// 출처 : https://blockdmask.tistory.com/150

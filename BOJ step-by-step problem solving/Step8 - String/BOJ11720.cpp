#include <iostream>

using namespace std;

int main(void) {
    int length;
    cin >> length;
    char ch;
    int sum = 0;

    for (int i = 0; i < length; i++) {
        cin >> ch;
        sum += (ch - '0'); // ASCII
        // 파이썬의 (int) 느낌?
    }
    cout << sum;
    return (0);
}

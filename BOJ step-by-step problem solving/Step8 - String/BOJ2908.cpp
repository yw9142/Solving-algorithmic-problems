#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(void) {
    int A, B;
    int newA = 0, newB = 0;

    cin >> A >> B;
    for (int i = 0; i < 3; i++) {
        newA += (A % 10) * pow(10, 2 - i);
        newB += (B % 10) * pow(10, 2 - i);
        A /= 10;
        B /= 10;
    }

    cout << max(newA, newB) << endl;
    return (0);
}

// 참고 : https://blockdmask.tistory.com/144

#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int N;

    cin >> N;

    for (int i = 1; i < N * 2; i++) {
        for (int j = 1; j <= N - abs(N - i); j++) {
            cout << '*';
        }
        cout << '\n';
    }
    return (0);
}

// 참고 : https://j3sung.tistory.com/390
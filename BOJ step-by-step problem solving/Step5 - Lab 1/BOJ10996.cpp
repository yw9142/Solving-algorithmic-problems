#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int N;

    cin >> N;
    for (int i = 1; i <= N * 2; i++) {
        for (int j = 1; j <= N; j++) {
            if (i % 2 == 0) {
                if (j % 2 == 0)
                    cout << '*';
                else
                    cout << ' ';
            } else {
                if (j % 2 == 0)
                    cout << ' ';
                else
                    cout << '*';
            }
        }
        cout << '\n';
    }
    return (0);
}

// 참고 : https://jow1025.tistory.com/54

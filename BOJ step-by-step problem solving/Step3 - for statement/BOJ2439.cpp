#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false); // iostream 과 stdio의 동기화를 끊어서 속도 향상. but 둘중 하나만 사용 가능

    int N;
    cin >> N;

    for (int i = 1; i <= N; i++) {
        for (int j = 0; j < N; j++) { // 5 4 3 2 1
            if (j < N - i) {
                cout << ' ';
            } else {
                cout << '*';
            }
        }
        cout << '\n';
    }
    return (0);
}

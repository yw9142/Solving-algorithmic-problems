#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int N;

    cin >> N;
    int count = N - 1;

    for (int i = 1; i < N * 2; i++) {
        for (int j = 1; j < N * 2; j++) {
            if (j >= N - count && j <= N + count) {
                cout << '*';
            }
            else if (j < N - count) {
                cout << ' ';
            }
        }
        if (i < N)
            count--;
        else
            count++;
        cout << '\n';
    }
    return (0);
}

// 참고 : https://blog.naver.com/PostView.nhn?blogId=legendmic2&logNo=221312980652

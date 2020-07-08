#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int A, B, C;
    int arr[10] = {0};

    cin >> A >> B >> C;
    int answer = A * B * C;

    while (answer != 0) {
        arr[answer % 10]++; // 숫자 위치배열에 증가
        answer /= 10; // 끝자리 증가 후 잘라내기
    }

    for (int i : arr) {
        cout << i << '\n';
    }
    return (0);
}


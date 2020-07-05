#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false); // iostream 과 stdio의 동기화를 끊어서 속도 향상. but 둘중 하나만 사용 가능

    int N, X;
    cin >> N >> X;
    int arr;

    for (int i = 0; i < N; i++) {
        cin >> arr;

        if (arr < X) {
            cout << arr << ' ';
        }
    }
    return (0);
}

/*
#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false); // iostream 과 stdio의 동기화를 끊어서 속도 향상. but 둘중 하나만 사용 가능

    int N, X;
    cin >> N >> X;
    int arr[N];

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    for (int i = 0; i < N; i++) {
        if (arr[i] < X) {
            cout << arr[i] << ' ';
        }
    }
    return (0);
}
*/

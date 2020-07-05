#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false); // iostream 과 stdio의 동기화를 끊어서 속도 향상. but 둘중 하나만 사용 가능

    int N;
    int A, B;

    cin >> N;
    for (int i = 1; i <= N; i++) {
        cin >> A >> B;
        cout << "Case #" << i << ": " << A + B << '\n'; // endl == 버퍼를 비워서 시간이 느려짐. // 상당히 버퍼 비우는데 시간이 오래걸리는 듯 함.
    }
    return (0);
}

#include <iostream>

using namespace std;

int main(void) {
    cin.tie(NULL); // cin cout의 묶음을 풀어 cout ; cin의 경우 cin이 먼저 작동.
    // cout는 디폴트에서는 출력명령을 내리거나 버퍼가 가득찼을 경우에만 flushed되고 출력됨.
    ios_base::sync_with_stdio(false); // iostream 과 stdio의 동기화를 끊어서 속도 향상. but 둘중 하나만 사용 가능

    int N;
    int A, B;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A >> B;
        cout << A + B << '\n'; // endl == 버퍼를 비워서 시간이 느려짐. // 상당히 버퍼 비우는데 시간이 오래걸리는 듯 함.
    }
    return (0);
}

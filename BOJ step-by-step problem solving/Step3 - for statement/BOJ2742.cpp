#include <iostream>

using namespace std;

int main(void) {
    cin.tie(NULL); // cin cout의 묶음을 풀어 cout ; cin의 경우 cin이 먼저 작동.
    // cout는 디폴트에서는 출력명령을 내리거나 버퍼가 가득찼을 경우에만 flushed되고 출력됨.
    ios_base::sync_with_stdio(false); // iostream 과 stdio의 동기화를 끊어서 속도 향상. but 둘중 하나만 사용 가능

    int N;

    cin >> N;
    for (int i = N; i != 0; i--) {
        cout << i << '\n';
    }
    return (0);
}

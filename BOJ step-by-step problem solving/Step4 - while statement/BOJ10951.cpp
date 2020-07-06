#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int A, B;

    while (cin >> A >> B) {
        cout << A + B << '\n';
    }
    return (0);
}

/*
 * 테스트 케이스의 개수를 알 수 없기에 입력을 EOF까지 받도록 설정함.
 */

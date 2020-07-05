#include <iostream>

using namespace std;

int main(void) {
    int N;
    int A, B;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A >> B;
        cout << A + B << endl;
    }
    return (0);
}

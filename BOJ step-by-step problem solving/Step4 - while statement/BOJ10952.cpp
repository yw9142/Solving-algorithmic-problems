#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int A, B;

    while (1) {
        cin >> A >> B;
        if (A != 0 && B != 0)
            cout << A + B << '\n';
        else
            break;
    }
    return (0);
}

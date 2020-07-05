#include <iostream>

using namespace std;

int main(void) {
    int N;

    cin >> N;
    for (int i = N - 1; i != 0; --i) {
        N += i;
    }
    cout << N << endl;
    return (0);
}

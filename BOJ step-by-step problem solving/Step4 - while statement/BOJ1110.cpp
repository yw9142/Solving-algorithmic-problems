#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int N; // 0 < N < 99
    int sum, result, first, second;

    int count = 0;

    cin >> N;
    if (N < 0 || N > 99)
        return (0);

    if (N < 10)
        N *= 10;

    result = N;

    while (1) {
        first = result / 10;
        second = result % 10;
        sum = first + second;
        result = (second * 10) + (sum % 10);
        count += 1;

        if (N == result)
            break;
    }
    cout << count << '\n';
    return (0);
}

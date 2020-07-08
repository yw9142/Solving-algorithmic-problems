#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int N;
    int min = 1000000;
    int max = -1000000;

    cin >> N;
    int array[N + 1];

    for (int i = 0; i < N; i++) {
        cin >> array[i];
        if (min > array[i])
            min = array[i];

        if (max < array[i])
            max = array[i];
    }

    cout << min << ' ' << max << '\n';
    return (0);
}

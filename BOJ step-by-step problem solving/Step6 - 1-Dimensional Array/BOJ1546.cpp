#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int N;

    cin >> N;

    int arr[N];
    int maxS = 0;

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
        maxS = max(maxS, arr[i]);
    }

    double total = 0.0;

    for (int i = 0; i < N; i++) {
        total += (double) ((arr[i] / (double) maxS) * 100);
    }

    cout << fixed;
    cout.precision(4);
    cout << (double) (total / N) << '\n';

    return (0);
}



#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int arr[10] = {0};
    int remainder[42] = {0};
    int count = 0;

    for (int &i : arr) {
        cin >> i;
        if (!remainder[i % 42]++) // 0이 아니면 조건 통과
            count++; // 즉 0 인곳에서만 sum이 증가
    }

    cout << count << '\n';
    return (0);
}


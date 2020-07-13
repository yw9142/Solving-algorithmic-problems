#include <iostream>

#define N 10001
using namespace std;
bool arr[N];

int solution(int n) {
    int sum = n;

    while (true) {
        if (n == 0)
            break;
        sum += n % 10;
        n /= 10;
    }
    return (sum);
}

int main(void) {

    for (int i = 1; i < N; i++) {
        int index = solution(i);

        if (index <= N)
            arr[index] = true;
    }

    for (int i = 1; i < N; i++) {
        if (!arr[i]) // arr[i] == False
            cout << i << '\n';
    }
    return (0);
}

// 출처 : https://blockdmask.tistory.com/160

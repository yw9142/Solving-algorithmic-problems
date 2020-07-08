#include <iostream>
#include <cstring>

using namespace std;

void solution(char arr[], int &sum) {

    int point = 0;
    sum = 0;
    scanf("%s", arr);

    for (int i = 0; i < strlen(arr); i++) {
        if (arr[i] == 'O') {
            point++;
            sum += point;
        } else {
            point = 0;
        }
    }
}

int main(void) {
    int N;
    char arr[80];
    int sum = 0;

    cin >> N;
    for (int i = 0; i < N; i++) {
        solution(arr, sum);
        cout << sum << '\n';
    }
    return (0);
}

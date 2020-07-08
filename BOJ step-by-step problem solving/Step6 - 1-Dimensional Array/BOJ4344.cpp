#include <iostream>

using namespace std;

int main(void) {
    int C;

    cin >> C;
    for (int i = 0; i < C; i++) {
        int num;
        int sum = 0;
        int count = 0;
        double average;

        scanf("%d", &num);
        int arr[num];

        for (int j = 0; j < num; j++) {
            scanf("%d", &arr[j]);
            sum += arr[j];
        }
        average = sum / num;

        for (int q = 0; q < num; q++)
            if (average < arr[q])
                count++;

        cout << fixed;
        cout.precision(3);
        cout << (float) (count) / num * 100 << '%' << '\n';
    }
    return (0);
}

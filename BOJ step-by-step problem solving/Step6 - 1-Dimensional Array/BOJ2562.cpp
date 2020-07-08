#include <iostream>
#include <climits>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int Num;
    int count;
    int Max = INT_MIN;

    for (int i = 1; i < 10; i++) {
        cin >> Num;
        if (Max < Num) {
            Max = Num;
            count = i;
        }
    }
    cout << Max << '\n' << count << '\n';
    return (0);
}

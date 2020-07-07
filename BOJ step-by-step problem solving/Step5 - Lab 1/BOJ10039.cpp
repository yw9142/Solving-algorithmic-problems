#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int score, sum = 0;
    for (int i = 0; i < 5; i++) {
        cin >> score;
        if (score < 40) {
            score = 40;
        }
        sum += score;
    }
    int average = sum / 5;

    cout << average << '\n';
    return (0);
}

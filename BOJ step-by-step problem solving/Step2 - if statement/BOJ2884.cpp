#include <iostream>
using namespace std;

int main(void){
    int H, M;
    cin >> H >> M;

    if (M < 45) {
        H -= 1;
        if (H < 0) {
            H += 24;
        }
        M += 15;
        cout << H << ' ' << M << endl;
    }
    else {
        M -= 45;
        cout << H << ' ' << M << endl;
    }
    return (0);
}

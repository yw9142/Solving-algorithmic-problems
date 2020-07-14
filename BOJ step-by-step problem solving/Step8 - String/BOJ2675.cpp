#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int num;
    cin >> num;
    int length;
    string str;

    for (int i = 0; i < num; i++) {
        cin >> length;
        cin >> str;

        for (char j : str) {
            for (int q = 0; q < length; q++) {
                cout << j;
            }
        }
        cout << '\n';
    }
    cout << '\n';
    return (0);
}

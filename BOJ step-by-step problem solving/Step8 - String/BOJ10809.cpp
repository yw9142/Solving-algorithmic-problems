#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    int index;

    cin >> str;
    for (int i = 97; i < 123; i++) {
        index = str.find(i);
        cout << index << " ";
    }

    cout << '\n';
    return (0);
}

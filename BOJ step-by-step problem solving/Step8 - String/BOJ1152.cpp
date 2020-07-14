#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int count = 1;
    string str;
    getline(cin, str);

    if (str.at(0) == ' ') // operator[index]가 at보다 빠르지만 범위를 벗어났을 때 예외를 리턴하지 않음.
        count = 0;
    int i = 0;

    while (i < str.length()) {
        if (str.at(i) == ' ')
            count++;
        i++;
    }

    if (str.at(i - 1) == ' ')
        count--;

    cout << count << '\n';
    return (0);
}

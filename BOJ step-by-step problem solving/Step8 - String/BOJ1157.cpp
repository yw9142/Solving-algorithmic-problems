#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int frequency[26] = {0};
    int max = 0;
    char solution;
    string str;

    cin >> str;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] >= 65 && str[i] <= 90) // 대문자
            frequency[str[i] - 65] += 1;
        else if (str[i] >= 97 && str[i] <= 122) // 소문자
            frequency[str[i] - 97] += 1;
    }

    for (int i = 0; i < (sizeof(frequency) / sizeof(*frequency)); i++) {
        if (frequency[i] > max) { // 빈도 maximum 찾기
            solution = i + 65; // maxi가 존재하면 ASCII를 활용해 대문자 알파벳 대입
            max = frequency[i]; // max값 변경

        } else if (frequency[i] == max) // 만약 maxi값이 같은게 존재하면 ? 대입
            solution = '?';
    }
    cout << solution << '\n';
    return (0);
}

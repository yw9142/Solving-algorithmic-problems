#include <iostream>
#include <vector>

using namespace std;

void hansoo(int number, vector<int> &a) {
    for (int i = 0; i <= number; i++) {
        if (i < 100 ||(i/100 - (i/10)%10) == ((i/10)%10 - (i%10))) // 1~2자리수 비교 and 2~3자리수 비교 (만약 제한이 1000을 넘었다면 다른 코드로 바꿨어야함.)
            a.push_back(i);
    }
}

int main(void) {
    int number;
    vector<int> array;
    cin >> number;

    hansoo(number, array);

    cout << array.size() - 1 << '\n';
    return (0);
}

// 참조 : https://dalgong2.tistory.com/29

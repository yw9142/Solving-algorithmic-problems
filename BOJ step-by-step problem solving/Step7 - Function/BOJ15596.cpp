#include <iostream>
#include <vector>

using namespace std;

long long sum(vector<int> &a) {
    long long nsum = 0;
    vector<int>::iterator iter;
    for (iter = a.begin(); iter < a.end(); iter++) // auto는 타입추론을 제공해주지만 오류가 발생할 가능성이 존재하므로 사용을 안하는 것이 좋을듯 함.
        nsum += *iter;
    return (nsum);
}

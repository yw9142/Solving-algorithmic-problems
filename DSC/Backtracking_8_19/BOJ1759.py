from itertools import combinations

vowel = {'a', 'e', 'i', 'o', 'u'}  # 모음
L, C = map(int, input().split())  # L = 암호 길이 / C = 조합 가능한 알파벳의 수
string = sorted(list(input().split()))  # string = 조합할 알파벳 입력

answer = sorted(list(combinations(string, L)))  # 오름차순으로 정렬된 가능한 알파벳의 모든 조합 추출

for i in answer:  # 이제 조합식을 하나씩 보면서 자음이 2개 이상으로 구성되어 있는지 판별
    difference = set(i) - vowel  # answer[i] - 모음(차집합) = 남은 것은 자음뿐
    if 1 < len(difference) < L:  # 자음이 2개 이상 and 모음이 1개 이상
        print(''.join(i))  # 출력

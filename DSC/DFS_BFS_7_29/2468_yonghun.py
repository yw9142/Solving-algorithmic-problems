N = int(input())  # N 입력
area = [list(map(int, input().split(' '))) for i in range(N)]  # area 행열 입력

max_value = 0
for i in range(N):
    for j in range(N):
        max_value = max(max_value, area[i][j])

answer = 0

for q in range(max_value + 1):  # 0 ~ max value까지 전부 탐색해서 안전영역이 가장 많은 것을 answer로 출력
    visited = [[False for j in range(N)] for i in range(N)]  # N^2의 공간을 생성한 후 모두 False로 설정
    n = 0
    for i in range(N):  # 행
        for j in range(N):  # 열
            if not visited[i][j]:  # 방문하지 않았다면
                if area[i][j] > q:  # 탐색중인 수보다 크다면 DFS실행
                    stack = [(i, j)]
                    n += 1  # 대피소 영역 증가
                    while stack:
                        a, b = stack.pop()
                        visited[a][b] = True
                        if a > 0 and not visited[a - 1][b] and area[a - 1][b] > q:  # 상
                            stack.append((a - 1, b))
                        if b > 0 and not visited[a][b - 1] and area[a][b - 1] > q:  # 좌
                            stack.append((a, b - 1))
                        if a < N - 1 and not visited[a + 1][b] and area[a + 1][b] > q:  # 하
                            stack.append((a + 1, b))
                        if b < N - 1 and not visited[a][b + 1] and area[a][b + 1] > q:  # 우
                            stack.append((a, b + 1))

                else:
                    visited[i][j] = True
    answer = max(answer, n)

print(answer)

# 출처 : https://blog.setsuna.kr/140?category=318532

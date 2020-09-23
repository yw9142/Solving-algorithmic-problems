from sys import stdin
from itertools import combinations
from copy import deepcopy

dx = [1, 0, -1, 0] # 동 서 남 북
dy = [0, 1, 0, -1] # 동 서 남 북

emptys = []  # 비어 있는 좌표
teachers = []  # 선생이 있는 좌표
students = []  # 학생이 있는 좌표


def DFS(board, x, y, idx):
    global n
    if x < 0 or x >= n or y < 0 or y >= n or board[x][y] == 'O':
        return
    else:  # 장애물이 없으면 선생님의 위치를 기준 동서남북 방향으로 'T'를 채워넣음.
        board[x][y] = 'T'
        DFS(board, x + dx[idx], y + dy[idx], idx)  # IDX는 동서남북을 가르키는 기능


def check():
    copy_board = deepcopy(board)
    for [x, y] in teachers:
        for i in range(4):
            DFS(copy_board, x, y, i)
    for [x, y] in students:
        if copy_board[x][y] != 'S':
            return False  # 학생 위치의 BOARD가 'S'가 아닌 경우 선생님에게 잡혀서 'T'로 바뀐경우이니 실패

    return True  # 아니라면 안잡힘


def solution():
    for case in list(combinations(emptys, 3)):  # list(combinations(emptys, 3)) 장애물 3개 놓을 때 모든 경우의 수
        for [x, y] in case:
            board[x][y] = 'O'
        if check():  # 케이스별로 전부 확인
            return "YES"  # 그래서 TRUE가 나오면 안잡히는 경우가 존재하는 것이니까 YES
        for [x, y] in case:  # 초기화
            board[x][y] = 'X'

    return "NO"  # 한번도 체크에 걸리지 않았다면 안잡히는 경우가 한번도 없는 것


n = int(input())  # N 입력
board = [list(map(str, stdin.readline().split())) for _ in range(n)]  # 보드판 입력

for i in range(n):
    for j in range(n):
        if board[i][j] == 'X':
            emptys.append([i, j])
        elif board[i][j] == 'T':
            teachers.append([i, j])
        elif board[i][j] == 'S':
            students.append([i, j])

print(solution())

# 출처 : https://choichumji.tistory.com/85

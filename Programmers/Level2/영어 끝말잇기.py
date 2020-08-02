def solution(n, words):
    answer = [0, 0]

    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] or words[i] in words[0:i]:
            answer = [(i % n) + 1, (i // n) + 1]
            break

    return answer

# 단어의 끝부분과 시작부분 확인 and 단어가 중복되는지 확인 둘중하나라도 걸린다면 answer 좌표 수정

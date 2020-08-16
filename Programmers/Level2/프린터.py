from collections import deque


def solution(priorities, location):
    answer = 0
    deque_priorities = deque([(v, i) for i, v in enumerate(priorities)])  # 이 부분은 다른곳에서 보고 배웠다. index 번호같이 반환
    # 출처 : https://eda-ai-lab.tistory.com/461

    while deque_priorities:
        value = deque_priorities.popleft() # 왼쪽 pop
        # value[0] == item
        # value[1] == item_index_location

        if deque_priorities and max(deque_priorities)[0] > value[0]:  # deque값이 존재 and max값이 value보다 크다면
            deque_priorities.append(value)  # 오른쪽에 다시 붙이기
        else:
            answer += 1
            if value[1] == location:  # index_location이 location과 같다면 그 부분이 answer이 됨.
                break
    return answer

def solution(skill, skill_trees):
    answer = 0
    from collections import deque
    for tree in skill_trees:
        skill_list = deque(skill)  # ['C', 'B', 'D']

        for sit in tree:  # for else (for 문제없이 다 돌면 else 실행)
            if sit in skill and sit != skill_list.popleft():
                break
        else:
            answer += 1

    return answer

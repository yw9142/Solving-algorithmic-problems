def solution(d, budget):
    count = 0
    d.sort()
    # greedy?
    for i in d:
        budget -= i
        count += 1
        if budget < 0:
            count -= 1
            break
    return count

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    count = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            count = -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        count += 1

    return count

# 성능이 너무 안좋은 것 같다..

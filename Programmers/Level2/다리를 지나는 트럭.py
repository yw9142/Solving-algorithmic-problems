from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)  # 다리길이만큼 들어갈 수 있음 (무게 허용선에서)
    truck_weights = deque(truck_weights)  # deque로 양방향으로 추출 가능
    bridge_weight = sum(bridge)

    while bridge:
        bridge_weight -= bridge[0]  # 다리위의 무게에서 기존 0번 인덱스 무게 빼기
        bridge.popleft()  # 마찬가지로 다리위에 트럭 제거
        answer += 1

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                bridge_weight += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return answer

# 출처 : https://duwjdtn11.tistory.com/539

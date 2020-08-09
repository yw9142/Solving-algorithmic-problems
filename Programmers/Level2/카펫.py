def solution(brown, red):
    x = (brown + 4 + ((brown + 4) ** 2 - 16 * (brown + red)) ** 0.5) / 4
    y = (brown + red) // x
    return [max(x, y), min(x, y)]

# 출처 : https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B9%B4%ED%8E%AB-in-python
# 점화식은 생각 못해봣는데 신기하다.

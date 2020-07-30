def solution(n, a, b):
    count = 0  # 서로 겨루기 위해 참가해야할 경기 수
    while a != b:  # 참가 번호가 같지 않다면
        a = (a + 1) // 2  # 다음 라운드에 진출 했을 때 가지게 될 번호 수
        b = (b + 1) // 2
        count += 1  # 경기수 1 증가
    return count
# 4 7 / 2 4 / 1 2 / 1 1
# 참고 : https://m.blog.naver.com/kbsdr11/221600346889


# 다른사람의 코드
# 대단한코드 어떻게 이런 생각을 하는지가 궁금하다
# def solution(n,a,b):
#     return ((a-1)^(b-1)).bit_length()

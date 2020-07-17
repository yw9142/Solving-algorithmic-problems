def solution(numbers):
    numbers = list(map(str, numbers))
    ## ['6', '10', '2']
    numbers.sort(key=lambda x: x * 10, reverse=True)
    ## 문자열을 기준으로 reverse 하면 맨 앞 숫자만 보기때문에 역순 정렬하면 큰 순서대로 나옴.
    return str(int(''.join(numbers)))

# 참고 : https://sinsomi.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Python-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%88%98-%EC%B4%88%EC%BD%94%EB%8D%94

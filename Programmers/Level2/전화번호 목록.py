def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1]:
            answer = False
            break

    return answer

# 접두어를 찾는 문제라 가능한 것. 전체를 확인할 필요 없이 sort 이후 인접한 원소만 비교하면 됨.

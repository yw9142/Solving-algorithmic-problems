def solution(people, limit):
    people.sort()  # 50 50 70 80

    count = 0
    min = 0
    max = len(people) - 1  # list index list[3]

    while min <= max:
        if people[min] + people[max] <= limit:  # 최소 + 최대 합이 limit 이하라면 최솟값과 최댓값 둘다 태우기
            min += 1
        max -= 1  # if 안걸렸으면 그냥 최댓값 한명만 태워서 출발
        count += 1
    ## min += 1 최솟값 태우고
    ## max += 1 최댓값 태우고

    return count

# index slicing

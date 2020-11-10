def escape():
    N = int(input())

    lists = list(map(int, input().split()))
    lists.append(0)
    lists.append(0)

    count = 0
    for i in range(N):
        if lists[i] == 1:
            lists[i] = 0
            count += 1
            lists[i + 1] = not lists[i + 1]
            lists[i + 2] = not lists[i + 2]
    return count


print(escape())

def ispalindrome(word):
    check = True
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            check = False
            break

    return check

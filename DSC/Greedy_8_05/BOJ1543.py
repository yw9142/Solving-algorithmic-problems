# -*- encoding: utf-8 -*-

base_word = input()  # ababababa
search_word = input()  # aba
count = 0
word_index = 0

while word_index <= len(base_word) - len(search_word):  # 전체길이 - 찾는단어 길이
    if base_word[word_index:word_index + len(search_word)] == search_word:  # 같다면
        count += 1
        word_index += len(search_word)  # 찾는단어 길이만큼 밀어내기
    else:  # 안같으면
        word_index += 1  # 한칸만 밀고

print(count)

# ex) ababababa ->(count+=1) bababa ->(count+=1) ababa -> end

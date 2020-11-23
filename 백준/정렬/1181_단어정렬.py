# 1181 단어 정렬
# 단어의 순서를 정의하여 정렬하는 문제

import sys

n = int(input())

word_list = []

for i in range(n):
    word_list.append(str(input()))

word_list = sorted(list(set(word_list)), key=lambda x : (len(x),x))

for word in word_list:
    print(word)
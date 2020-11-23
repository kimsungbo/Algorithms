# 2941 크로아티아 알파벳
# 크로아티아 알파벳의 개수를 세는 문제

string = input()

croatic_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 문자열에 크로아티아 알파벳이 포한된경우 x로 치환하여 한 단어로 생각
for alphabet in croatic_alphabet:
    string = string.replace(alphabet, 'x')

print(len(string))
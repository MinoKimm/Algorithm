S = int(input())

for R in range(S):
    cnt, word = input().split()
    for i in word:
        print(i * int(cnt), end='')
    print()
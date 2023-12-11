dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0
word = list(input())

for i in word:
    for j in dial:
        if i in str(j):
            num = dial.index(j) + 3
            cnt += num
print(cnt)
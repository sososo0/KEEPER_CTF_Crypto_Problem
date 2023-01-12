n = 0
x = int(input())
y = input()
for i in range(6):
    while n < len(y):
        print(y[n+i], end = '')
        n += x
    n = 0
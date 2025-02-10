k, r = map(int, input().split())
n = 1
while True:
    total = n * k
    if total % 10 == r or total % 10 == 0:
        print(n)
        break
    n += 1

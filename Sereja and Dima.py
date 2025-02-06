n = int(input().strip())  
cards = list(map(int, input().split()))  
sereja, dima = 0, 0
turn = True  
left, right = 0, n - 1
while left <= right:
    if cards[left] > cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1
    if turn:
        sereja += chosen
    else:
        dima += chosen
    turn = not turn  # Switch turns
print(sereja, dima)

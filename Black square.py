a1, a2, a3, a4 = map(int, input().split())
s = input().strip()
calories = [a1, a2, a3, a4]
total_calories = 0
for char in s:
    total_calories += calories[int(char) - 1]  

print(total_calories)

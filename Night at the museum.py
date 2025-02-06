s = input().strip()
current = 'a'
rotations = 0

for char in s:
    diff = abs(ord(char) - ord(current))
    rotations += min(diff, 26 - diff)
    current = char

print(rotations)

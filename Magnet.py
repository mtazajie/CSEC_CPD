n = int(input().strip())  
prev = input().strip()  
groups = 1  

for i in range(n - 1):
    curr = input().strip()
    if curr != prev:
        groups += 1  
    prev = curr  

print(groups)

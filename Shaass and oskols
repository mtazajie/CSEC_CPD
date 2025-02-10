# Read the number of wires
n = int(input())

# Read the initial number of birds on each wire
a = list(map(int, input().split()))

# Read the number of shots
m = int(input())

# Process each shot
for _ in range(m):
    xi, yi = map(int, input().split())
    xi -= 1  # Convert to 0-based index

    # Birds to the left of the shot bird move to the wire above
    if xi > 0:
        a[xi - 1] += yi - 1

    # Birds to the right of the shot bird move to the wire below
    if xi < n - 1:
        a[xi + 1] += a[xi] - yi

    # Remove the shot bird and update the current wire
    a[xi] = 0

# Print the final number of birds on each wire
for birds in a:
    print(birds)

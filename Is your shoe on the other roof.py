# Read the four colors
colors = list(map(int, input().split()))

# Use a set to find the number of unique colors
unique_colors = set(colors)

# Calculate the number of additional horseshoes needed
additional_horseshoes = 4 - len(unique_colors)

# Print the result
print(additional_horseshoes)

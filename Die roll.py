from math import gcd

# Read Yakko's and Wakko's rolls
Y, W = map(int, input().split())

# Determine the maximum of Yakko's and Wakko's rolls
max_yw = max(Y, W)

# Calculate the number of favorable outcomes for Dot
favorable = 6 - max_yw + 1

# Simplify the fraction
common_divisor = gcd(favorable, 6)
numerator = favorable // common_divisor
denominator = 6 // common_divisor

# Output the result in the required format
print(f"{numerator}/{denominator}")

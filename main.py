#! user/bin/env python3

def sort(width, height, length, mass):
    # Calculate the volume of the package
    volume = width * height * length
    # Determine if the package is bulky
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    # Determine if the package is heavy
    is_heavy = mass >= 20
    # Determine the category based on the conditions

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Test cases
print(sort(200, 100, 50, 10))  # Output: "SPECIAL" (bulky but not heavy)
print(sort(100, 100, 100, 25))  # Output: "SPECIAL" (heavy but not bulky)
print(sort(200, 200, 200, 25))  # Output: "REJECTED" (both bulky and heavy)
print(sort(50, 50, 50, 10))  # Output: "STANDARD" (neither bulky nor heavy)

# Boundary conditions for bulky
print(sort(100, 100, 100, 10))  # Output: "SPECIAL" (volume = 1,000,000, bulky but not heavy)
print(sort(150, 50, 50, 10))    # Output: "SPECIAL" (width = 150, bulky but not heavy)
print(sort(50, 150, 50, 10))    # Output: "SPECIAL" (height = 150, bulky but not heavy)
print(sort(50, 50, 150, 10))    # Output: "SPECIAL" (length = 150, bulky but not heavy)

# Boundary conditions for heavy
print(sort(50, 50, 50, 20))  # Output: "SPECIAL" (mass = 20, heavy but not bulky)

# Combination of bulky and heavy
print(sort(100, 100, 100, 20))  # Output: "REJECTED" (bulky and heavy)
print(sort(100, 100, 99, 19))   # Output: "STANDARD" (neither bulky nor heavy)

# Neither bulky nor heavy
print(sort(10, 10, 10, 5))  # Output: "STANDARD" (neither bulky nor heavy)

# Extreme values
print(sort(1000, 1000, 1000, 100))  # Output: "REJECTED" (extremely bulky and heavy)
print(sort(1, 1, 1, 0))             # Output: "STANDARD" (extremely small and light)

# Zero or negative values
print(sort(0, 100, 100, 10))  # Output: "STANDARD" (volume = 0, not bulky or heavy)
print(sort(-50, 100, 100, 10))  # Output: "STANDARD" (negative width, not bulky or heavy)
print(sort(50, 50, 50, -10))  # Output: "STANDARD" (negative mass, not bulky or heavy)

# Single large dimension
print(sort(1000, 1, 1, 10))  # Output: "SPECIAL" (bulky but not heavy)

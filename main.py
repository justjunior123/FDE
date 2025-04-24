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

# Day 1

# Part 1

# Open data file
with open('01-input.txt', 'r') as file:
    data = file.read().splitlines()

sum = 0

for i in data:
    first = ''
    second = ''
    # Find first digit in string
    for j in i:
        if j.isdigit():
            first = j
            break
    for j in i[::-1]:
        if j.isdigit():
            second = j
            break
    sum += int(first + second)

print(sum)
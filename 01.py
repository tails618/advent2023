# Day 1: Trebuchet?!

# Open data file
with open('01-input.txt', 'r') as file:
    data = file.read().splitlines()

numWordDict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

sum = 0

for input in data:
    first = ''
    second = ''
    # Iterate over each character in the string forwards
    for char in range(len(input)):
        breakFlag = False
        # If the character is a digit, set it as the first number, and break the loop
        if input[char].isdigit():
            first = input[char]
            break
        # If the character is a number word, set it as the first number, and break the loop
        for numWord in numWordDict:
            if input[char:char+len(numWord)] == numWord:
                first = numWordDict[numWord]
                breakFlag = True
                break
        if breakFlag:
            break
    # Now do it again, backwards
    for char in range(len(input)):
        breakFlag = False
        if input[::-1][char].isdigit():
            second = input[::-1][char]
            break
        for numWord in numWordDict:
            if input[::-1][char:char+len(numWord)] == numWord[::-1]:
                second = numWordDict[numWord]
                breakFlag = True
                break
        if breakFlag:
            break
        
    sum += int(first + second)

print(sum)
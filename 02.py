# Day 2: Cube Conundrum

# Open data file
with open('02-input.txt', 'r') as file:
    data = file.read().splitlines()

sumColors = 0
sumPowers = 0

for game in data:
    # Find the ID, between the first space and the first (only) colon
    colonIdx = game.find(':')
    id = game[game.find(' ') + 1:colonIdx]

    # Find the game data, which is everything after the colon and the space after it,
    # then split it into sets
    gameData = game[colonIdx + 2:]
    sets = gameData.split('; ')
    valid = True
    
    # Part 1
    # For each set, find the number of each color.
    # If they are over the limit for ANY set, break the loop and move on to the next game.
    # Otherwise, they are correct, so add the ID to the sum.
    for set in sets:
        r = 0
        g = 0
        b = 0

        words = set.split(' ')
        for wordIdx in range(len(words)):
            if words[wordIdx][0] == 'r':
                r += int(words[wordIdx - 1])
            elif words[wordIdx][0] == 'g':
                g += int(words[wordIdx - 1])
            elif words[wordIdx][0] == 'b':
                b += int(words[wordIdx - 1])
    
        if r > 12 or g > 13 or b > 14:
            valid = False
            break
    
    if valid:
        sumColors += int(id)
    
    # Part 2
    rMax = 0
    gMax = 0
    bMax = 0

    # For each set, find the maximum number of each color, by comparing the current max to the number in the set.
    for set in sets:
        words = set.split(' ')
        for wordIdx in range(len(words)):
            if words[wordIdx][0] == 'r':
                rMax = max(rMax, int(words[wordIdx - 1]))
            elif words[wordIdx][0] == 'g':
                gMax = max(gMax, int(words[wordIdx - 1]))
            elif words[wordIdx][0] == 'b':
                bMax = max(bMax, int(words[wordIdx - 1]))
    
    sumPowers += rMax * gMax * bMax

print(sumColors)
print(sumPowers)
# Day 2: Cube Conundrum

# Open data file
with open('02-input.txt', 'r') as file:
    data = file.read().splitlines()

sum = 0

for game in data:
    colonIdx = game.find(':')
    id = game[game.find(' ') + 1:colonIdx]

    gameData = game[colonIdx + 2:]
    sets = gameData.split('; ')
    valid = True
    
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
        sum += int(id)

print(sum)
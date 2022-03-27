


from math import floor

def calcSpace(i, numStars):
    return floor((numStars - i)/2)

def printStarsHelper(i, numStars):
        print(' ' * calcSpace(i, numStars), end='')
        print('*' * i, end='')
        print(' ' * calcSpace(i, numStars))

def printStars(numStars):
    for i in range(1, numStars, 2):
        printStarsHelper(i, numStars)
    for i in range(numStars, 0, -2):
        printStarsHelper(i, numStars)

if __name__ == "__main__":
    printStars(13)


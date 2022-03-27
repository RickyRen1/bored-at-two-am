def printStarsHelper(i, numStars):
    numSpace = (numStars - i)//2
    print(f"{' ' * numSpace}{'*' * i}{' ' * numSpace}")

def printStars(numStars):
    for i in range(1, numStars, 2):
        printStarsHelper(i, numStars)
    for i in range(numStars, 0, -2):
        printStarsHelper(i, numStars)

if __name__ == "__main__":
    printStars(13)

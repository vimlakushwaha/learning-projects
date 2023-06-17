import random
def getSecretNum(NumDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NumDigits):
        secretNum += str(numbers[i])
    return secretNum
NUMDIGITS = 3
MAXGUESS = 10

print("I am thinking of a %s-digit number. Try to giess what it is."%(NUMDIGITS))
print("Here are some clues:")
print("When I say: That means:")
print(' Pico    One digit is orrect but in the wrong position.')
print(' Fremi   One digit is correct and  in the right position')
print(' Bagels  No digit is correct.')

while True:
    secretNum  = getSecretNum(NUMDIGITS)
    print("I have thought up a number. You have %s guesses to get it."%(MAXGUESS))

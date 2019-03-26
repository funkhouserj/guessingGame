import random
def numRange():
    while True:
        try:
            maxNum = int(raw_input("Choose a number range by entering an integer from 100 to 1000: "))
            print("")
        except ValueError:
            print("That's not an int! Try again.")
            continue
        else:
            if 100 <= maxNum <= 1000:
                answer = random.randint(1, maxNum)
                return answer, maxNum
            else:
                print("That value is not in range! Try again.")
                continue

def userInput(n):
    while True:
        try:
            guess = int(raw_input("Enter an integer from 1 to " + str(maxNum) + ": "))
        except ValueError:
            print("That's not an int! Try again.")
            continue
        else:
            return guess

print("")  
print ("Guessing Game")
print("")
answer,maxNum = numRange()
guess = userInput(maxNum);
while answer != "guess":
    print("")
    if guess < answer:
        print ("guess is low")
        guess = userInput(maxNum);
    elif guess > answer:
        print ("guess is high")
        guess = userInput(maxNum);
    else:
        print ("you guessed it!")
        break
    print("")

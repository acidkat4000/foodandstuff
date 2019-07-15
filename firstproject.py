import random

def main():
    randnum = random.randint(1,10)
    tries = random.randint(3,10)
    while(tries>0):
        guess = int(input("guess a number between 1 and 10 "))
        if (guess == randnum):
            print("you win, no wait its a tie!")
        else:
            tries = tries -1
            print("ha ha ha, you LOOSE, you have " + str(tries) + " more tries")
if __name__ == "__main__":
    main()
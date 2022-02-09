import random

def guess(x):
    random_number = random.randint(1,x) #Random number generator between 1 and x
    choice = 0
    while choice != random_number:
        choice = int(input("Pick a number between 1 and " + str(x)))
        if choice > random_number:
            print("Too High");
        elif choice < random_number:
            print("Too Low");
    print("CORRECT - Thanks for playing the secret number game!")

def computer_guess(x): #MYBE IN 5 TRIES????
    print("INSTRUCTIONS: PICK A NUMBER BETWEEN 1-100. THE PROGRAM WILL ASK YOU IF A GIVEN NUMBER IS CORRECT. TYPE c IF CORRECT, l IF TOO LOW AND h IF TOO HIGH. GOOD LUCK!")
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        guess = random.randint(low,high)
        feedback = input("Is " + str(guess) + " correct?").lower()
        if feedback == "l":
            low = guess + 1
        elif feedback == "h":
            high = guess - 1
    print("CORRECT - COMPUTER WINS")


#guess(100) #Call to guess function
computer_guess(100)
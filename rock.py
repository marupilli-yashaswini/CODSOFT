import random

def UserChoice():
    userChoice=input("enter your choice among [rock, paper, scissors]:").lower()
    while userChoice not in ['rock','paper','scissors']:
        userChoice=input("INVALID CHOICE\nPlease enter your choice among [rock, paper, scissors]:")
    return userChoice
def CompChoice():
    return random.choice(['rock','paper','scissors'])
def winner(userChoice,compChoice):
    if (userChoice=='rock' and compChoice=='scissors') or (userChoice=='paper' and compChoice=='rock') or (userChoice=='scissors' and compChoice=='paper'):
        return 'win'
    elif userChoice==compChoice:
        return 'Its a tie!'
    else:
        return 'lose'

userScore=0
compScore=0
while True:
    userChoice=UserChoice()
    compChoice=CompChoice()
    result=winner(userChoice,compChoice)
    if "win" in result:
        userScore+=1
    elif "lose" in result:
        compScore+=1
    print(f"\nresult:{result}\nYou chose: {userChoice}\nComputer Chose: {compChoice}")
    playagain=input("do you want to play again?(yes/no):").lower()
    if playagain!='yes':
        break
print("Thanks for playing!")

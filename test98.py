#code to play rock paper scissors game
import random  
def play_rps():
    user = input("Enter your choice (rock, paper, scissors): ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer}")
    
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"
print("Hello world")
for i in range(1,5):
    print("Goodbye world")
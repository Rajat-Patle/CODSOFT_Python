import random as r
class Game:
    def __init__(self):
        self.user = 0
        self.comp = 0
        self.user_score = 0 
        self.comp_score = 0    
        
    def game(self):
        self.comp = r.randint(0, 2)
        self.user = int(input("Enter Your Move:\n1. Press 0 for Rock\n2. Press 1 for Paper\n3. Press 2 for Scissors\n"))

        if self.user not in [0, 1, 2]:
            print("Invalid Move, please select among Rock[0], Paper[1], and Scissors[2]!!")
            return

        if self.comp == self.user:
            print("Both the User and Compute Moves are Same!, So It's Draw\n")
        elif (self.comp == 0 and self.user == 1) or (self.comp == 1 and self.user == 2) or (self.comp == 2 and self.user == 0):
            print(f"Computer Choice is :{self.comp} and User Choice is:{self.user}! So, Congratulations User Won \n")
            self.user_score += 1
        else:
            print(f"Computer Choice is :{self.comp} and User Choice is:{self.user}! So, User Loss\n ")
            self.comp_score += 1

    def round(self):
        self.play_again = str(input("Do you want to Play Again:-\n1. Yes \n2. No\n")).lower()
        while self.play_again in ['yes', '1']:
            self.game()
            self.play_again = str(input("Do you want to Play Again:-\n1. Yes \n2. No")).lower()
        print(f"Winning Score :- Users Score is :{self.user_score}, Computer Score is :{self.comp_score}\n")
          
G = Game()
G.game()
G.round()
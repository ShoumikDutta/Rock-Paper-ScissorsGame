import random

def main():
    print("Welcome to Rock-Paper-Scissors Game\n")
    print("1.Rock 2.Paper 3.Scissors")
    score=0
    comp_score=0
    while(True):
        comp_choice=random.randint(1,3)
        try:
            user_choice=int(input("Enter Your choice(only 1,2,3):"))
        except:
            print("Invalid Input.Try Again.")
            continue
        if score==3:
            print("Congratulations. You have won the game.")
            break
        if comp_score==3:
            print(" You Lost the game.Better luck next time")
            break
        result=check_winner(comp_choice,user_choice)
        if result==0:
            print("Tie!")
        elif result==1:
            score+=1
            print("You won this round")
        else:
            comp_score+=1
            print("You lost This round")

        
        
        
def check_winner(comp,user):
    if comp==user:
        return 0
    
    if (user==1 and comp==3) or (user==2 and comp==1) or (user==3 and comp==2):
        return 1
    else:
        return -1


if __name__=="__main__":
    main()

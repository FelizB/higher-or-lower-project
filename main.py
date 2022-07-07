from art import logo 
from art import vs
from  game_data import data
from random import randint

score=0
information1={}
information2={}
guessed=randint(0,(len(data)-1))
guessed2=""
def guessed_info(number1,number2):
    global guessed
    global guessed2
    if number1!=number2:
        guessed2=randint(0,(len(data)-1))
        return guessed2
    elif number1==number2:
        guessed=randint(0,(len(data)-1))
        return guessed


def compare(number1,number2):
    if number1>number2:
        return True
    else:
        return False
  



# print(guessed,guessed2)
# print(data[guessed])

not_over=False
while not not_over:
    guessed2=guessed_info(guessed2,guessed)
    print(guessed,guessed2)
    information1=data[guessed]
    information2=data[guessed2]
    
    infoA=[information1["name"],information1["follower_count"],information1["description"],information1["country"]]
    
    infoB=[information2["name"],information2["follower_count"],information2["description"],information2["country"]]
    
    print (logo)
    print(f"Compare A:{infoA[0]},a {infoA[2]}, from {infoA[3]} ")
    print(vs)
    print(f"Compare B:{infoB[0]},a {infoB[2]}, from {infoB[3]} ")
    
    entered=input("Who has many followers. 'A' or 'B': ").lower()
    EnteredA=infoA[1]
    EnteredB=infoB[1]
    if entered=="a":
        
        valued=compare(EnteredA,EnteredB)
        if valued==True:
            
            score+=1
            guessed2=guessed_info(guessed,guessed2)
            # print(guessed2)
            print("Correct.")
            not_over=False
            
        else:
            not_over=True
            print(f"False. Your score is at {score}")
    elif entered=="b":
        valued=compare(EnteredB,EnteredA)
        if valued==True:
            score+=1
            guessed=guessed2
            print("Correct")
            not_over=False
        else:
            not_over=True
            print(f"False. Your score is at {score}")
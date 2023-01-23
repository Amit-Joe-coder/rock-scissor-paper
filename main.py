import random
use=['r','s','p']
print("\t\t\t\t\t\t---WELCOME---")
print("\n\t\t\t\t---Rock+++Scissor+++Paper---")
print("---Enter\n|->r for Rock\n|->s for Scissor\n|->p for Paper")
print("\t\t\t\t\t\t***Rules***")
print("______________________________________________________")
print("1.Their is total three chance.")
print("2.Final winner is calculated on total winning.")
print("______________________________________________________")


noof_chances=3
cpoint=0
ppoint=0

while noof_chances:
  _input=input('\nEnter you choice rock,scissor,paper:')
  _random=random.choice(use)
  if _input==_random:
    print("Draw")
    print(f"Computer choses {_random} and Player choses {_input}")
  #user input rock
  elif _input=="r" and _random=="s":
    print("Player wins")
    print(f"Player choses {_input} and Computer choses {_random}")
    ppoint+=1
  elif _input=="r" and _random=="p":
    print("Computer wins")
    print(f"Player choses {_input} and Computer choses {_random}")
    cpoint+=1

#user input scissor
  elif _input=="s" and _random=="p":
    print("Player wins")
    print(f"Player choses {_input} and Computer choses {_random}")
    ppoint+=1
  elif _input=="s" and _random=="r":
    print("Computer wins")
    print(f"Player choses {_input} and Computer choses {_random}")
    cpoint+=1


    
#user input paper
  elif _input=="p" and _random=="r":
    print("Player wins")
    print(f"Player choses {_input} and Computer choses {_random}")
    ppoint+=1
  elif _input=="p" and _random=="s":
    print("Computer wins")
    print(f"Player choses {_input} and Computer choses {_random}")
    cpoint+=1
  noof_chances-=1
  print(f"\n\t\t----------This is {noof_chances} chance------------")

print("\t\t\t---------Result---------")
if cpoint==ppoint:
  print("====This is Tie both have same points")
elif cpoint>ppoint:
  print(f"===Computer wins by Getting {cpoint} points")
else:
  print(f"===Player wins by Getting {ppoint} points")
print("\n\n\t\t\t<___________END__________>")

import random

option_choosen = int(input("what do u choose \n type\n 0 for Rock ⚫️ \n 1 for paper 📄\n 2 for scissors ✂️ :  "))


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if option_choosen == 0:
  print(rock)
elif option_choosen == 1:
  print(paper)
elif option_choosen == 2:
  print (scissors)
else:
  print("invalid entry")

computer_choice = random.randint(0 , 2)
print("computer chose: \n")
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print (scissors)
else:
  print("ops the Computer is cheater")

if computer_choice == option_choosen :
  print("Drow")
elif option_choosen == 0 and computer_choice == 1:
  print("computer win😂 .. You loss🥺")
elif option_choosen == 1 and computer_choice == 2:
  print("computer win😂 .. You loss🥺")
elif option_choosen == 2 and computer_choice == 0:
  print("computer win😂 .. You loss🥺")

elif option_choosen == 0 and computer_choice == 2:
  print("You win 😍 .. computer loss🥺")
elif option_choosen == 1 and computer_choice == 0:
  print("You win 😍 .. computer loss🥺")
elif option_choosen == 2 and computer_choice == 1:
  print("You win 😍 .. computer loss🥺")

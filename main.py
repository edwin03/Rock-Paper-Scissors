import random

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

options = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, len(options) - 1)

print(f"You chose: {options[choice]}\n")
print(f"Computer chose: {options[computer]}")

if choice == 0 and computer == 2:
    print("You Win!")
elif choice == 1 and computer == 0:
    print("You Win!")
elif choice == 2 and computer == 1:
    print("You Win!")
elif choice == computer:
    print("It's a tie!")
else:
    print("You Lose!")
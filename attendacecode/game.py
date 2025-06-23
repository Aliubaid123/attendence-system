'''Number Guessing Game
The computer randomly picks a number (e.g., 1–100).

The user keeps guessing until they get it right.

Use loops to repeat until the correct number is guessed.
You have to submit it tomorrow and also run it and add screen shot of outputs'''
import random 


any_number=random.randint(1,100)


print("Well come to guessing number game  ❤ :")
print("Guess any number between 1 and 100  🤞 :")

while True:
         
         guess=int(input("Enter the number between 1 and 100 :"))

         if guess< any_number:
                 print("its  low number ! try again")
         elif guess> any_number:
                 print("its high number !  try again")
         else:
           print("congratulation !  you guessed the correct number 👏👏  ")
           break
         
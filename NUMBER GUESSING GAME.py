import random
secret_number = random.randint(1,10)
attempts = 3
print("Welcome to the number guessing game!")
print("Guess a number between 1 and 10. You have", attempts, "attempts.")

while attempts > 0:
     n = int(input("Guess the secret_number:"))
     
     if n < 1 or n > 10:
         print("Please enter a number between 1 and 10.")
         attempts -= 1
         continue
        
     if n == secret_number:
         print("Congratulations!! you guessed the right number")
         break
        
     elif n > secret_number:
         print("Too high! try again")
         
     else:
         print("Too Low! Try again")
     attempts -= 1
     
else:
    print("Bette luck next time! The correct number was:", secret_number)

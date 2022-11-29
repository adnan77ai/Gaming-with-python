user_input = 500000
count = 0
while True:
  guess = int(input("Guess the correct guess that which i picked between 1 to 1,000,000 : "))
  
  if guess < 0 :
    print ("Now we'll never know what the answer is …")
    exit()
  
  elif guess > user_input :
    print ("Too high,try again...")
    
  elif guess < user_input :
    print ("Too low, try agin...")
    
  elif guess == user_input :
    print("Awesome, you are our winner for today 💣!!!")
    break
  
  else:
    print("That is not a guess I recognize.")
  
  count += 1
    
print ("You have guessed the correct guess after", count, "attemp, congratulatuions 🙌!!!")
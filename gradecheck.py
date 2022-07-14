print("Enter your score")
score = input()
intScore = int(score)
if intScore  >= 90:
  print("Your score is an A")
elif intScore >=80 and intScore <=89: 
  print("Your score is a B") 
elif intScore >=70 and intScore <=79:
  print("Your score is a C")
elif intScore >=60 and intScore <=69:  
  print("Your score is a D")
else:
  print("You Failed!")

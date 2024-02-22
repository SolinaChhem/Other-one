#file name quiz-app.py
name = input("what is your name? ")
print("Hello!", name)

total_point = 0
question = input("UI stand for")
if question.lower() == "user interface":
   total_point = total_point + 1
   print("Correct")
else:
    print("Incorrect")


question = input("2+2? ")
if question == "4":
    total_point = total_point + 1
    print('Correct')
else: 
    print('Incorrect')

question = input("2+3? ")
if question == "5":
    total_point = total_point + 1
    print('Correct')
else: 
    print('Incorrect')

question = input("2+4? ")
if question == "6":
    total_point = total_point + 1
    print('Correct')
else: 
    print('Incorrect')

question = input("2+5? ")
if question == "7":
    total_point = total_point + 1
    print('Correct')
else: 
    print('Incorrect')

question = input("2+6? ")
if question == "8":
    total_point = total_point + 1
    print('Correct')
else: 
    print('Incorrect')

question = input("2+7? ")
if question == "9":
    total_point = total_point + 1
    print('Correct')
else: 
    print('Incorrect')

#float number (int) is integer no decimal
#print("RESULT::")
#print(int(total_point/6*100))
print(f"Your total point is: {int(total_point/6*100)}%") 
#for creating words question
#question.lower = "apple":

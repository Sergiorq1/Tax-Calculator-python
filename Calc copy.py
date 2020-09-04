#making sure the person is mmindful about their mood
greeting = input("How's your day?")
print(f"Thanks for letting me know that your day is {greeting}")
#Telling user what this program is
print(f"This is a SF sales tax calculator!")

tip_question = input("are you at a restraunt and are you trying to tip? Type yes or no")
if tip_question == "yes":
    print("how much are you trying to tip? 15-20% pre-tax is typical")
    percent_tip = input("(Example answer: 17)")
elif tip_question == "no":
    print("Got it!")

# I tried to get a functioning else statement to work, but I could'nt, I will ask during office hours
# else:
#     print("please input something valid")

number = input("Enter amount of money spent pre-tax")
input_number = float(number) * (1+((float(percent_tip)/100)))
conversion = float(number) * 1.085 + (input_number - float(number))
conversion_rounded = round(conversion, 3)
tax_alone = round(float(number) * 1.085 - float(number),2)
tips_alone = round(input_number - float(number),2)
print(f"With tax, total is {conversion_rounded} tax alone is {tax_alone} and tips alone is {tips_alone}")


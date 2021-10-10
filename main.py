from replit import clear
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator!")
bill = 0.0
tip = [0.0]
persons = [0]
def bill_amount():
    while True:
        try:
            bill = float(input("What was the total bill? $"))
            return bill
        except:
            print("This isn't a valid number")
            clear()
            
def tip_amount(tip):
    isnotanumber = True
    while isnotanumber:
        try:
            tip_data = int(input("What is the tip you want to give? 10, 12 or 15?: "))
            if tip_data == 10 or tip_data == 12 or tip_data == 15:
                tip[0] = tip_data*0.01 + 1
                isnotanumber = False
            else:
                print("The number has to be 10, 12 or 15.")
        except:
            print("This isn't a number")

def persons_amount(persons):
    isnotanumber = True
    while isnotanumber:
        try:
            persons[0] = int(input("How many persons are dividing the tip?: "))
            isnotanumber = False
        except:
            print("This isn't a valid number")
powerswitch = True
while powerswitch:           
    bill = bill_amount()
    tip_amount(tip)
    persons_amount(persons)            
    math = ((bill / persons[0]) * tip[0])
    print("Each person should pay: $" + ("{:.2f}".format(math)))
    wanttoexit = input("Do you want to exit? type yes to finish the program. ").lower()
    if wanttoexit == "yes":
        powerswitch = False
    else:
      clear()

# def bill_calc(bill,tip,persons):
#   calc = (tip / 100 * bill + bill) / persons
#   final_amount = round(calc, 2)
#   final_amount = "{:.2f}".format(calc)
#   print(f"Each person should pay: ${final_amount}")
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $ "))
# tip = int(input("What percentage tip would you like to give? 10,12 or 15? "))
# persons = int(input("How many people to split the bill? "))
# bill_calc(bill,tip,persons)

Total_bill = float(input("Please enter your total bill amount \n$"))
tip_percent = float(input("What percentage tip would you like to give? \n"))
number_of_people = float(input("How many people to split the bill \n"))
split_bill = float(Total_bill / number_of_people)
total_tip = float(Total_bill * (tip_percent / 100))
split_tip = float(total_tip / number_of_people)
total_pay = split_bill + split_tip
total_pay_round = round(total_pay , 2)
print(f"Each person must pay {total_pay_round}")

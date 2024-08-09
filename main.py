print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? R:"))
tip = int(input("What percentage tip would you like to give? (Please just write the number, it automatically adds the percentage) 10 12 15 or any of your choice "))
people = int(input("How many people to split the bill? "))
tip_as_percentage = tip/100
tip_amount=bill*tip_as_percentage
total_bill=bill+tip_amount
bill_per_person=total_bill/people
print(round(bill_per_person, 2))
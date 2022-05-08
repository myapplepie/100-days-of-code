print("Welcome to the tip calculater!")
bill = float(input("what was the total amount? $"))
tip = float(input("How much would you like to tip? 10, 15, 20 "))
people = int(input("How many people will split the bill? "))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount}")


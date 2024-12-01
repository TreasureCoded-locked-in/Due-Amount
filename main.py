num_people = int(input("How many people are in your group? "))
total_cost = float(input("What was the total cost of the lunch? "))
tip_percent = float(input("What percentage tip would you like to leave? "))
tip_amount = total_cost * tip_percent / 100
total_cost += tip_amount
cost_per_person = total_cost / num_people
#This code divides the total cost by the number of people in the group to get the cost per person.
print(f"The total cost of the lunch is {total_cost:.2f}")
print(f"The tip amount is {tip_amount:.2f}")
print(f"The cost per person is {cost_per_person:.2f}")
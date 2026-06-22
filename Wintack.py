print("===== Daily Water Intake Tracker =====")

goal = int(input("Enter daily water goal (ml): "))

morning = int(input("Morning water intake (ml): "))
afternoon = int(input("Afternoon water intake (ml): "))
evening = int(input("Evening water intake (ml): "))

total = morning + afternoon + evening

percentage = (total / goal) * 100

print(f"\nTotal Water Intake = {total} ml")
print(f"Goal Completion = {round(percentage, 2)}%")

if total >= goal:
    print("Congratulations! Daily goal achieved.")

else:
    remaining = goal - total
    print(f"Goal Remaining = {remaining} ml")
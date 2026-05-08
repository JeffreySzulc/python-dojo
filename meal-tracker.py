# Meal 1

food1 = input("Name the food, Dawg: ")
protein1 = int(input("How much protein does it have?: "))

food2 = input("Name the food, Dawg: ")
protein2 = int(input("How much protein does it have?: "))

food3 = input("Name the food, Dawg: ")
protein3 = int(input("How much protein does it have?: "))

meal1 = f"{food1}, {food2}, and {food3}"
total1 = protein1 + protein2 + protein3

# Meal 2

food4 = input("Name the food, Dawg: ")
protein4 = int(input("How much protein does it have?: "))

food5 = input("Name the food, Dawg: ")
protein5 = int(input("How much protein does it have?: "))

food6 = input("Name the food, Dawg: ")
protein6 = int(input("How much protein does it have?: "))

meal2 = f"{food4}, {food5}, and {food6}"
total2 = protein4 + protein5 + protein6


if(total1 > total2):
    print(f"Meal 1 {meal1} has more protein.")
elif(total2 > total1):  
    print(f"Meal 2 {meal2} has more protein.")
else:
    print("Meal 1 and Meal 2 have the same exact amount of protein, would ya believe it??")
# print(f"Todays meal is: \n{food1}\n{food2}\n{food3}")
# print(f"Total protein = {total}")
# print(meal1)
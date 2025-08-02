# age_difference_calculator.py

print("👫 Age Difference Calculator")

# Input names
boy_name = input("Enter boy's name: ")
girl_name = input("Enter girl's name: ")

# Input ages
boy_age = int(input("Enter boy's age: "))
girl_age = int(input("Enter girl's age: "))

# Calculate age difference
age_difference = abs(boy_age - girl_age)

# Display result
if boy_age > girl_age:
    print(f"{boy_name} is older than {girl_name} by {age_difference} years.")
elif girl_age > boy_age:
    print(f"{girl_name} is older than {boy_name} by {age_difference} years.")
else:
    print(f"{boy_name} and {girl_name} are the same age.")
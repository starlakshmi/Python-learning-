print("Friendship Program 🤝")

boy_name = input("Enter boy's name: ")
girl_name = input("Enter girl's name: ")

boy_age = int(input("Enter boy's age: "))
girl_age = int(input("Enter girl's age: "))

age_difference = abs(boy_age - girl_age)

print("\n--- Friendship Details ---")
print(f"Boy's Name: {boy_name}")
print(f"Girl's Name: {girl_name}")
print(f"{boy_name} is friends with {girl_name}.")
print(f"Age difference is {age_difference} years.")
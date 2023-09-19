# Get the number of pennies from the user
pennies = int(input("Enter the number of pennies: "))

# Calculate the number of dollars
dollars = pennies // 100
pennies %= 100

# Calculate the number of quarters
quarters = pennies // 25
pennies %= 25

# Calculate the number of dimes
dimes = pennies // 10
pennies %= 10

# Calculate the number of nickels
nickels = pennies // 5
pennies %= 5

# The remaining pennies
remaining_pennies = pennies

# Display the results
print(f"Dollars: {dollars}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {remaining_pennies}")
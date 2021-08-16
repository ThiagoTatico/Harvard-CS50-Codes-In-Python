# Calculates the smallest amount of coins for change

from cs50 import get_float
# --------------------------------------

# Prevents the input from being negative or zero
while True:
    dollars = get_float("Change owed: ")
    
    if dollars > 0:
        break
# --------------------------------------

# Covert to int cents
cents = round(dollars * 100)

# Count how many coins were used
coins = 0
# --------------------------------------

# Distribute the coins in the best way
while cents >= 25:
    cents -= 25
    coins += 1

while cents >= 10:
    cents -= 10
    coins += 1

while cents >= 5:
    cents -= 5
    coins += 1

while cents >= 1:
    cents -= 1
    coins += 1
# --------------------------------------

print(f"Total coins: {coins}")
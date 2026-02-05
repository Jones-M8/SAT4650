fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Q1. checking if Kiwi is in the list
if "kiwi" in fruits:
    print("The fruit 'Kiwi' is in the fruits container\n")
else:
    print ("The fruit 'Kiwi' is not in the fruit container.\n")

# Q2. replace "melon" with "watermelon"
i = fruits.index("melon")
fruits[i] = "watermelon"
print(f"New fruit container: {fruits}\n")

# Q3.  insert "blueberry" right after "cherry".
j = fruits.index("cherry")
fruits[j + 1] = ("blueberry")
print(f"Updated container after blueberry additon: {fruits}\n")

# Q4. append "pear". 
fruits.append("pear")
print(f"Updated container after pear additon: {fruits}\n")

# Q5 for secondlist=['Peach', 'papaya'], add it to fruits using the extend method.
secondlist=['Peach', 'papaya']
fruits.extend(secondlist)
print(f"Updated container after addition of second list of fruits: {fruits}")
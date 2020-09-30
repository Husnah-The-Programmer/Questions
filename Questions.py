# Give the user some context.
# All choice in a series of print statements.

print("\n\nQuestion 1.\n")
print("C variable cannot start with _______?\n")
print("A. An alphabet\n")
print("B. A number\n")
print("C. A special symbol other than underscore\n")
print("D. Both (B) and (C)\n")
print("E. Exit\n")
#Ask for user's choice 
selection = input("Choose the correct answer:\n")
# Responds to the user's choice.
if (selection == 'A'):
    print("Incorrect!!\nTry again.")
elif (selection == 'B'):
    print("Incorrect!!\n")
elif (selection == 'c'):
    print("Incorrect!!\n")
    
elif (selection == 'D'):
    print("Correct!\n")             
else:
    print("Wrong Choice, terminating the program.\n")
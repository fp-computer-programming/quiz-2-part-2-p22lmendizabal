# Author: LM (AMDG) 11/17/21

letter = input("Enter letter for the day: ").upper()
meetday = ['A', 'C', 'E']
if letter == meetday[0]:
    print("You have class today because it is {0} day".format(letter))
elif letter == meetday[1]:
    print("You have class today because it is {0} day".format(letter))
elif letter == meetday[2]:
    print("You have class today because it is {0} day".format(letter))
elif letter != meetday:   
    print("{0} Tech and Coding does not meet today".format(letter))
else:
    print("{0} is not a valid day".format(letter))

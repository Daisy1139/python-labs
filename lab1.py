print("Welcome to Hogwarts!")

print("Today is the day you will be sorted into one house; Gryffindor, Slytherin, Ravenclaw and Hufflepuff.")

gryffindor = 0

slytherin = 0

hufflepuff = 0

ravenclaw = 0

q1 = input("Are you brave?")

if q1 == "No" or "no":

    gryffindor + 0

    hufflepuff + 1

q2 = input("Are you creative?")

if q2 == "No" or "no":

    ravenclaw + 0

elif q2 == "Yes" or "yes":

    ravenclaw + 1

q3 = input("Are you kind?")

if q3 == "No" or "no":

    hufflepuff + 0

elif q3 == "Yes" or "yes":

    hufflepuff + 1

q4 = input("Are you competitive?")

if q4 == "No" or "no":

    slytherin + 0

elif q4 == "Yes" or "yes":

    slytherin + 1

if slytherin > gryffindor or hufflepuff or ravenclaw:

    print("Slytherin!")

elif gryffindor > slytherin or hufflepuff or ravenclaw:

    print("Gryffindor!")

elif hufflepuff > slytherin or gryffindor or ravenclaw:

    print("Hufflepuff!")

elif ravenclaw > slytherin or gryffindor or hufflepuff:

    print("Ravenclaw!")

elif slytherin == gryffindor:

    print("Slytherin and Gryffindor!")

elif slytherin == hufflepuff:

    print("Slytherin and Hufflepuff!")

elif slytherin == ravenclaw:

    print("Slytherin and Ravenclaw!")

elif gryffindor == slytherin:

    print("Slytherin and Gryffindor!")

elif gryffindor == hufflepuff:

    print("Gryffindor and Hufflepuff!")

elif gryffindor == ravenclaw:

    print("Gryffindor and Ravenclaw!")

elif ravenclaw == gryffindor:

    print("Gryffindor and Ravenclaw!")

elif hufflepuff == gryffindor:

    print("Hufflepuff and Gryffindor!")

elif hufflepuff == ravenclaw:

    print("Hufflepuff and Ravenclaw!")

elif hufflepuff == slytherin:

    print("Hufflepuff and Slytherin!")

elif ravenclaw == gryffindor:

    print("Ravenclaw and Gryffindor!")

elif ravenclaw == hufflepuff:

    print("Hufflepuff and Ravenclaw!")

elif ravenclaw == slytherin:

    print("Ravenclaw and Slytherin!")






# Sample code:

# gryffindor = ask_question("Are you brave? ")

# ravenclaw = ask_question("Are you creative? ")

# hufflepuff = ask_question("Are you kind? ")

# slytherin = ask_question("Are you competitive? ")
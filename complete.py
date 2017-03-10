import math

#Function to calculate the total costs. 1 parameter: the number of students.
def calculateTotal(numberOfStudents):
    #Variables for different costs, and for the number of students
    costOfCoach = 550
    costPerStudent = 30
    numberOfTickets = int(numberOfStudents)

    #Works out the number of free tickets, then subtracts that from the number of tickets
    freeTickets = int(int(numberOfStudents) / 10)
    print("Free tickets: "+str(freeTickets))
    numberOfTickets -= freeTickets

    #Works out cost per student
    cost = costPerStudent * numberOfTickets
    cost += costOfCoach

    #Works out cost per student
    costPerStudent = math.ceil(cost / int(numberOfStudents))

    #Returns cost per student
    return int(costPerStudent)

#Function to input and add student records
def addNames():
    #Stores the contents of the file used to store student records in variables
    namesStorage = open("listNames.txt", "r+")
    names = namesStorage.readlines()
    namesStorage.close()

    paidStorage = open("listPaid.txt", "r+")
    paid = paidStorage.readlines()
    paidStorage.close()

    runNames = True
    while runNames == True:
        runContinue = True
        #Checks the maximum number of students has not been reached
        if len(names) > 44 or len(paid) > 44:
            print("Maximum number of students reached.")
            #Ends the While loop
            runNames = False
        else:
            runNames = True
            #Input for the name of the student
            nameInput = input("Please enter a name: ")
            #Adds name of the student to the list
            names.append(nameInput)
            while runContinue == True:
                #Input for whether that student has paid or not
                paidInput = input("Have they paid? (y or n) ")
                #Checks that the input is valid
                if str.lower(paidInput) == "y":
                    #Adds the input to the list
                    paid.append("True")
                    #Ends the While loop
                    runContinue = False
                elif str.lower(paidInput) == "n":
                    #Adds the input to the list
                    paid.append("False")
                    #Ends the While loop
                    runContinue = False
                else:
                    print("Answer not valid.")
                    runContinue = True
            #Input for whether or not to add another student
            continueVar = input("Add another name? (y or n) ")
            if str.lower(continueVar) == "n":
                #Ends the While loop
                runNames = False
            else:
                print("")

    #Variables for the files to store the student records
    namesStorage = open("listNames.txt", "r+")
    paidStorage = open("listPaid.txt", "r+")
    #Variable for length of list
    list_length = len(paid)
    i = 0
    #Writes to lists to the files
    for i in range(list_length):
        namesStorage.write(names[i].rstrip())
        namesStorage.write("\n")
        paidStorage.write(paid[i].rstrip())
        paidStorage.write("\n")
    namesStorage.close()
    paidStorage.close()

#Function to delete student records
def deleteNames():
    run = True

    #Stores the contents of the file used to store student records in variables
    namesStorage = open("listNames.txt", "r+")
    names = namesStorage.readlines()
    namesStorage.close()

    paidStorage = open("listPaid.txt", "r+")
    paid = paidStorage.readlines()
    paidStorage.close()

    while run == True:
        #Input for the position of the record to delete
        indexToDelete = input("What position is the student you want to remove from the list at? ")
        #Checks the input is a number
        if indexToDelete.isdigit():
            #Checks the number is valid
            if int(indexToDelete) >= 0 and int(indexToDelete) <= len(names) - 1:
                print("Number accepted.")
                #Deletes the item at that position from both lists
                del names[int(indexToDelete)]
                del paid[int(indexToDelete)]

                #Ends the While loop
                run = False
            else:
                print("Not a valid input")
                run = True
        else:
            print("Not a valid input")
            run = True


    #Variables for the files to store the student records
    namesStorage = open("listNames.txt", "w")
    paidStorage = open("listPaid.txt", "w")
    #Variable for length of list
    list_length = len(paid)
    i = 0
    #Writes to lists to the file
    for i in range(list_length):
        namesStorage.write(names[i])
        paidStorage.write(paid[i])
    namesStorage.close()
    paidStorage.close()

#Function to output student records
def printNames():
    #Stores the contents of the file used to store student records in variables
    namesStorage = open("listNames.txt", "r+")
    names = namesStorage.readlines()
    namesStorage.close()

    paidStorage = open("listPaid.txt", "r+")
    paid = paidStorage.readlines()
    paidStorage.close()

    #Outputs each line of both lists
    i = 0
    for i in range(0, len(names)):
        print(str(i)+"\n"+names[i]+str(paid[i]))

#Outputs each line of both lists
def calculateCosts():
    #Stores the contents of the file used to store student records in variables
    paidStorage = open("listPaid.txt", "r+")
    paid = paidStorage.readlines()
    numberOfStudents = len(paid)
    paidStorage.close()

    #Variable for the number of students who have payed, from the checkPayed function
    numPayed = checkPayed()

    #Outputs the number of students who have payed
    print(str(numPayed)+" out of "+(str(len(paid)))+" people have paid.")

    #Variables for the total that has been collected, and the costs that need to be payed
    total = int(calculateTotal(len(paid)))
    costs = int(calculateTotal(numPayed))

    #Outputs the amount collected
    print("So far you have collected £"+(str(numPayed*total))+" in total.")

    #Works out and assigns to a variable whether they have broken even, made a profit or a loss.
    message = ""
    if costs - total < 0:
        message = "make a profit."
    elif costs - total == 0:
        message = "break even."
    elif costs - total > 0:
        message = "make a loss."
    else:
        message = "[ERROR]"

    #Outputs different costs
    print("Each child should pay £"+(str(total))+"; as only "+(str(numPayed))+" have paid, if you charge this you will "+str(message))

    #Assigns the final message to a variable
    if message == "make a profit.":
        message = ("This means you will have £"+str(total-costs)+" left over. Congratulations!")
    elif message == "break even.":
        message = ("This means you're charging exactly the right amount. Well done!")
    elif message == "make a loss.":
        message = ("This means you should consider raising the price so you don't make a loss. To break even, you will need to charge £"+str(calculateTotal(numPayed))+" per student instead. Good luck!")
    else:
        message = "[ERROR]"

    #Returns that message
    return message

#Function to check how many students have payed
def checkPayed():
    #Variable to store the contents of the file listing who has payed
    paidStorage = open("listPaid.txt", "r+")
    paid = paidStorage.readlines()

    numPayed = 0

    #Reads through the list and adds 1 to a variable counting the number of students who have payed each time a student is marked True
    for i in range (len(paid)):
        if paid[i] == "True" or paid[i] == "\nTrue" or paid[i] == "True\n":
            numPayed += 1
        else:
            continue

    paidStorage.close()

    #Returns the number of students who have payed
    return int(numPayed)

run = True

while run == True:
    #Input for what the user would like to do
    userInput = input("What would you like to do? (C)alculate values, (V)erify how many have payed and view costs, (I)nput student values, (D)elete student values, or (P)rint them? ")
    if str(userInput) == "c" or str(userInput) == "C":
        y = True
        while y == True:
            #Input for the number of students
            numberOfStudents = input("Please enter the number of students taking part: ")
            #Checks if input is a number
            if numberOfStudents.isdigit():
                #Checks if input is in the correct range.
                if int(numberOfStudents) < 1 or int(numberOfStudents) > 45:
                    y = True
                    print("That's not a valid number, please try again.")
                else:
                    y = False
                    print("Number accepted. There are "+str(numberOfStudents)+" students.")
            else:
                y = True
                print("That's not a valid number, please try again.")
        #Outputs the cost per student
        print("Cost per student: "+(str(calculateTotal(numberOfStudents))))
    elif str(userInput) == "v" or str(userInput) == "V":
        print(calculateCosts())
    elif str(userInput) == "i" or str(userInput) == "I":
        addNames()
    elif str(userInput) == "d" or str(userInput) == "D":
        deleteNames()
    elif str(userInput) == "p" or userInput == "P":
        printNames()
    else:
        print("Not a valid input.")
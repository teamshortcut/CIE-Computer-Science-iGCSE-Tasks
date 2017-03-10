#Stores the contents of the file used to store student records in variables
namesStorage = open("listNames.txt", "r+")
names = namesStorage.readlines()
namesStorage.close()

paidStorage = open("listPaid.txt", "r+")
paid = paidStorage.readlines()
paidStorage.close()

#Function to input and add student records
def addNames():
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
        print(names[i]+str(paid[i]))

run = True

while run == True:
    #Input for what the user would like to do
    userInput = input("What would you like to do? (I)nput values, or (P)rint them? ")
    if str(userInput) == "i" or str(userInput) == "I":
        addNames()
    elif str(userInput) == "p" or userInput == "P":
        printNames()
    else:
        print("Not a valid input.")
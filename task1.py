import math

#Function to calculate the total costs. 1 parameter: the number of students.
def calculateTotal(numberOfStudents):
    #Variables for different costs, and for the number of students
    costOfCoach = 550
    costPerStudent = 30
    numberOfTickets = int(numberOfStudents)

    #Works out the number of free tickets, outputs it, then subtracts that from the number of tickets
    freeTickets = int(int(numberOfStudents) / 10)
    print("Free tickets: "+str(freeTickets))
    numberOfTickets -= freeTickets

    #Works out cost from the number of tickets, then adds the cost of the coach
    cost = costPerStudent * numberOfTickets
    cost += costOfCoach

    #Works out cost per student
    costPerStudent = math.ceil(cost / int(numberOfStudents))

    #Returns cost per student
    return costPerStudent

#Function to allow the user to input the number of students
def enterNumStudents():
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
    #Variable storing the total cost
    total = calculateTotal(numberOfStudents)
    #Returns total cost
    return total

#Outputs total cost
print("Cost per student: £"+str(enterNumStudents()))
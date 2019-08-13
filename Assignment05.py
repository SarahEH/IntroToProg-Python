#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Sarah Hogan, 8-11-2019, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
#declare variables (all as empty/blank values) & constants for the PRIORITY code
objFileName = "C:\_PythonClass\Assignment05\Todo.txt" #explicit file path used to benefit Command Prompt, implied file path worked just fine for PyCharm
strMenu = ""
dicRow = {}
lstTable = []
newtask = ""
PRIORITY = ["high", "medium", "low"]
key = ""
value = ""

#-- Processing --#
#Step 1: Load data from text file to python dictoinary.
objFile = open(objFileName,"r") #file opened as read-only
for line in objFile:
    lstTable.append(line.strip()) #strip 'dead' characters & add to the table
    key, value = line.strip().split(',') #split table values as keys & values
    dicRow[key] = value #define dictionary as {"key":"value"} for each table entry
objFile.close() #file closed
#print(dicRow) #used to validate successful import (when editing)
#print(lstTable) #used to validate successful import (when editing)

#-- Input/Output --#
#Step 2:  Display a Menu of choices to the user
while(True):
    print(
    """
TO DO LIST MENU: 
1) Show current data
2) Add a new item.
3) Remove an existing item.
4) Save Data to File
5) Exit Program
    """
    )
    strMenu = input("\nPlease select a menu action: ")

    #Step 3: Show Current data
    if (strMenu.strip() == '1'):
        print("\nCURRENT TO DO LIST: ")
        #using the .get(i) command, cycle through the list & print out the groupings of tasks based on priority
        print("\nHIGH PRIORITY:")
        for i in dicRow:
            if dicRow.get(i) == 'high':
                print("\t"+i)

        print("\nMEDIUM PRIORITY:")
        for i in dicRow:
            if dicRow.get(i) == 'medium':
                print("\t"+i)

        print("\nLOW PRIORITY:")
        for i in dicRow:
            if dicRow.get(i) == 'low':
                print("\t"+i)

        print("\n")

    #Step 4: Add new item to list/Table
    elif (strMenu.strip() == '2'):
        newtask = input("What is the new task? ").title()
        #looks to see if the newtask item already exists, if no assign a priority (while loop used to enforce "high", "medium", "low" selection
        if newtask not in dicRow:
            newpriority="" #initializes a 'blank' priority every new if statement execution
            while newpriority not in PRIORITY:
                newpriority = input("What is the priority? (high/medium/low) ").lower()
            dicRow[newtask] = newpriority #assigns data to dictionary
            print("\n"+newtask, "has been added!")
        else:
            print("\nThat task already exists!")

    #Step 5: Remove an item from the list/Table
    elif (strMenu.strip() == '3'):
        #displays current list for ease of selection
        for row in dicRow:
            print(row)
        removeitem = input("\nWhich task would you like to remove? ").title()
        #looks to see if the removeitem exists, if not return an error message
        if removeitem in dicRow:
            del dicRow[removeitem]
            print("\n"+removeitem, "has been deleted!")
        else:
            print(removeitem,"isn't in the list.")

    #Step 6: Save tasks to the file
    elif (strMenu.strip() == '4'):
        objFile = open(objFileName,"w") #opens file as write (to overwrite any existing data)
        for key, value in dicRow.items():
            lines = [key+","+value,"\n"] #formats each line in a better looking format
            objFile.writelines(lines) #writes each line
        objFile.close() #closes the file we were writing to
        print("To-Do list was written to the file!")

    #Step 7: Exit
    elif(strMenu.strip() == '5'):
        exit()



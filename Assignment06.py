#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Sarah Hogan, 8-11-2019, Added code to complete assignment 5
#   Sarah Hogan, 8-18-2019, Refactored code for functions & class for assignment 6
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
#declare variables (all as empty/blank values) & constants for the PRIORITY code
objFileName = "C:\_PythonClass\Assignment06\Todo.txt" #explicit file path used to benefit Command Prompt, implied file path worked just fine for PyCharm
strMenu = ""
dicRow = {}
lstTable = []
newtask = ""
PRIORITY = ["high", "medium", "low"]
key = ""
value = ""

#-- Processing --#
class todoactions (object):
    @staticmethod

    #Step 1: Load data from text file to python dictoinary.
    def openandread ():
        '''initial step to read in existing data'''
        objFile = open(objFileName,"r") #file opened as read-only
        for line in objFile:
            lstTable.append(line.strip()) #strip 'dead' characters & add to the list
            key, value = line.strip().split(',') #split table values as keys & values
            dicRow[key] = value #define dictionary as {"key":"value"} for each table entry
        objFile.close() #file closed

    def menu ():
        '''Menu for user to select an action from'''
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
        strMenu = input("\nPlease select a menu action: ").strip()
        return strMenu

    def showcurrentdata (dicRow):
        '''Menu option 1 to display current data'''
        print("\nCURRENT TO DO LIST: ")
        # using the .get(i) command, cycle through the list & print out the groupings of tasks based on priority
        print("\nHIGH PRIORITY:")
        for i in dicRow:
            if dicRow.get(i) == 'high':
                print("\t" + i)
        print("MEDIUM PRIORITY:")
        for i in dicRow:
            if dicRow.get(i) == 'medium':
                print("\t" + i)
        print("LOW PRIORITY:")
        for i in dicRow:
            if dicRow.get(i) == 'low':
                print("\t" + i)
        print("")

    def addnewitem (dicRow):
        '''Menu option 2 to add a new item'''
        newtask = input("What is the new task? ").title()
        # looks to see if the newtask item already exists, if no assign a priority (while loop used to enforce "high", "medium", "low" selection
        if newtask not in dicRow:
            newpriority = ""  # initializes a 'blank' priority every new if statement execution
            while newpriority not in PRIORITY:
                newpriority = input("What is the priority? (high/medium/low) ").lower()
            dicRow[newtask] = newpriority  # assigns data to dictionary
            print("\n" + newtask, "has been added!")
        else:
            print("\nThat task already exists!")

    def removeitem (dicRow):
        '''Menu option 3 to remove an item'''
        todoactions.showcurrentdata(dicRow)
        removeitem = input("\nWhich task would you like to remove? ").title()
        # looks to see if the removeitem exists, if not return an error message
        if removeitem in dicRow:
            del dicRow[removeitem]
            print("\n" + removeitem, "has been deleted!")
        else:
            print(removeitem,"isn't in the list.")

    def writeandclose (dicRow):
        '''Menu option 4 to write data to file'''
        objFile = open(objFileName, "w")  # opens file as write (to overwrite any existing data)
        for key, value in dicRow.items():
            lines = [key + "," + value, "\n"]  # formats each line in a better looking format
            objFile.writelines(lines)  # writes each line
        objFile.close()  # closes the file we were writing to
        print("To-Do list was written to the file!")

#From here down, we are outside of the class!
def main (dicRow):
    '''Main script to open file, interact with user'''
    todoactions.openandread()
    # Step 2:  Display a Menu of choices to the user
    while (True):
        selection = todoactions.menu()
        # Step 3: Show Current data
        if (selection == '1'):
            todoactions.showcurrentdata(dicRow)
        # Step 4: Add new item to list/Table
        elif (selection == '2'):
            todoactions.addnewitem(dicRow)
        # Step 5: Remove an item from the list/Table
        elif (selection == '3'):
            todoactions.removeitem(dicRow)
        # Step 6: Save tasks to the file
        elif (selection == '4'):
            todoactions.writeandclose(dicRow)
        # Step 7: Exit
        elif (selection == '5'):
            exit()

#-- Input/Output --#
main(dicRow)
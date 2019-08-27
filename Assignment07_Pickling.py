#-------------------------------------------------#
# Title: Working with Pickling
# Dev:   Sarah Hogan
# Date:  August 26, 2019
# ChangeLog: (Who, When, What)
#   SHogan, 8/26/2019, Created file
#-------------------------------------------------#

#Data
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
animals = {"sheep": "lamb", "cow": "calf", "horse": "pony", "dog": "puppy"}
f = "Pickle.dat"
import pickle #import pickle module to enable pickling

#Processing
def writefile(f, colors, animals):
    objFile = open(f, 'wb') #write method can either open an existing file
                            # or will open one if it does not exist
    print("The file was opened or created using the write method.")
    pickle.dump(colors, objFile)
    pickle.dump(animals, objFile)
    print("The data was successfully written to the file.\n")
    objFile.close()

def readfile(f):
    objFile = open(f, "rb+") #write method can only open an existing file
    print("The file opened with read method.")
    colors = pickle.load(objFile)
    animals = pickle.load(objFile)
    print(colors)
    print(animals)
    objFile.close()

#I/O
writefile(f, colors, animals)
readfile(f)


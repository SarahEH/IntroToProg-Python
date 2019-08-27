#-------------------------------------------------#
# Title: Working with Try/Except Blocks
# Dev:   Sarah Hogan
# Date:  August 26, 2019
# ChangeLog: (Who, When, What)
#   SHogan, 8/26/2019, Created file
#-------------------------------------------------#

#Data
f = "Exception.txt"

#Processing
def readfile (f):
    objFile = open(f, "r") #read method can only open an existing file
    print("The file opened using the read method!")
    objFile.close() #closes file

def writefile (f):
    objFile = open(f, "w") #write method can either open an existing file
                            # or will open one if it does not exist
    print("The file opened or created using the write method!")
    objFile.close() #closes fle

def tryread (f): #attempts the readfile function, will throw exception if error occurs
    try:
        readfile(f)
    except FileNotFoundError as e:
        print("Python encountered this file error: " + str(e))
    except:
        print("Python encountered an unknown error.")

def trywrite(f): #attempts the writefile function, will throw exception if error occurs
    try:
        writefile(f)
    except FileNotFoundError as e:
        print("Python encountered this file error: " + str(e) + "\n")
    except:
        print("Python encountered an unknown error.")

def mainloop (f):
    i = 0
    while i < 2:
        print("Attempt #", i+1, ":")
        tryread(f) #first time through, expect read to fail, since no file exists
        trywrite(f) #fist time thorugh, expect write to create file, since no file exists
        print("\n")
        i += 1

#I/O
mainloop(f)
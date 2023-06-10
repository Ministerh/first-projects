#using absolute directory to locate and open my file
#with open("/Users/MINISTER/Documents/100DAYSPYTHON CHALLENGE/Day24/mine.txt") as file:
#using relative file path to locate and open the file
#with open("./Day24/mine.txt") as file:
    #the file can be opened to read, write or add 
    #when opening a file that dioes niot exist in write mode, it automatically creates  the file
    #file.read()
#using absolute path to locate and open
#with open("/Users/MINISTER/Desktop/test.txt") as test:
#using relative path to open
with open("../../Desktop/test.txt") as test:
    content = test.read()
    print(content)
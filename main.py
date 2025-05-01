#create new file
new_file = open('newfile.txt', 'x')
new_file.close()

#check if a file exists
import os
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("The file does not exist")

    #create a new if it doesn't

my_file = open("newfile.txt", "w")
my_file.write("Yo. I'm Zeina and I am 14, but just pretend I'm fifteen because my birthday is in two months.")
my_file.close()

#delete file named codingal
os.remove("file.txt")

#delete the folder
os.rmdir('Folder')


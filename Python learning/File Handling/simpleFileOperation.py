f = open("test.txt",'w')
f.write("hey this is my first file. ")
f.close()

f = open("test.txt",'a')
f.write("hey i'm vicky kumar. I'm fine and how are you? ")
f.close()


f= open("test.txt",'r')
data = f.read()
print(data)
f.seek(0)
data = f.read()
print(data)
f.close()


import os
print("the size of the file is",os.path.getsize("test.txt"))
# os.remove("test.txt")

# os.rename("test.txt","newTxt.txt")

import shutil
shutil.copy("test.txt","copy_test.txt")

with open("copy_test.txt","r") as f:
    print(f.read())
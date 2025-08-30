#creating new file in write mode
fw = open("test_file.txt","w")
fw.write("This is my second file\n")
fw.write("My name is Divit\n")
fw.close()

#opening file in read mode and printing the content
fr = open("test_file.txt")
file_content = fr.read()
print(file_content)
fr.close()

#reading the file line by line
#must use this method for large files
frl = open("test_file.txt")
for line in frl:
    print(line,end = "")
frl.close
#iterating using readLine

frl1 = open("test_file.txt")
print(frl1.readlines(),end="")
print(frl1.readline())
frl1.close()


#opening file using with
with open("test_file.txt") as f:
    for line in range(5):  
        print(f.readline())



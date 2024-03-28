#  file reading with python


f = open("DP/DP/lis/notes.txt", "r")
# print(f.read(), "here")
f.close()

f = open("DP/DP/lis/notes.txt", "r")
for line in f.readlines():
    # print(line)
    pass
f.close()

# writing to a file


f = open("DP/DP/lis/notes.txt", "w")
f.write("hi")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
f.writelines(L)
f.close()


# seek(n) takes the file handle to the nth
# byte from the beginning. 

f = open("DP/DP/lis/notes.txt", "w+")
f.seek(0)

print(f.read(9))
print()
 
# f.seek(0)
 
# print(f.readline(9))
f.close()
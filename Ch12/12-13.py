f = open("i_have_a_dream.txt", "r")
contents = f.read()
print(contents)
f.close()


#Solution
with open("i_have_a_dream.txt","r") as my_file:
    contents = my_file.read()
    print(contents)

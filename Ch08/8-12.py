alist = ["a", "b", "c"]
blist = ["1", "2", "3"]
abcd= [ ]

for a, b in enumerate(zip(alist, blist)):
    try:
        abcd.append(b[a])
    except IndexError:
        abcd.append("error")
        
print(abcd)

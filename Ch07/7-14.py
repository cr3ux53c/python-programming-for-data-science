Mydict = {'1' : 1, '2' : 2}
Copy = Mydict
Mydict['1'] = 5
result= Mydict['1'] + Copy['1']
print(result)

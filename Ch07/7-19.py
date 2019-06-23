data_1 = {'one' : (1,2,3,4,5,6), 'two' : [1,2,3,4,5,6], 'three' : {'four' : 4, 'five' : 5}}

for k in ['one','two','three']:
    try:
        print(data_1[k][:1])
    except TypeError:
        print("error")

for k in ['one', 'two','three']:
    try:
        data_1[k][-1] = "a"
        print(data_1[k][-1])
    except TypeError :
        print("error")

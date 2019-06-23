line_counter = 0
data_header = [ ]
techusa_list = [ ]

with open ('techusa.csv') as techusa:
    while 1:
        data = techusa.readline()

        if not data:
            break
            if line_counter==0:
                data_header = data.split(",")
        else:
            techusa_list.append(data.split(","))
        line_counter += 1

print (techusa_list[1][0])

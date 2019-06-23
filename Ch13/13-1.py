import csv
# my_first.csv 파일은 이미 작업 디렉터리에 있다고 가정
# tsv로 변환되는 파일명은 transfer.tsv

read_file = open('./my_first.csv', 'r')
reader = csv.reader(read_file, delimiter=",")
with open("transfer.tsv", 'w') as writer_file:
    writer = csv.writer(writer_file, delimiter= "\t")
    for row in reader:
        writer.writerow(row)

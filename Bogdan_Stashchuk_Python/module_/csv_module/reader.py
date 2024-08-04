import csv
with open("test.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter='-')
    print(reader)
    print(type(reader))
    csv_list = list(reader)
    print()
    print(csv_list)
    print(type(csv_list))
    csv_list.pop()
    print()
    print(csv_list)
    name_column = csv_list[0]
    print("Name columns are: ", name_column)
    print()
    for i in range(3):
        print(f"Name {i} column is: {name_column[i]}")
    print(reader.line_num)
    # for line in csv.reader(csv_file):#we can  only ONE do iteration by object reader
    #     print(line)
    #     print("Go")

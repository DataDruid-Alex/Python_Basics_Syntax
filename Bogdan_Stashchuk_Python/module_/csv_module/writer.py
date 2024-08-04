import csv
with open("test.csv", 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter="-")
    writer.writerow(['user_id', 'user_name', 'comments_qnt'])
    writer.writerow(["342", "Ivan", "34"])
    writer.writerow(["3903", "Oleksanr", "2"])
    writer.writerow(["1042", "Brut", "3004"])

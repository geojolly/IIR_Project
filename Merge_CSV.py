import csv

in_1_name = "us.csv"
in_2_name = "city_zones.csv"
out_name = "US_Time.csv"

with open(in_1_name) as in_1, open(in_2_name) as in_2, open(out_name, 'w') as out:
    reader1 = csv.reader(in_1, delimiter=";")
    reader2 = csv.reader(in_2, delimiter=";")
    writer = csv.writer(out, delimiter=";")
    for row1, row2 in zip(reader1, reader2):
        if row1[0] and row2[0]:
            writer.writerow([row1[0], row2[0]])
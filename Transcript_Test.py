import csv

# Open the CSV file for reading
with open('major_crimes_smaller.csv', newline='', encoding='utf-8') as csv_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)

    # Read the header row
    header = next(csv_reader)
    dic = {}
    for row in csv_reader:
        longe = row[4]
        lat = row[5]
        long_lat = (longe, lat)
        sub_dict = {}
        sub_dict[header[0]] = row[0]
        # sub_dict[header[1]] = row[1]
        sub_dict[header[2]] = row[2]
        sub_dict[header[3]] = row[3]
        dic[long_lat] = sub_dict
    print(dic)

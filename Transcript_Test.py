import csv

# Open the CSV file for reading
with open('major_crimes_smaller.csv', newline='', encoding='utf-8') as csv_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)

    # Read the header row
    header = next(csv_reader)
    print(header)
    # Initialize a list to store dictionaries
    data_list = []

    # Iterate through the rows and create dictionaries
    for row in csv_reader:
        print(row)

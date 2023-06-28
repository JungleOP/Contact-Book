from tabulate import tabulate
import csv

def display_contact_file(file_name):
    file_path = file_name + ".csv"
    with open(file_path, "r") as csvfile:
        options = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            options.append(
                {"Contact ID": row["Contact ID"], "First name": row["First name"], "Last name": row["Last name"],
                 "Number": row["Number"]})
        print(tabulate(options, headers="keys", tablefmt="grid"))
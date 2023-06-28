from tabulate import tabulate
import csv
import os


def search_contact(file_name):
    file_path = file_name + ".csv"
    if not file_path.endswith(".csv"):
        file_path += ".csv"

    if not os.path.exists(file_path):
        print("Contact file not found.")
        return

    key = input("Enter the first name of the contact you want to search for: ")
    with open(file_path, "r", newline="") as csvfile:
        options = []
        reader = csv.DictReader(csvfile)

        for row in reader:
            options.append(
                {
                    "Contact ID": row["Contact ID"],
                    "First name": row["First name"],
                    "Last name": row["Last name"],
                    "Number": row["Number"]
                }
            )
    contact_to_retrieve = [contact for contact in options if contact["First name"] == key]

    if contact_to_retrieve:
        print("Contact found:")
        print(tabulate(contact_to_retrieve, headers="keys"))
    else:
        print("No matching contacts found.")

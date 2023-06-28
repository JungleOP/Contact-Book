import os
from tabulate import tabulate
import csv
import inflect

p = inflect.engine()

def create_contact_file(file_name):
    file_path = file_name + ".csv"
    if not file_path.endswith(".csv"):
        file_path += ".csv"

    if os.path.exists(file_path):
        print("Contact file already exists.")
        return

    with open(file_path, "w", newline="") as csvfile:
        fieldnames = ["Contact ID", "First name", "Last name", "Number"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        counter = int(input("Enter the number of contacts you want to add: "))
        contact_id = 1

        for i in range(counter):
            while True:
                fname = input("Enter the first name: ").title()
                if not fname.isalpha():
                    print("Invalid input. Please enter a valid first name.")
                else:
                    break

            while True:
                lname = input("Enter the last name: ").title()
                if not lname.isalpha():
                    print("Invalid input. Please enter a valid last name.")
                else:
                    break

            while True:
                num = input("Enter the phone number (10 digits): ")
                if not num.isdigit() or len(num) != 10:
                    print("Invalid input. Please enter a 10-digit phone number.")
                else:
                    break

            task_data = {
                "Contact ID": contact_id,
                "First name": fname,
                "Last name": lname,
                "Number": num
            }

            writer.writerow(task_data)
            contact_id += 1

    if contact_id == 2:
        contact_word = p.a("contact")
        message = "Here is the {} you added:".format(contact_word)
    else:
        contact_word = "contacts"
        message = "Here are the {} you added:".format(contact_word)

    print(message)
    with open(file_path, "r") as csvfile:
        options = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            options.append(
                {"Contact ID": row["Contact ID"], "First name": row["First name"], "Last name": row["Last name"],
                 "Number": row["Number"]})
        print(tabulate(options, headers="keys", tablefmt="grid"))

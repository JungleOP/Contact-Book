from tabulate import tabulate
import csv
import os

def edit_contact_file(file_name):
    file_path = file_name + ".csv"
    if not file_path.endswith(".csv"):
        file_path += ".csv"

    if not os.path.exists(file_path):
        print("Contact file not found.")
        return

    options = input("Press [1] to delete a contact, [2] to modify a contact's data: ")
    if options == "1":
        try:
            with open(file_path, "r") as csvfile:
                print("Here are the contacts you have. Enter the contact ID you want to delete: ")
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
                print(tabulate(options, headers="keys", tablefmt="grid"))
                ID = int(input("Enter the ID of the contact you want to delete: "))
                if 1 <= ID <= len(options):
                    deleted_contact = options.pop(ID - 1)
                    print("Contact deleted successfully:", deleted_contact["First name"])
                    with open(file_path, "w", newline="") as csvfile:
                        fieldnames = ["Contact ID", "First name", "Last name", "Number"]
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(options)
                    print("Contacts file updated.")
                else:
                    print("Invalid Contact ID")
        except FileNotFoundError:
            print("File not found: " + file_path)
        except PermissionError:
            print("Permission denied: " + file_path)
        except IOError:
            print("An error occurred while opening the file: " + file_path)
    elif options == "2":
        try:
            with open(file_path, "r") as csvfile:
                print("Here are the contacts you have. Enter the contact ID you want to modify:")
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
                print(tabulate(options, headers="keys", tablefmt="grid"))
                ID = int(input("Enter the ID of the contact you want to modify: "))
                if 1 <= ID <= len(options):
                    contacts_to_keep = [contact for contact in options if contact["Contact ID"] != str(ID)]
                    with open(file_path, "w", newline="") as csvfile:
                        fieldnames = ["Contact ID", "First name", "Last name", "Number"]
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(contacts_to_keep)
                    with open(file_path, "a", newline="") as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        while True:
                            fname = input("Enter the first name: ")
                            if not fname.isalpha():
                                print("Invalid input. Please enter a valid first name.")
                            else:
                                break

                        while True:
                            lname = input("Enter the last name: ")
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
                            "Contact ID": ID,
                            "First name": fname,
                            "Last name": lname,
                            "Number": num
                        }
                        writer.writerow(task_data)
                else:
                    print("Invalid contact ID.")
        except FileNotFoundError:
            print("Invalid file name.")

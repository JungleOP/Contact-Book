import sys
from create_file import create_contact_file
from edit_file import edit_contact_file
from display_file import display_contact_file
from search_file import search_contact

def main():
    while True:
        try:
            options = input("Enter [1] to add a new contact, [2] to search a contact, [3] to display the contacts, [4] to edit a contact, or Ctrl+D to exit: ")
            print("(Press Ctrl+D to exit)")
            if options == "1":
                file_name = input("Please provide the file name: ")
                if file_name:
                    create_contact_file(file_name)
                else:
                    print("Invalid file name.")
            elif options == "2":
                file_name = input("Please provide the file name to search: ")
                if file_name:
                    search_contact(file_name)
                else:
                    print("Invalid file name.")
            elif options == "3":
                file_name = input("Please provide the file name to display: ")
                if file_name:
                    display_contact_file(file_name)
                else:
                    print("Invalid file name.")
            elif options == "4":
                file_name = input("Please provide the file name to edit contact: ")
                if file_name:
                    edit_contact_file(file_name)
                else:
                    print("Invalid file name.")
            else:
                print("Invalid option")
        except EOFError:
            sys.exit("Have a good day!")

if __name__ == '__main__':
    main()

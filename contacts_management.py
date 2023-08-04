import os

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    name, phone_number, email, address = map(str.strip, line.split(','))
                    contact = Contact(name, phone_number, email, address)
                    self.contacts.append(contact)
        else:
            print("File does not exist.")

    def save_contacts(self):
        new_contact = self.contacts[-1]  # Get the last contact (the newly added one)
        with open(self.filename, "a") as file:
            file.write(f"{new_contact.name},{new_contact.phone_number},{new_contact.email},{new_contact.address}\n")
        # with open(self.filename, "a") as file:
        #     for contact in self.contacts:
        #         file.write(f"{contact.name},{contact.phone_number},{contact.email},{contact.address}\n")

    def add_contact(self, contact):
        if contact not in self.contacts:
            self.contacts.append(contact)
            self.save_contacts()

    def view_all_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone Number: {contact.phone_number}")
            print(f"Email: {contact.email}")
            print(f"Address: {contact.address}")
            print("=" * 20)

    def search_contact(self, search):
        results = []
        for contact in self.contacts:
            if (search.lower() in contact.name.lower()) or (search in contact.phone_number):
                results.append(contact)
        return results

    def delete_contact(self, name):
        contact_to_delete = None
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact_to_delete = contact
                break
        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            temp_filename = self.filename + ".tmp"
            with open(temp_filename, "w") as temp_file:
                for contact in self.contacts:
                    temp_file.write(f"{contact.name},{contact.phone_number},{contact.email},{contact.address}\n")
            os.replace(temp_filename, self.filename)
            print(f"{contact_to_delete.name} has been deleted.")
        else:
            print(f"Contact with name '{name}' not found.")

def main():
    filename = "contacts.txt"
    cms = ContactManager(filename)

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            cms.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == '2':
            cms.view_all_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            results = cms.search_contact(search_term)
            if results:
                print("Search Results:")
                for result in results:
                    print(f"Name: {result.name}")
                    print(f"Phone Number: {result.phone_number}")
                    print("=" * 20)
            else:
                print("No contacts found.")

        elif choice == '4':
            name = input("Enter name of contact to delete: ")
            cms.delete_contact(name)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()

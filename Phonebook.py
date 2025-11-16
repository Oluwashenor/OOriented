import json
from dataclasses import dataclass


@dataclass
class Contact:
    name: str
    phone: str
    email: str = None


class Phonebook:
    contact = []

    def __init__(self):
        self.name = None
        self.phone = None

    @staticmethod
    def add_contact(name, phone):
        Phonebook.contact.append({
            "id": len(Phonebook.contact) + 1,
            "name": name,
            "phone": phone
        })
        Phonebook.add_contact_to_file()

    @staticmethod
    def add_contact_to_file():
        with open('contacts.json', 'w') as contacts_file:
            json.dump(Phonebook.contact, contacts_file)

    @staticmethod
    def remove_contact(idd):
        Phonebook.contact.pop(idd - 1)

    @staticmethod
    def show_contact():
        for contact in Phonebook.contact:
            print(contact["name"] + "--" + contact["phone"])


phonebook = Phonebook()
processing = True
while processing:
    print("Hello")
    print("What would you like to do?")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Show Contact")
    print("4. Exit")
    choice = input()
    if choice == "1":
        phonebook.add_contact("John", "123-456-7890")
    if choice == "2":
        choice = int(input("What is the Id of the contact? "))
        phonebook.remove_contact(choice)
    if choice == "3":
        phonebook.show_contact()

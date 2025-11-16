import json
from dataclasses import dataclass
from typing import List
import os

@dataclass
class Contact:
    name: str
    phone: str
    email: str = None

    def serialize(self) -> dict:
        return {'name': self.name, 'phone': self.phone, 'email': self.email}

    def to_json(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)


class Phonebook:
    contact: List[Contact] = []

    def __init__(self):
        pass

    @staticmethod
    def add_contact(contact: Contact):
        Phonebook.contact.append(contact)
        Phonebook.add_contact_to_file(contact)

    @staticmethod
    def add_contact_to_file(contact: Contact):
        filename = "contacts.json"
        temp_contacts = []

        if os.path.exists(filename):
            with open(filename, "r") as contacts_file:
                try:
                    temp_contacts = json.load(contacts_file)
                except json.JSONDecodeError:
                    temp_contacts = []
                except Exception as e:
                    print(f"Error reading contacts file {e}")
                    temp_contacts = []

        temp_contacts.append(contact.serialize())
        with open(filename, 'w') as contacts_file:
            json.dump(temp_contacts, contacts_file, indent=4)

    @staticmethod
    def remove_contact(idd):
        Phonebook.contact.pop(idd - 1)

    @staticmethod
    def show_contact():
        for contact in Phonebook.contact:
            print(contact.name + "--" + contact.phone)


phonebook = Phonebook()
print("Hello")
processing = True
while processing:
    print("What would you like to do?")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Show Contact")
    print("4. Exit")
    choice = input()
    if choice == "1":
        new_contact = Contact(name=input("What name would you like to add?"),
                              phone=input("What phone number would you like to add?"),
                              email=input("What email would you like to add?"))
        phonebook.add_contact(contact=new_contact)
    if choice == "2":
        choice = int(input("What is the Id of the contact? "))
        phonebook.remove_contact(choice)
    if choice == "3":
        phonebook.show_contact()

from collections import defaultdict


class ContactBook:
    def __init__(self):
        self.contacts = defaultdict(dict)

    def add_contact(self, name, phone, email=None):
        if name in self.contacts:
            print("=== Contact Alredy Exist.")
            return
        
        self.contacts[name]["phone"] = phone
        self.contacts[name]["email"] = email
        print("\n ==== Contact added successfully! ")

    def view_contact(self):
        print("-" * 50)
        for name, info in self.contacts.items():
            print(f"Name : {name}")
            print(f"Phone : {info['phone']}")
            print(f"Email : {info['email']}")
            print("-" * 50)

    def update_contact(self, name, phone=None, Email=None):
        if name not in self.contacts:
            print("\n ==== Contact not found")
            return
        
        else:
            if phone:
                self.contacts[name]["phone"] = phone
            if Email:
                self.contacts[name]["Email"] = Email
            
            print("\n ==== Contact updated successfully!")
            return
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f'\n ==== contact({name}) deleted')
            return
        print("\n ==== Contact not exist")

if __name__ == "__main__":
    book = ContactBook()

    while True:
        print("\nWelcome to contact book! ")
        print("1. add contatnt")
        print("2. view contants")
        print("3. update contant")
        print("4. delete contant")
        print("5. Exit")

        chose = input("Which Option? ")

        if chose == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email? ")
            book.add_contact(name, phone, email)

        elif chose == "2":
            print("\nList of contacts:")
            book.view_contact()

        elif chose == "3":
            name = input("Enter contact name: ")
            phone = input("Do you want change your phone number?(if dont want just click Enter.) ")
            email = input("Do you want change your email?(if dont want just click Enter.) ")
            book.update_contact(name, phone, email)

        elif chose == "4":
            name = input("Enter contact name: ")
            book.delete_contact(name)
            
        elif chose == "5":
            print("\n Goodbye.")
            break
        
        else :
            print("  Enter a valid number !!!! ")
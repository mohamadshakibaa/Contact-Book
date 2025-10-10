from collections import defaultdict
from typing import Optional


class ContactBook:
    """
    A simple in-memory contact book.

    Attributes:
        contacts (dict[str, dict[str, Optional[str]]]): mapping from name to info (phone, email).
    """

    def __init__(self) -> None:
        self.contacts = defaultdict(dict)

    def add_contact(self, name: str, phone: str, email: Optional[str] = None) -> None:
        """
        Add a new contact if it does not already exist.

        Args:
            name: Contact's display name (unique key).
            phone: Contact's phone number.
            email: Optional email address.
        """
        name = name.strip()
        if not name:
            print("\n === Name cannot be empty.")
            return
        if name in self.contacts:
            print("\n === Contact already exists.")
            return

        self.contacts[name]["phone"] = phone.strip()
        self.contacts[name]["email"] = (email or "").strip() or None
        print("\n ==== Contact added successfully! ====")

    def view_contact(self) -> None:
        """
        Print all contacts in a simple list.
        """
        if not self.contacts:
            print("---- No contacts yet.")
            return

        print("-" * 50)
        for name, info in self.contacts.items():
            phone = info.get("phone") or "-"
            email = info.get("email") or "-"
            print(f"Name  : {name}")
            print(f"Phone : {phone}")
            print(f"Email : {email}")
            print("-" * 50)

    def update_contact(self, name: str, phone: Optional[str] = None, email: Optional[str] = None) -> None:
        """
        Update a contact's phone and/or email.

        Args:
            name: Contact key to update.
            phone: New phone number (optional).
            email: New email address (optional).
        """
        name = name.strip()
        if name not in self.contacts:
            print("\n ==== Contact not found. ====")
            return

        if phone is not None and phone.strip():
            self.contacts[name]["phone"] = phone.strip()
        if email is not None:
            self.contacts[name]["email"] = (email or "").strip() or None

        print("\n ====>>> Contact updated successfully!")

    def delete_contact(self, name: str) -> None:
        """
        Delete a contact by name.

        Args:
            name: Contact key to delete.
        """
        name = name.strip()
        if name in self.contacts:
            del self.contacts[name]
            print(f"\n ==== Contact ({name}) deleted. ====")
        else:
            print("\n ==== Contact does not exist. ====")


if __name__ == "__main__":
    book = ContactBook()

    while True:
        print("\nWelcome to Contact Book!")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email (optional): ")
            book.add_contact(name, phone, email)

        elif choice == "2":
            print("\nList of contacts:")
            book.view_contact()

        elif choice == "3":
            name = input("Enter contact name to update: ")
            phone = input("New phone (press Enter to skip): ").strip()
            email = input("New email (press Enter to clear/skip): ").strip()
            book.update_contact(
                name,
                phone=phone or None,
                email=email if email != "" else None
            )

        elif choice == "4":
            name = input("Enter contact name to delete: ")
            book.delete_contact(name)

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Enter a valid number (1-5).")

contacts =[]

def add_contact(name, phone):
    contacts.append({"name": name, "phone": phone})
    print(f"Contact {name} added successfully!")

def view_contacts():
  if not contact:
  print("No contacts found.")
  else:
     print("\nContact List:")
     for i, contact in enumerate(contacts, 1):
     print(f"{i}. {contact['name']} - {contact['phone']}")

add_contact("Alice", 1234567890")
add_contact("Bob", 9876543210")

view_contacts()


def search_contact(name):

found = [contact for contact in contacts if contact["name].lower() == name.lower()]

if found:

 for contact in found:
  print(f"\nFound: [contact['name']} - (contact['phone']}")

else:

 print("\nSorry, no contact found with that name you searched.")

search_contach("Alica")
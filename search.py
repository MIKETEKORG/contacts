def search_contact(name):

found = [contact for contact in contacts if contact["name].lower() == name.lower()]

if found:

 for contact in found:
  print(f"\nFound: [contact['name']} - (contact['phone']}")

else:

 print("\nSorry, no contact found with that name you searched.")

search_contach("Alica")
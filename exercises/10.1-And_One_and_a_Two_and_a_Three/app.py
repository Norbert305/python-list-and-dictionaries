contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:

def contact_list(contact):
    for key in contact:
        print(f"{key} : {contact[key]}")

contact_list(contact)


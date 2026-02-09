phone = input("Enter phone number: ")
email = input("Enter email id: ")

if phone.isdigit() and len(phone) == 10 and "@" in email:
    print("Valid details")
else:
    print("Invalid details")

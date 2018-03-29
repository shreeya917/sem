phonebook={
    "Shreeya":"9861814343",
    "Samriddhi":"9861289111"
}

def f(phonebook):
    phone=input("Enter your name:")
    print(phonebook.get(phone,"Contact not found"))

f(phonebook)
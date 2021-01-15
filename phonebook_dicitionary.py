phonebook_dict = {
    "Alice": "703-493-1834",
    "Bob": "857-384-124",
    "Elizabeth": "484-584-2923"

}
phonebook_dict["Kareem"] = "938-489-1234"
del phonebook_dict["Alice"]
phonebook_dict["Bob"] = "968-345-2345"
print(phonebook_dict["Elizabeth"])

for name, number in phonebook_dict.items():
    print(name + ": " + number)
    

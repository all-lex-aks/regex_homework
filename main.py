from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts_list1 = []
pattern = r"(8|\+7)[\s-]*?\(?(\d..)\)?[\s-]*?(\d..)[\s-]*(\d.)[\s-]*(\d.)([\s-]*?\(?(доб\.)?\)?[\s-]*?(\d+)\)?)?"
for list in contacts_list:
    lastname = " ".join(list[:3]).replace("  ", " ").split(" ")[0]
    firstname = " ".join(list[:3]).replace("  ", " ").split(" ")[1]
    surname = " ".join(list[:3]).replace("  ", " ").split(" ")[2]
    organization = list[3]
    position = list[4]
    email = list[-1]
    phone = list[5]
    correct_phone = re.sub(pattern, r"+7(\2)\3-\4-\5 \7\8", phone).rstrip()
    contacts_list1.append([lastname, firstname, surname, organization, position, correct_phone, email])

contacts_dict = {}
unique_person = []
for list in contacts_list1:
    key = f"{list[0]} {list[1]}"
    if key not in unique_person:
        unique_person.append(key)
        contacts_dict[key] = {"lastname": list[0], 
                               "firstname": list[1], 
                               "surname": list[2], 
                               "organization": list[3], 
                               "position": list[4], 
                               "correct_phone": list[5], 
                               "email": list[6]}
    else:
        if contacts_dict[key]["lastname"] == "":
            contacts_dict[key]["lastname"] = list[0]
        if contacts_dict[key]["firstname"] == "":
            contacts_dict[key]["firstname"] = list[1]
        if contacts_dict[key]["surname"] == "":
            contacts_dict[key]["surname"] = list[2]
        if contacts_dict[key]["organization"] == "":
            contacts_dict[key]["organization"] = list[3]
        if contacts_dict[key]["position"] == "":
            contacts_dict[key]["position"] = list[4]
        if contacts_dict[key]["correct_phone"] == "":
            contacts_dict[key]["correct_phone"] = list[5]
        if contacts_dict[key]["email"] == "":
            contacts_dict[key]["email"] = list[6]    
        
# print(unique_person)
# pprint(contacts_dict)

contacts_list2 = []
for person in unique_person:
    contacts_list2.append([contacts_dict[person]["lastname"], 
                           contacts_dict[person]["firstname"], 
                           contacts_dict[person]["surname"], 
                           contacts_dict[person]["organization"],
                           contacts_dict[person]["position"],
                           contacts_dict[person]["correct_phone"],
                           contacts_dict[person]["email"]])

pprint(contacts_list2)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list2)
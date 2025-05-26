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
pprint(contacts_list1)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list1)
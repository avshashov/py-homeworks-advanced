import csv
import re


def format_file(contacts):
    fullname_pattern1 = r'([А-Я]\w+)[ ,]([А-Я]\w+)[ ,](([А-Я]\w+((вич)|(вна))))?,{1,3}'
    fullname_pattern2 = r'([А-Я]\w+)[ ,]([А-Я]\w+)[ ,](([А-Я]\w+((вич)|(вна))))?,{1,3}(,{2})'
    phone_pattern = r'((\+7)|(8))\s?\(?(\d{3})\)?\s?-?(\d{3})-?(\d{2})-?(\d{2}\s?)(\(?(доб\.) (\d{4})\)?)?'

    result = []
    for contact in contacts:
        contact = ','.join(contact)

        fullname1 = re.search(fullname_pattern1, contact)
        fullname2 = re.search(fullname_pattern2, contact)
        if fullname1:
            contact = re.sub(fullname_pattern1, r'\1,\2,\3,', contact)
        if fullname2:
            contact = re.sub(fullname_pattern2, r'\1,\2,\3,\8,', contact)

        phone = re.search(phone_pattern, contact)
        if phone:
            contact = re.sub(phone_pattern, r'+7(\4)\5-\6-\7\9\10', contact)

        result.append(contact.split(','))
    return result


def merge_duplicates(contacts):
    merge_contacts = [contacts[0]]

    for contact in contacts[1:]:
        lastname, firstname, surname = contact[0], contact[1], contact[2]
        organization, position = contact[3], contact[4]
        phone, email = contact[5], contact[6]

        for column in contacts[1:]:
            if column[0] == lastname and column[1] == firstname:
                if surname == '' and column[2] != '':
                    contact[2] = column[2]
                if organization == '' and column[3] != '':
                    contact[3] = column[3]
                if position == '' and column[4] != '':
                    contact[4] = column[4]
                if phone == '' and column[5] != '':
                    contact[5] = column[5]
                if email == '' and column[6] != '':
                    contact[6] = column[6]

        if contact[:7] not in merge_contacts:
            merge_contacts.append(contact[:7])

    return merge_contacts


with open('phonebook_raw.csv', encoding='utf-8') as f:
    contacts = list(csv.reader(f))
    edit_contacts = merge_duplicates(format_file(contacts))

with open('new_contacts.csv', 'w', encoding='utf-8', newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(edit_contacts)

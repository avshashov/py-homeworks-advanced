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


with open('phonebook_raw.csv', encoding='utf-8') as f:
    contacts = list(csv.reader(f))
    edit_contacts = format_file(contacts)

with open('new_contacts.csv', 'w', encoding='utf-8', newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(edit_contacts)

# fullname_pattern = r'^[А-Я]\w+[ ,][А-Я]\w+[ ,]'
# surname_pattern = r'[А-Я]\w+((вич)|(вна))'
# organization_pattern = r'(ФНС)|(Минфин)'
# position_pattern = r'((главный.*лиц)|(cоветник.*технологий))'
# phone_pattern = r'((\+7)|(8))\s?\(?(\d{3})\)?\s?-?(\d{3})-?(\d{2})-?(\d{2})( \(?(доб\.) (\d{4})\)?)?'
# email_pattern = r'[A-z].*ru'

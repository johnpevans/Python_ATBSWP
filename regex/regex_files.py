#! python3

import re, pyperclip

#First name, middle initial if applicable with period, last name with symbol if applicable

fullName = re.compile(r'''
(
(^[A-Z]{1}[a-z]+)
(\s[A-Z]?[.]?\s?)
([A-Za-z]{1,3}.[A-Z][a-z]+)
)''', re.VERBOSE)

phoneRegex = re.compile(r'''
(
((\d{3})| (\(\d{3}\)))?
(\s|-)
\d{3}
-
\d{4}
(((ext(\.)?\s)|x)
(\d{2,5}))?
)''', re.VERBOSE)

emailRegex = re.compile(
'''
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+
''', re.VERBOSE)

text = pyperclip.paste()

allPhoneNumbers = []
allNames = []

extractedName = fullName.findall(text)
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

for phone in extractedPhone:
    allPhoneNumbers.append(phone[0])

for name in extractedName:
    allNames.append(name[0])

result = '\n'.join(allNames) + '\n' + '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

#Create a database to sort and store the information collected to make it retrievable

#Copies to clipboard so all you have to do is CTRL-V on selected document
pyperclip.copy(result)

"""
A regular expression  script for extracting
phones and emails from text copied to clipboard

NOTE: Change the phone regex according to your requirements
Current Format : 123-456-7890 | (123) 456-7890 | 123-456-7890 ext. 1234 | 123-456-7890 ext 12345

"""

import re, pyperclip

# Regex for Phone Numbers

phoneRegex = re.compile(r'''
	(
	((\d\d\d) | (\(\d\d\d\)))?  # Area code 
	(\s|-)                   # a seprator
	\d\d\d                   # first three digits of number
	-                        # a seperator
	\d\d\d\d                 # last 4 digits of number
	(((ext(\.)?\s) | x)      # Extension word
	(\d{2,5}))?              # Extension Number
	)
	''', re.VERBOSE)

#Regex for Email Address

emailRegex = re.compile(r'''
	[a-zA-Z0-9.+_]+   # First part of the email
	@                # @ sign
	[a-zA-Z0-9.+_]+  # domain name 
	''', re.VERBOSE)

# Get the text from the clipboard
text = pyperclip.paste()

phoneNumbers = phoneRegex.findall(text)
emailAddresses = emailRegex.findall(text)

print("Extracted..")

allphones = []

for phones in phoneNumbers:
	allphones.append(phones[0])

result = '\n'.join(allphones) + '\n' + '\n'.join(emailAddresses)

pyperclip.copy(result)

print("Copied to Clipboard.")
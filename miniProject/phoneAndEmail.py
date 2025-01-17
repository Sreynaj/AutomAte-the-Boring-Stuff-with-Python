#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

print("Finds phone numbers and email addresses on the clipboard.")
import re

import pyperclip

# Create phone regex.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # Area code (optional)
    (\s|-|\.)?              # Separator (optional)
    (\d{3})                 # First 3 digits
    (\s|-|\.)               # Separator
    (\d{4})                 # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension (optional)
)''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # Username
    @                       # At symbol
    [a-zA-Z0-9.-]+         # Domain name
    (\.[a-zA-Z]{2,4})      # Dot-something
)''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []

# Find phone numbers
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8]:  # Check if extension exists
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

# Find email addresses
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

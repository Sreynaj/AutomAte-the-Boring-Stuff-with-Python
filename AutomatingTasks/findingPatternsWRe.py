import re  # Step 1: Import the regex module

# Step 2: Create a Regex object
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')  # Matches the pattern XXX-XXX-XXXX

# Sample string to search
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# Step 3: Search for the pattern in the string
match = phone_regex.search(message)

# Step 4: Check if a match was found and retrieve the matched text
if match:
    print('Phone number found: ' + match.group())
else:
    print('No phone number found.')

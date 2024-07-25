import re

greedyHaRegex = re.compile(r'(HA){3,5}')
mo1 = greedyHaRegex.search('HAHAHA')
mo1.group()
print ("Greedy:" + mo1.group())

nonGreedyHaRegex = re.compile(r'(HA){3,5}?')
mo2 = nonGreedyHaRegex.search('HAHAHA')
mo2.group()
print ("No Greedy:" + mo2.group())

#Find all method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')

print(mo.group())
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

#characters classes
xmasRegex = re.compile (r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(xmasRegex.findall)

#matching everything with a dot-star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

print("\ncase insensitive matching")

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocents.').group())
print(robocop.search('AI, why does your programming book talk about robocop so much?').group())

#Substituting Strings with the sub() Method
print("\nSubstituting Strings with the sub() Method")
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED' , 'Agent Alice gave the secret docutments to Agent bob.'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

#Combining re.ignorecASe, re.dotAll, and re.VerBoSe
print("\nCombining re.ignorecASe, re.dotAll, and re.VerBoSe")
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
print(someRegexValue)

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
print(someRegexValue)

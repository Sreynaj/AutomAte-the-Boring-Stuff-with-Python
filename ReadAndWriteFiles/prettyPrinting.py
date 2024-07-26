import pprint

cats = [{'name': 'Zophie', 'desc': 'Chbby'}, {'name' : 'Pooka', 'desc' : 'Fluffy'}]
pprint.pformat(cats)

fileObj = open('myCats.py', 'w') 
fileObj.write('cats = ' + pprint.pformat(cats) + '\n') 

fileObj.close()
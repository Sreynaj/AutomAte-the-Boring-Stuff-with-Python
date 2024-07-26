helloFile = open('helloFile.txt', 'w')
helloFile.write('hello world!\n')

helloFile.close()
helloFile = open('helloFile.txt', 'a')
helloFile.write("Bacon is not a vegetable")

helloFile.close()
helloFile = open('helloFile.txt')
content = helloFile.read()
helloFile.close()
print(content)
import shelve

shelfFile = shelve.open('mydata')

cats= ['Zophie' , 'Pooka' , 'Simon'] 
type(shelfFile)

list(shelfFile.keys())

shelfFile['Cat'] = cats
shelfFile.close()


from unicodedata import name


catNames = []
while True:
    print('Enter name of the cat'+str(len(catNames)+1)+'(enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are: ')
for name in catNames:
    print (' '+ name)

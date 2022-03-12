from http.client import BAD_GATEWAY
from unicodedata import name


birthdays = {'Alice':'JAN 1','Deepan':'MAY 21'}
while True:
    print('Enter a name: (blank to exit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I donot have information about birthday for '+ name)
        print('What is their birthday? ')
        bday = input()
        birthdays[name] = bday
        print('Birthday Database updated')
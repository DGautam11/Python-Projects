from unicodedata import name


pets = ['houdy','bruno','cookie']
print('Enter a pet name:')
name = input()
if name not in pets:
    print('You donot have pet name '+ name)
else:
    print('You have a pet name ' + name)
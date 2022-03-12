import pprint #imports pprint module 
"""

The program loops over each character in 
the message variable’s string, 
counting how often each character appears.
The setdefault() method call ➊ ensures that
the key is in the count dictionary
(with a default value of 0) so the program 
doesn’t throw a KeyError error 
when count[character] = count[character] + 1 is
executed

"""


message = 'It was a bright cold day in Frburaru'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count [character] + 1

pprint.pprint(count)
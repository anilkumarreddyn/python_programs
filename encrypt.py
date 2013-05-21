#SD
#Given a string in all caps, this program shifts the characters to left by 4, i.e A becomes E and Z becomes D
#!/usr/bin/python

import sys
import string

def cypher_string(string):
  cypher_string = ''
  for c in string:
    if ord(c) < 65 or ord(c) > 90: 
      cypher_string += c 
    elif ord(c) >= 87 : 
      x = (ord(c)+4)%90
      cypher_string += chr(x+64)
    else :
      cypher_string += chr(ord(c)+4)
  return cypher_string

def decypher_string(string):
  decypher_string = ''
  for c in string:
    if ord(c) < 65 or ord(c) > 90:
      decypher_string += c
    elif ord(c) <= 68:
      x = (ord(c)- 4) 
      if x < 65:
        decypher_string += chr(90-(64-x))
    else :
      decypher_string += chr(ord(c)-4)
  return decypher_string 

def main(): 
  strings = sys.argv[1:]
  if strings == []:
    print "usage: python encrypt.py <YOUR STRING IN CAPS>"
    sys.exit(2)

  for string in strings:
    cyphered = ''
    decyphered = ''
    print "Given String      -->  " + string
    cyphered = cypher_string(string)
    print "Encrypted String  -->  " + cyphered
    decyphered = decypher_string(cyphered)
    print "Decyphered String -->  " + decyphered

if __name__ == '__main__':
  main()
    
  

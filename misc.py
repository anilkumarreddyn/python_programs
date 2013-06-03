#SD 
# Misc programs
#!/usr/bin/python

import timeit
import re 

def ret_len(l):
  # Returns sum of all elements in string using recurssion
  if len(l) == 1: 
    return l[0]
  else : 
    return l[0] + ret_len(l[1:])

def fact(n):
  # Returns factorial of given number using recurssion
  if n == 0: 
    return 1
  else :
    return n*fact(n-1)

def combos(l):
  # Returns an list of lists with all possible arrangements of original list
  if len(l) == 1 or len(l) == 0:
    return l 
  else : 
    x = []
    for i in range(len(l)):
      this_elem = l[i]
      other_elem = l[:i] + l[i+1:]
      for seating_arrangement in combos(other_elem):
        x.append([this_elem] + [seating_arrangement])
    return x

def lambda_ex():
  #Sorting based on second element in tuple
  a = [('a',1,'#'),('b',9,'!'),('c',4,'%'),('e',3,'*')]
  return sorted(a, key=lambda x: x[1])

def dup():
  # Returns unique elements in given 2 lists
  m = ['a','c','e','f','d','h']
  l = ['a', 'b', 'c', 'a', 'd', 'c']
  #return [x for x in l if x not in set(m)] + [y for y in m if y not in set(l)]
  return list((set(l)-set(m)) | (set(m)-set(l)))    
  #return list(set(l)-set(m))    

def str_match():
  # returns interface with status Up
  str = '''
        iface     flag      status
        --------------------------
         1/1     enabled     Up
         2/2     disabled    Down
         3/3     enabled     NA
         4/3     enabled     Up
        '''
  #new_str = ' '.join(str.rsplit())
  #print new_str
  x = re.findall(r'(\d/\d).*?Up',str)
  #x = re.findall(r'(\d/\d)\s+\S+\s+Up',new_str)
  #x = re.findall(r'(\d/\d).*?Up',new_str) # will not work
  if x :  
    return x
  else : return 0

if __name__ == '__main__':
  #print timeit.timeit("dup()", setup="from __main__ import dup",  number=100000)
  #print timeit.timeit("str_match()", setup="from __main__ import str_match", number=100000)
  print str_match()
  print lambda_ex()
  l = [1,2,3,4,5]
  a = ['abc','xzt','dafd']
  print ret_len(l)
  print fact(5)
  print combos(a)



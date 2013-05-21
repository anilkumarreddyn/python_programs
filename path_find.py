#SD
#Lists the files in a given dir
#!/usr/bin/python 

import sys
import os 

def List(dir):
  filenames = os.listdir(dir)
  for files in filenames:
    path = os.path.join(dir, files)
    print path	 
    print os.path.abspath(path) 

def main():
  if (sys.argv[1:]):
    List(sys.argv[1])
  else:
    print "usage : python path_find.py <dir>" 
    sys.exit(2)

if __name__ == '__main__':
  main()

  

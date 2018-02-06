import os
from os.path import join
for (dirname, dirs, files) in os.walk('.'):
 for filename in files:
   if filename.endswith('.txt'):
       filepath = os.path.join(dirname, filename)
       filecontent = open(filepath, 'r')
       get_lines = list()
       for line in filecontent:
        get_lines.append(line)
       filecontent.close()
       print filepath
       for elem in get_lines:
          print elem      

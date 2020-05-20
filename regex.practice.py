import re

cell = "<Cell 'April'.N6>"

print('------------')
colfind = re.findall('\.[A-Z]', cell)
print(colfind)
column = re.sub('\.', colfind)
print(column)
print('------------')
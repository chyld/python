filename1 = 'ch04.py'
filename2 = 'temp.py'

with open(filename1) as file:
    for line in file:
        print('*** ', line.rstrip())

with open(filename2, "a") as file:
    file.write('3.14159162\n')

try:
    x = 3
except FileNotFoundError:
    pass
else:
    print('done')

import json
odds = list(range(1, 30, 2))
with open('odds.json', 'w') as file:
    json.dump(odds, file)

with open('odds.json', 'r') as file:
    nums = json.load(file)
print('nums from disk:', nums)

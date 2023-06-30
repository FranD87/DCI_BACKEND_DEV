import sys
import getopt

file_name = sys.argv[0]
other_data = sys.argv[1:]
rec_data, not_rec_data = getopt.getopt(other_data, 'hm:', ['help', 'massage=', 'name='])
# print(rec_data)
# print(not_rec_data)
name = None
for item in rec_data:

    if item[0] == '-h' or item[0] == '--help':
        print('Some help massage')
    elif item[0] == '-m' or item[0] == '--massage':
        print('massage is', item[1])
    elif item[0] == '--name':
        name = item[1]

if name:
    print('Hello', name)
else:
    print('Hello User')


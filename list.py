import json

a = [
    {'id': 1},
    {'id': 2},
    {'id': 3},
    {'id': 3},
    {'id': 1}
    ]
list = []
for items in a:
    list.append(items['id'])

print (max(list))
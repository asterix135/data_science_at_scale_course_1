import json

f1=open('test_friends.json', 'w+')
a = [['a', 'b'], ['b', 'c'], ['b', 'a']]
jenc = json.JSONEncoder()
for item in a:
    print >>f1, jenc.encode(item)
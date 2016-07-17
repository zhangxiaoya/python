from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(3)

print(d)


dd= defaultdict(set)
dd['a'].add(1)
dd['b'].add(2)
dd['c'].add(3)
print(dd)

ddd ={}
ddd.setdefault('a',[]).append(1)
ddd.setdefault('a',[]).append(2)
ddd.setdefault('b',[]).append(3)
print(ddd)



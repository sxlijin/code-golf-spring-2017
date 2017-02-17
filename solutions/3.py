import itertools as i
f=open('inputs/3.txt').readlines()
w=set(w[:-1] for w in f)
d ={a+b:(a,b) for a,b in i.permutations(w, 2)}
r=set()
for c in d:
    if c in w:
        r.add(c)
        r.add(d[c][0])
        r.add(d[c][1])
w.difference_update(r)
print(w)

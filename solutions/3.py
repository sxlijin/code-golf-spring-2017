import itertools as i
f=open('inputs/3.txt').readlines()
s=set
w=s(l[:-1] for l in f)
d={a+b:(a,b) for a,b in i.permutations(w,2)}
print w.difference(s().union(*(s(d[c]+(c,)) for c in d if c in w)))

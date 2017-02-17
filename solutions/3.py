import itertools as i
f=open('inputs/3.txt').readlines()
w=set(l[:-1] for l in f)
d={a+b:(a,b) for a,b in i.permutations(w, 2)}
print '\n'.join(set().union(*(set(d[c]+(c,)) for c in d if c in w)))

import itertools as i
f=[map(float,x.split()) for x in open('inputs/4.txt').readlines()]
slopes=[(y2-y1)/(x2-x1) for (x1, y1), (x2, y2) in i.combinations(f, 2)]
m=sum(slopes)/len(slopes)
b=0
def sos(l, m, b): return sum((y-m*x+b)**2 for x, y in l)
for i in range(100000):
    if sos(f, m, b) > sos(f, m+0.0001, b): m=m+0.0001
    if sos(f, m, b) > sos(f, m-0.0001, b): m=m-0.0001
    if sos(f, m, b) > sos(f, m, b+0.0001): b=b+0.0001
    if sos(f, m, b) > sos(f, m, b-0.0001): b=b-0.0001
print(b/m)

from operator import mul
r=range(2,41)
p=[x for x in r if 0 not in (x%y for y in r if x!=y)]
def f(n):
 for i in p:
  if n == i: return (n,)
  if n % i == 0: return (i,)+f(n/i)

def x(t,k=0):
    sp = ' '*k
    if len(t) == 1:
        return ('%s<prime value="%d">\n%s</prime>' % (sp, t[0], sp))
    else:
        return ('%s<composite value="%d">\n%s\n%s\n%s</composite>'%(sp, reduce(mul, t, 1), x(t[:1], k+2), x(t[1:], k+2), sp))

print((f(500)))
print(x(f(500)))

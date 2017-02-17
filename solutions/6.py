import re
def r(l):
 d={}
 for i,s in enumerate('zero one two three four five six seven eight nine ten eleven twelve     thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()):d[s]=str(i)
 for i,s in enumerate('ten twenty thirty forty fifty sixty seventy eighty ninety'.split()): d[s]=str(10*(i+1))
 l = l.replace(' and ',' ').replace('-',' ').replace(',',' ')
 for a in d:
  l = l.replace(a,d[a]).replace(' hundred','*100')
  if 'thousand' in l:l='('+l.replace(' thousand',')*1000')
 return eval(' '.join(l.split()).replace(' ','+'))
f=open('inputs/6.txt').readlines()
for l in f: print r(l[:-1])

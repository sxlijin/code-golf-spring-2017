r=range(2,1001)
p=[x for x in r if 0 not in (x%y for y in r if x!=y)]
print '\n'.join([str(len([x for x in p if x <= int(k)])) for k in open('inputs/1.txt').readlines()])



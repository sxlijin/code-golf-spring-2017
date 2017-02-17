n='1234567890'
def parse(s):
    t=[]
    for ch in s:
        t.append(ch)
        while len(t) >= 3 and t[-3] in '+-*/' and t[-2] in n and t[-1] in n:
            t[-3:] = [str(eval(t[-2]+t[-3]+t[-1]))]
    return t[0]

print '\n'.join(parse(l) for l in open('inputs/2.txt').readlines())

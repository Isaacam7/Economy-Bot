import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.pow,
}

def solve(problem):
    problem = clean(problem)
    if len(problem) == 3:
        a = float(problem[0])
        b = problem[1]
        c = float(problem[2])
        return ops[b](a, c)

    if len(problem) > 3:
        p1 = 0
        p2 = 0
        i = 0
        olen =len(problem)
        nlen = len(problem)
        while ')' in problem:
            if i == len(problem):
                i = 0
            if i == 0:
                olen = nlen
            if problem[i] == '(':
                p1 = i
            if problem[i] == ')':
                p2 = i
                problem[p2] = solve(problem[p1+1:p2])
                for i in range(p2-1,p1-1,-1):
                    problem.pop(i)
                p1 = 0
                p2 = 0
                nlen = len(problem)
            i += 1
            if nlen < olen:
                i = 0
        if len(problem) == 1:
            return problem[0]

        for i in range(len(problem)):
            if problem[i] == '^':
                a = float(problem[i - 1])
                b = problem[i]
                c = float(problem[i + 1])
                problem[i + 1] = ops[b](a, c)
                problem[i - 1] = 'f'
                problem[i] = 'f'

        while 'f' in problem:
            problem.remove('f')

        if len(problem) == 1:
            return problem[0]

        for i in range(len(problem)):
            if problem[i] in ['*', '/', '%']:
                a = float(problem[i - 1])
                b = problem[i]
                c = float(problem[i + 1])
                problem[i + 1] = ops[b](a, c)
                problem[i - 1] = 'f'
                problem[i] = 'f'

        while 'f' in problem:
            problem.remove('f')

        if len(problem) == 1:
            return problem[0]

        a = float(problem[0])
        b = problem[1]
        c = float(problem[2])
        tot = ops[b](a, c)
        for i in range(3, len(problem), 2):
            j = problem[i]
            k = float(problem[i + 1])
            tot = ops[j](tot, k)

        return tot

def deflag(data):
    while 'f' in data:
        data.remove('f')
    return data

def clean(prb):

    for i in range(1, len(prb)):
        if prb[i] == '.':
            prb[i + 1] = prb[i - 1] + prb[i] + prb[i + 1]
            prb[i - 1] = 'f'
            prb[i] = 'f'

    prb = deflag(prb)

    for i in range(1, len(prb)):
        try:
            if (float(prb[i - 1]) or float(prb[i - 1]) == 0) and (float(prb[i]) or float(prb[i]) == 0):
                prb[i] = prb[i - 1] + prb[i]
                prb[i - 1] = 'f'
        except ValueError:
            pass

    prb = deflag(prb)

    for i in range(1, len(prb)):
        if prb[i] == '-' and prb[i - 1] in ['+','-','*','/','%']:
            prb[i + 1] = '-' + prb[i + 1]
            prb[i] = 'f'

    if prb[0] == '-':
        prb[0] = 'f'
        prb[1] = '-' + prb[1]

    prb = deflag(prb)

    return prb

"""""
#code to test
prb = list(input('input problem: '))
while ' ' in prb:
    prb.remove(' ')
print(f"{solve(prb)}")
"""""

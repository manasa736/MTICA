##s=input()
##s.split()
##print(len(s))


def solveProblem(s):
    lst=s.split()
    return [len(i) for i in lst]

inp=input()
print(*solveProblem(inp))

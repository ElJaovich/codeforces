def countProblems(n):
    count  = 0
    count1 = 0
    for count in range(int(n)):
        solvedProblems = 0
        problem = list(input().split(' '))
        for i in range(len(problem)):
            solvedProblems += int(problem[i])
        if solvedProblems >= 2:
            solvedProblems = 0
            count1 += 1
    print(count1)
                
countProblems(input())
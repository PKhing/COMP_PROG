    n = int(input())
    if n==0:
        print(0)
        print(0)
        exit(0)
    a = input().split()
    union = set(a)
    inter = set(a)

    for i in range(n-1):
        tmp = set()
        for j in input().split():
            union.add(j)
            if j in inter:
                tmp.add(j)
        inter = tmp
    print(len(union))
    print(len(inter))

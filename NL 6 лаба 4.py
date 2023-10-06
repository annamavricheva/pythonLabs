list_1 = list(map(int, input().split()))
list_0 = set()
for n in list_1:
    if n in list_0:
        print('YES')
    else:
        print('NO')
        list_0.add(n)

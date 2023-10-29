towns = {}
for i in range(int(input())):
    s = input().split()
    country=s[0]
    town=s[1:]
    towns[country] = town
for i in range(int(input())):
    a = input()
    for j in towns:
        if a in towns[j]:
            print(j)

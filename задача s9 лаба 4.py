s=str(input())
a=s.find('f')
s_new=s[a+1::]
c= len(s[:a])
if a==-1:
    print('-2')
else:
    a1_new=s_new.find('f')
    if a1_new==-1:
        print('-1')
    else:
        print(a1_new+c+1)
    
    

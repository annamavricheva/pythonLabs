output=open('СФ1.txt', 'r')
s=[]
count=0
while True:
    list1=readline()
    s=s.append(list1)
    a=max(s)
    while a>=10:
        i=a%10
        if i==0:
            count=count+1
        a=a//10
    if not line:
        break
print(count)
    
    

list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
list1_new=list(set(list1))
list2_new=list(set(list2))

count=0
for i in range(len(list2_new)):
    a = list2_new[i]
    for j in range (len(list1_new)):
        b=list1_new[j]
        if a==b:
            count=count+1
print(count)
            
        

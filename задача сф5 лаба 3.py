output=open(r"C:\Users\annma\OneDrive\Рабочий стол\pythonLabs\СФ5.txt", 'r')
file=open('result.txt', 'w')
while True:
    n=output.readline()
    list1=output.readlines()
    list1=[int(i.strip()) for i in list1]
    s=list(list1)
    for i in s:
        if int(i)%2==0:
            file.write(str(i)+'\n')
    break
file.close()
            
    
    

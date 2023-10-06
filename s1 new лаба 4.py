def sum_digits(s):
    summ=0
    for a in s:
        if a=='1'or a=='2' or a=='3' or a=='4' or a=='5' or a=='6' or a=='7' or a=='8' or a=='9':
            a=int(a)
            summ=summ+a
    return summ
print(sum_digits(s=input()))

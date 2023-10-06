def power(a, n):
    result = 1
    for i in range(abs(n)):
        result=result*a
    if n >= 0:
        return result
    else:
        return 1 / result


print(power(float(input()), int(input())))
  

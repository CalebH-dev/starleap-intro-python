# A(m, n) = 	
# ⎧               n+1	if  m = 0 
# ⎪               A(m−1, 1)	if  m > 0  and  n = 0 
# ⎨               A(m−1, A(m, n−1))	if  m > 0  and  n > 0. 
# ⎪
# ⎩	


num = 0


def ackerman(m, n, count = 1):
    global num
    num = n + 1
    # print("recursion depth: ", count)
    if(m == 0):
       print("m == 0, count: ", count)
       return n + 1
    elif(m > 0 and n == 0):
        print("condition 2, count: ", count)
        return ackerman(m-1, 1, count+1)
    elif(m > 0 and n > 0):
        print("condtion 3, count: ", count)
        return ackerman(m-1, ackerman(m, n-1, count+1), count + 1)
    else: 
        print("returned 0 for count: ", count)
        return 0

    return -1

print(ackerman(3,3))
print("Num: " + str(num))

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(10))




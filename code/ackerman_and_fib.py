# A(m, n) = 	
# ⎧               n+1	if  m = 0 
# ⎪               A(m−1, 1)	if  m > 0  and  n = 0 
# ⎨               A(m−1, A(m, n−1))	if  m > 0  and  n > 0. 
# ⎪
# ⎩	


import time 

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




def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        val = fib(n-1) + fib(n-2)
        return val
    

def time_fib_wrap(n):

    print("Fib of ", n)
    start = time.time()

    print(fib(n))

    end = time.time()
    total = end - start
    total = total % 1 * 10000
    print("Total time (ms): ", total)


def time_and_cache_fib_wrap(n):

    print("Fib of ", n)
    start = time.time()

    print(fib_with_cache(n))

    end = time.time()
    total = end - start
    total = total % 1 * 10000
    print("Total time (ms): ", total)



cache = {}


def fib_with_cache(n):
    if n in cache:
        return cache[n]
    elif n < 2:
        return n
    else:
        cache[n] = fib_with_cache(n-1) + fib_with_cache(n-2)
        # cache[n] = result
        return cache[n]




# time_fib_wrap(10)
# time_fib_wrap(20)
# time_fib_wrap(30)
# time_fib_wrap(40)

# print("\n\n")
time_and_cache_fib_wrap(10)
time_and_cache_fib_wrap(20)
time_and_cache_fib_wrap(30)
time_and_cache_fib_wrap(40)
time_and_cache_fib_wrap(100)









##### Template for Chapter 5.14, Exercises 1 - 4 ######


print("********** Ch 5 Exercise 1 **********")

# Do your work for Exercise 1 here

import time

def time_since_epoch():
    long_time = time.time()
    days = long_time // (3600*24)
    hours = (long_time % (3600*24)) // 3600
    minutes = (long_time % 3600) // 60
    seconds = (long_time % minutes)
    print("days: " + str(round(days)))
    print("hours: " + str(round(hours)))
    print("minutes: " + str(round(minutes)))
    print("seconds: " + str(round(seconds)))

    # check
    # check = days*86400 + hours*3600 + minutes*60 #+ seconds
    # print(long_time % check)
    # print(check)


time_since_epoch()


print("********** Ch 5 Exercise 2 **********")

def fermat(a, b, c, n):
    if n <= 2:
        print("n !< 2")
    else:
        x = a**n + b**n
        y = c**n
        if x == y:
            print("equal")
        else:
            print("not equal")


fermat(1, 2, 3, 3)
        

print("********** Ch 5 Exercise 3 **********")




print("********** Ch 5 Exercise 3 **********")

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(3, 0)
recurse(4, 3)


print("********** Ch 5 Exercise 4 **********")

# Do your work for Exercise 4 here.

print("Ch 5 Exercise 4: Not implemented") # Delete this line when you write your code!

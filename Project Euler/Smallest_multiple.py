"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
import time
time1=time.time()
def max_of_two(x,y):
    if x>y:
        return x
    elif y>x:
        return y
    else:
        return x
def calculate_least_common_multiple(x=20):
    a,b=1,2
    num=max_of_two(a,b)
    while(a<=x):

        while(True):
            if((num%a==0)and(num%b==0)):
                a,b=a+1,num
                break 
            else:
                num+=1
                 
        
    return num
print(calculate_least_common_multiple())        
time2=time.time()
timedif=round(time2-time1,3)
print(f"Elapsed time to calculation : {timedif}")
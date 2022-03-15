"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""
import time
time1=time.time()
num=600851475143
rv=round(num**(1/2))+1
def max_of_two(x,y):
    """This function returns the maximum of two numbers."""
    if x>y:
        return x
    elif y>x:
        return y
    else:
        return x    

def is_prime(x):
    """Takes x and check whether its a prime number or not.
     Then returns True or False depend on the case."""
    x_sqrt=round(x**(1/2))+1

    for k in range(2,x_sqrt):
        
        if(x%k==0):
            return False
    return True

largestprime=1
for t in range(1,rv):
    if num%t==0:
        if t==1:
            if is_prime(num):
                largestprime=num
                
                break
        else:
            if (is_prime(num/t) and is_prime(t)):
                
                largestprime=max_of_two(num/t,t)
            elif(is_prime(t)):
                if t>largestprime:
                    largestprime=t
            elif(is_prime(num/t)):
                if (num/t)>largestprime:
                    largestprime=num/t
        
print(int(largestprime))

time2=time.time()
timedif=round(time2-time1,3)
print(f"The spend time for calculation is : {timedif}")
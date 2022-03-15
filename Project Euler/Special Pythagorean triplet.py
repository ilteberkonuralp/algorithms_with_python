"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
def check_pythagorean(x,y,z):
    if(x**2+y**2==z**2):
        return True
    else:
        return False

def optimize_values():
    a,b,c=1,2,997
    while(True):
        if(check_pythagorean(a,b,c)):
            return a*b*c
        else:
            if (c>b):
                a,b,c=a,b+1,c-1
                d,e,f=a,b,c
                for k in range(a,b):
                    if (d+1<e):
                        d,e,f=d+1,e,f-1
                        if(check_pythagorean(d,e,f)):
                            return d*e*f
                    else:
                        break
            
print(optimize_values())
"""A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

def is_palindrome(x):
    if str(x)==str(x)[::-1]:
        return True
    else:
        return False
def loop_for_palindrome(max=1000):
    recorder=[]
    for j in range(max,99,-1):
        for k in range(max,99,-1):
            if (is_palindrome((j)*(k))):
                if (j*k not in recorder):
                    recorder.append((j*k))
    print(sorted(recorder)[-1])
loop_for_palindrome()
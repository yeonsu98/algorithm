def total(n):
    if n==1:
        return 1
    
    return n + total(n-1)


n = total(3)
print("n =", n)

# practice
def power(n, exp):
    if exp == 0:
        return 1
    return n * power(n, exp-1)

n = power(2, 10)
print("n =", n)
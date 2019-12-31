#function for nth fibonacci number
count=0
def fib(n):
    if n<0:
        print("incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

num=int(input("Enter term in the sequence to display:"))
print(fib(num))

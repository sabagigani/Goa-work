def my_func(x,y):
    print(x * y)
my_func("hello",5)
def my_c(x,b):
    if x:
        print(b)
my_c(True,"hello")
def mu(x,u):
    print(x[0:u])
mu([1,2,3,4,5,6,7,8],5)
def n(b):
    print(b*b)
n(5)
def my_func_four(t):
    is_prime = True
    if t < 2:
        print(False)
    else:
        for i in range(2, t):
            if t % i == 0:
                is_prime = False
            else:
                continue
    print(is_prime)
my_func_four(8)
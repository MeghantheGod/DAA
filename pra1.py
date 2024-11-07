def fibonacci_iter(n):
    if n < 0:
        return -1, 1
    
    if n == 0 or n == 1:
        return n, 1
    
    steps = 1  # To account for the first iteration in the loop
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
        steps += 1  # Count each step of the loop
    return c, steps

def fibonacci_rec(n):
    if n < 0:
        return -1, 1
    if n == 0 or n == 1:
        return n, 1
    
    fib1, steps1 = fibonacci_rec(n - 1)
    fib2, steps2 = fibonacci_rec(n - 2)
    return fib1 + fib2, steps1 + steps2 + 1

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    iter_result, iter_steps = fibonacci_iter(n)
    rec_result, rec_steps = fibonacci_rec(n)
    print("Iterative Fibonacci:", iter_result)
    print("Iterative Steps:", iter_steps)
    print("Recursive Fibonacci:", rec_result)
    print("Recursive Steps:", rec_steps)


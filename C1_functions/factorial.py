def main():
    pass
    print(factorial(5))
    print(factorial_iterative(0))


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is defined only for n > 0")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


def factorial_iterative(n):
    factorial = 1
    if n < 0:
        raise ValueError("Factorial is defined only for n > 0")
    else:
        for i in range(n,0,-1):
            factorial *= i
        return factorial



if __name__ == '__main__':
    main()
    

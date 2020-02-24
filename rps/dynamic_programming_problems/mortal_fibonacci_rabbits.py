import rps.dynamic_programming_problems.fibonacci as fib


def main():
    time = int(input("Enter number of months"))
    lifespan = int(input("Enter the rabbit lifespan"))
    rabbits = fib.count_mortal_rabbits(time, lifespan)
    print(rabbits)


if __name__ == '__main__':
    main()

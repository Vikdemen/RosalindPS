"""
Calculates number of rabbit pairs after n months given k rabbits in a litter
"""
import rps_fibonacci as fib


def main():
    time = int(input("Please enter n \n"))
    litter = int(input("Please enter k \n"))
    rabbits = fib.count_rabbits(time, litter)
    print(rabbits)


if __name__ == '__main__':
    main()

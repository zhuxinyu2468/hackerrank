def print_formatted(number):
    # your code goes here
    # for i in range(1, number+1):
    #     octal = oct(i)5
    #     hexadecimal = hex(i)
    #     binary = bin(i)
    #     print(i, octal[2:], hexadecimal[2:], binary[2:])
        
    w = len("{0:b}".format(number))
    for i in range(1,n+1):
        print ("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=w))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
def print_formatted(number):
    width = len(bin(number))-2
    for i in range(1,number+1):
        # print(i,oct(i),hex(i),bin(i))
        d = str(i).rjust(width)
        o = oct(i)[2:].rjust(width)
        x = hex(i)[2:].rjust(width).upper()
        b = bin(i)[2:].rjust(width)
        print(d, o, x, b)
        
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

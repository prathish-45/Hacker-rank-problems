def print_formatted(number):
    # Determine the width of the binary representation of the largest number
    width = len(bin(number)[2:])
    print(width)
    print(bin(number)[2:])
    for i in range(1, number + 1):
        # Print the values in the required format with the correct width
        print(f"{i:>{width}} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
def main():
    import array as arr
    N = arr.array('i', [3, 4, 5, 1, 2, 3, 4, 9, 13, 0])
    a = int(input('Insert the first number: ')) #declare the variable a and initialized it how input
    i = int()
    flug = int()
    for i in range(len(N)):
        if a in N:
            flug = 0
            print(f'The number {a} is present in the array.')
            break
        else:
            flug += 1
    if flug > 0:    
        print(f'The number {a} is not present in the array.')

if __name__ == "__main__":
    main()





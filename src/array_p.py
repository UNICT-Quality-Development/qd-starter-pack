#def my function main
def main():
    import array as arr #import array as arr
    N = arr.array('i', [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]) #declare array
    a = int(input('Insert the first number: ')) #declare the variable a and initialized it how input
    i = int() #declare my index
    flug = int() #declare a flug

    #use a loop to reserch the number
    for i in range(len(N)):
        #create a condition where i check if the number exist in the array
        if a in N:
            #reinitialized my flug to 0
            flug = 0
            print(f'The number {a} is present in the array.') #print a phrase if the number is in the array
            break #exit to the loop
        else:
            flug += 1 #increment my flug
     #check if my flug is grater than 0       
    if flug > 0:    
        print(f'The number {a} is not present in the array.') #print a phrase if the number is not in the array

#check if the function main exits
if __name__ == "__main__":
    main()





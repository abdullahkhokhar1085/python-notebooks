rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('enterthe number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(0,i+1):
        # display nnumber
        print("*", end='')
    # new line after each row 
    print('')    
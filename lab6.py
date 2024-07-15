rows = 7
# if you want user to enter a number, uncomment the below line
# rows = int(input('enterthe number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display nnumber
        print(i, end='')
    # new line after each row 
    print('')       
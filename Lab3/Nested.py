start = 0;
stop = 10;
for b in range (10):
    for x in range (start,stop):
        print(x, sep=" ", end=" ")
        if x < 10 :
            print('{0:>2}'.format(""),end="")
        else :
         print('{0:>1}'.format(""),end="")
    start+=1
    stop+=1
    print("")

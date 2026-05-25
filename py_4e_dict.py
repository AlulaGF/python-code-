
    fname = input("Enter a file: ")
    fhand  = open(fname)
    many = {}
    for line in fhand:
     line = line.rstrip()
     wds = line.split()
    #print(wds)
     for w in wds:
        #print("+++++++>", "wds")
       # print("Befor",many)
        oldvalue = 0
        if w in many:
            oldvalue = many[w]
            print("Oldvalue:", oldvalue)
            many[w] = oldvalue + 1
            print('After', many)

